# BDL

A Python client for Bloomberg Data License API.

## Installation

pip install bdl

## Usage

```python
from bdl import BDL

client_id = 'your_client_id'
client_secret = 'your_client_secret'

bloomberg = BDL(client_id=client_id, client_secret=client_secret)
data = bloomberg.bdh(
    tickers=['AAPL US Equity'],
    flds=['PX_LAST'],
    start_date='2023-01-01',
    end_date='2023-12-31'
)

print(data)