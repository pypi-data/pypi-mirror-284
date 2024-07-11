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
    username='username',
    password='password',
)

df = client.FiinData(
    sticker="HPG", 
    from_date='2024-06-09 09:15', 
    to_date='2024-07-11 14:29', 
    multiplier=1, 
    timespan='day', 
    limit=100000).toDataFrame()

fi = client.FiinIndicator(df)
df['EMA_5'] = fi.ema(window=5)
df['SMA_5'] = fi.sma(window=5)
df['RSI'] = fi.rsi()

print(df)

```