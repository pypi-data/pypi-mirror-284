import datetime
import io
import json
import logging
import time
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from urllib.parse import urljoin
from urllib3.util.retry import Retry

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)-8s] [%(name)s:%(lineno)s]: %(message)s',
)
LOG = logging.getLogger(__name__)

class LoggingAdapter(requests.adapters.HTTPAdapter):
    """
    Requests adapter that handles logging of server response.
    """
    def __init__(self, *args, **kwargs):
        logging.getLogger('urllib3.util.retry').setLevel(logging.DEBUG if logging.getLogger().level == logging.INFO else logging.WARNING)
        retry_strategy = Retry(total=3, status_forcelist=[429], backoff_factor=1)
        super(LoggingAdapter, self).__init__(max_retries=retry_strategy, *args, **kwargs)

    def send(self, request, **kwargs):
        request.headers['api-version'] = 2
        LOG.info("Request being sent to HTTP server")
        response = super(LoggingAdapter, self).send(request, **kwargs)
        LOG.info("Response received with status: %s", response.status_code)
        if not response.ok:
            LOG.error("Response content: %s", response.text)
            raise RuntimeError(f'Unexpected response status code: {response.status_code}')
        return response

class BDL:
    def __init__(self, client_id=None, client_secret=None, credentials_path=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.credentials_path = credentials_path
        self.session = None
        self.token = None
        self.host = 'https://api.bloomberg.com'
        
        if self.credentials_path:
            self.load_credentials()
        
        if not self.client_id or not self.client_secret:
            raise ValueError("client_id and client_secret must be provided either directly or via credentials_path")

        self.authenticate()

    def load_credentials(self):
        with io.open(self.credentials_path, encoding="utf-8") as credential_file:
            self.credentials = json.load(credential_file)
        self.client_id = self.credentials['client_id']
        self.client_secret = self.credentials['client_secret']
        expires_in = datetime.datetime.fromtimestamp(self.credentials['expiration_date'] / 1000) - datetime.datetime.utcnow()
        if expires_in.days < 0:
            LOG.warning("Credentials expired %s days ago", expires_in.days)
        elif expires_in < datetime.timedelta(days=30):
            LOG.warning("Credentials expiring in %s", expires_in)

    def authenticate(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth2_endpoint = 'https://bsso.blpprofessional.com/ext/api/as/token.oauth2'
        self.session = OAuth2Session(client=client)
        self.session.mount('https://', LoggingAdapter())
        self.token = self.session.fetch_token(token_url=oauth2_endpoint, client_id=self.client_id, client_secret=self.client_secret)
        LOG.info("Authenticated successfully")

    def test_connection(self):
        url = urljoin(self.host, '/eap/catalogs/')
        LOG.info('Testing connection to Bloomberg API')
        response = self.session.get(url)
        if response.status_code == 200:
            LOG.info("Connection to Bloomberg API successful")
        else:
            LOG.error("Failed to connect to Bloomberg API: %s", response.text)

    def get_catalog_id(self):
        catalogs_url = urljoin(self.host, '/eap/catalogs/')
        response = self.session.get(catalogs_url)
        if response.status_code != 200:
            LOG.error("Failed to get catalog ID: %s", response.text)
            raise RuntimeError("Failed to get catalog ID")
        
        catalogs = response.json().get('contains', [])
        for catalog in catalogs:
            if catalog['subscriptionType'] == 'scheduled':
                return catalog['identifier']
        raise RuntimeError('Scheduled catalog not found')
    
    def list_responses(self, request_name):
        catalog_id = self.get_catalog_id()
        responses_url = urljoin(self.host, f'/eap/catalogs/{catalog_id}/content/responses/')
        params = {'prefix': request_name}
        response = self.session.get(responses_url, params=params)
        if response.status_code != 200:
            LOG.error("Failed to list responses: %s", response.text)
            raise RuntimeError("Failed to list responses")
        return response.json()

    def poll_for_response(self, request_id, request_name):
        reply_timeout_minutes = 45
        reply_timeout = datetime.timedelta(minutes=reply_timeout_minutes)
        expiration_timestamp = datetime.datetime.now(tz=datetime.timezone.utc) + reply_timeout        
        while datetime.datetime.now(tz=datetime.timezone.utc) < expiration_timestamp:
            content_responses = self.list_responses(request_name)
            for output in content_responses.get('contains', []):
                if output['metadata']['DL_REQUEST_ID'] == request_id:
                    LOG.info('Response is ready')
                    return output['key']
            time.sleep(10)
        raise RuntimeError(f"Response not received within {reply_timeout_minutes} minutes")
    
    def download_response(self, request_id, request_name):
        """
        Download the response for a given request_name and request_id.
        """
        output_key = self.poll_for_response(request_id, request_name)
        data = self.download_data(output_key)
        return data

    def download_data(self, output_key):
        catalog_id = self.get_catalog_id()
        file_url = urljoin(self.host, f'/eap/catalogs/{catalog_id}/content/responses/{output_key}')
        response = self.session.get(file_url, stream=True)
        if response.status_code != 200:
            LOG.error("Failed to download file: %s", response.text)
            raise RuntimeError(f"Failed to download file")
        
        data = response.content
        return data
    
    def validate_period(self, period):
        valid_periods = ["daily", "weekly", "monthly", "quarterly", "yearly"]
        if period not in valid_periods:
            raise ValueError(f"Invalid period: {period}. Must be one of {valid_periods}.")

    def validate_currency(self, currency):
        if not isinstance(currency, str) or len(currency) != 3 or not currency.isupper():
            raise ValueError("Invalid currency. Must be a 3-character uppercase string.")

    def validate_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Must be in YYYY-MM-DD format.")

    def bdh(self, tickers, flds, end_date, start_date='1900-01-01', period='daily', currency='BRL'):

        self.validate_period(period)
        self.validate_currency(currency)
        self.validate_date(start_date)
        self.validate_date(end_date)

        catalog_id = self.get_catalog_id()
        account_url = urljoin(self.host, f'/eap/catalogs/{catalog_id}/requests/')
        request_date = datetime.datetime.now().strftime('%Y%m%d')
        request_name = "BDLH"+request_date
        request_payload = {
            '@type': 'HistoryRequest',
            'name': request_name,
            'description': 'Historical data request',
            'universe': {
                '@type': 'Universe',
                'contains': [{'@type': 'Identifier', 'identifierType': 'TICKER', 'identifierValue': ticker} for ticker in tickers]
            },
            'fieldList': {
                '@type': 'HistoryFieldList',
                'contains': [{'mnemonic': field} for field in flds]
            },
            'trigger': {'@type': 'SubmitTrigger'},
            'runtimeOptions': {
                '@type': 'HistoryRuntimeOptions',
                'dateRange': {'@type': 'IntervalDateRange', 'startDate': start_date, 'endDate': end_date},
                'period': period,
                'historyPriceCurrency': currency
            },
            'formatting': {'@type': 'MediaType', 'outputMediaType': 'application/json'}
        }
        response = self.session.post(account_url, json=request_payload)
        if response.status_code != 201:
            LOG.error("Failed to submit request: %s", response.text)
            raise RuntimeError("Failed to submit request")
        request_id = response.json()['request']['identifier']
        LOG.info("Request ID: %s", request_id)
        data = self.download_response(request_id, request_name)
        return data