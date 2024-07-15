# quant_indicators

Python package for financial technical indicators.

## Installation

You can install the package via pip:

```python
pip install FiinQuant
```

## Usage

```python
from FiinQuant import FiinSession

client = FiinSession(
    username='fiinquant.staging@fiingroup.vn',
    password='sdksoiILelrbJ909)_)aOKknn456',
)

df = client.FiinDataHistorical(
    ticker="HPG", 
    from_date='2024-06-09 09:15', 
    to_date='2024-07-15 14:29', 
    multiplier=1, 
    timespan='minute',  
    limit=10000).toDataFrame()

fi = client.FiinIndicator(df)
df['EMA_5'] = fi.ema(window=5)
print(df)

```