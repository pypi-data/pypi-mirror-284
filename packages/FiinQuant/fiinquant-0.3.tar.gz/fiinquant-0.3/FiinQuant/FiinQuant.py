from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np
import requests
from signalrcore.hub_connection_builder import HubConnectionBuilder

TOKEN_URL = "http://42.112.22.11:9900/connect/token"
HISTORICAL_API = "https://fiinquant-staging.fiintrade.vn/TradingView/GetStockChartData"
REALTIME_API = "https://fiinquant-realtime-staging.fiintrade.vn/RealtimeHub?access_token="
USERNAME_API = 'fiinquant.staging@fiingroup.vn'
PASSWORD_API = 'sdksoiILelrbJ909)_)aOKknn456'

GRANT_TYPE='password'
CLIENT_ID='FiinTrade.Customer.Client'
CLIENT_SECRET='fiintrade-Cus2023'
SCOPE='openid fiintrade.customer'
USERNAME=''
PASSWORD=''

class FiinSession:
    def __init__(self, username, password):

        """
        Initialize a session for fetching financial data.

        Parameters:
        username (str): The username for authentication.
        password (str): The password for authentication.
        """

        self.username = username
        self.password = password
        self.access_token = None
        self.expired_token = None
        self.urlGetToken = TOKEN_URL
        self.bodyGetToken = {
            'grant_type': GRANT_TYPE,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'scope': SCOPE,
            'username': USERNAME,
            'password': PASSWORD
        }

    def login(self):
        self.bodyGetToken['username'] = self.username
        self.bodyGetToken['password'] = self.password

        try:
            response = requests.post(self.urlGetToken, data=self.bodyGetToken)
            if response.status_code == 200:
                res = response.json()
                self.access_token = res['access_token']
                self.expired_token = res['expires_in'] + int(time.time())
                self.is_login = True
            else:
                self.is_login = False
        except:
            self.is_login = False
        
    def is_expired_token(self): # expired => True, still valid => False
        expires_in = self.expired_token
        current_time = int(time.time())

        try: # login
            if expires_in < current_time: # expired 
                self.is_login = False
                return True       
            else: 
                self.is_login = True
                return False
        except:
            self.is_login = False
            return True
    
    def get_access_token(self):
        if self.is_expired_token():
            self.login()
        return self.access_token
    
    def FiinDataHistorical(self, 
                 ticker: str, 
                 from_date: datetime, 
                 to_date: datetime, 
                 multiplier: int = 1, 
                 timespan: str = 'minute', 
                 limit: int = 1000):
        
        """
        Fetch financial data for a given ticker symbol within a specified date range.

        Parameters:
        ticker (str): The ticker symbol of the financial instrument.
        from_date (datetime): The start time of the data fetching period. format 'YYYY-MM-DD hh:mm:ss'
        to_date (datetime): The end time of the data fetching period. format 'YYYY-MM-DD hh:mm:ss'
        multiplier (int): The time period multiplier (e.g., 1 means 1 minute, 2 means 2 minutes). Default is 1.
        timespan (str): The granularity of the data ('minute', 'hour', 'day'). Default is 'minute'.
        limit (int): The maximum number of data points to fetch. Default is 1000.
        """

        access_token = self.get_access_token()    
        return FiinDataHistorical(access_token, ticker, from_date, to_date, multiplier, timespan, limit)

    def FiinIndicator(self, df: pd.DataFrame):

        """
        Initialize the FiinIndicator function with a DataFrame containing stock data.

        Parameters:
        df (pd.DataFrame): A DataFrame containing stock data. 
        It should have columns such as 'Timestamp', 'Open', 'Low', 'High', 'Low' and 'volume'.
        """

        return FiinIndicator(df)
    
    def FiinDataRealtime(self, ticker: str, callback: None):
        access_token = self.get_access_token() 
        return FiinDataRealtime(access_token, ticker, callback)

class FiinDataHistorical:
    def __init__(self,
                 access_token: str,
                 ticker: str, 
                 from_date, 
                 to_date, 
                 multiplier: int = 1, 
                 timespan: str = 'minute', 
                 limit: int = 1000):
        
        self.ticker = ticker
        self.from_date = from_date
        self.to_date = to_date
        self.multiplier = multiplier
        self.timespan = timespan
        self.limit = limit
        self.access_token = access_token
        self.urlGetDataStock = HISTORICAL_API

    def fetch_historical_data(self):

        # parameters for API
        param = {
            'Code' : self.ticker, 
            'Type' : 'stock', # Stock, Index, CoveredWarrant, Derivative
            'Frequency' : 'EachMinute', # EachMinute, EachOneHour, Daily
            'From' : self.from_date,
            'To' : self.to_date,
            'PageSize' : self.limit
        }
        bearer_token = self.access_token
        header = {'Authorization': f'Bearer {bearer_token}'}
        response = requests.get(url=self.urlGetDataStock, params=param, headers=header)

        if response.status_code == 200:
            res = response.json()
            df = pd.DataFrame(res['items'])
            return df
        
    def preprocess_data(self):
        self.df = self.df.drop(columns=['rateAdjusted', 'openInterest'])
        self.df = self.df.rename(columns={
            "tradingDate": "Timestamp", 
            "openPrice": "Open", 
            "lowestPrice": "Low", 
            "highestPrice": "High", 
            "closePrice": "Close", 
            "totalMatchVolume": "Volume", 
        })
        self.df[['Open', 'Low', 'High', 'Close']] /= 1000
        self.df['Volume'] = self.df['Volume'].astype(int)
        self.df = self.df[['Timestamp', 'Open', 'Low', 'High', 'Close', 'Volume']]
        return self.df
    
    def round_time(self, dt, start_time):
        if self.timespan == 'minute':
            interval = self.multiplier
        if self.timespan == 'hour':
            interval = self.multiplier * 60
        if self.timespan == 'day':
            interval = self.multiplier * 60 * 24

        time_diff = (dt - start_time).total_seconds() / 60
        rounded_minutes = round(time_diff / interval) * interval
        rounded_time = start_time + timedelta(minutes=rounded_minutes)
        return rounded_time
    
    def group_by_data(self):
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        if self.timespan == 'minute':
            start_time = datetime.combine(datetime.today(), datetime.strptime("09:15", "%H:%M").time())
            self.df['Timestamp'] = self.df['Timestamp'].apply(lambda x: self.round_time(x, start_time)).dt.strftime('%Y-%m-%d %H:%M')
        if self.timespan == 'hour':
            start_time = datetime.combine(datetime.today(), datetime.strptime("09:00", "%H:%M").time())
            self.df['Timestamp'] = self.df['Timestamp'].apply(lambda x: self.round_time(x, start_time)).dt.strftime('%Y-%m-%d %H:00')
        if self.timespan == 'day':
            start_time = datetime.combine(datetime.today(), datetime.strptime("09:15", "%H:%M").time())
            self.df['Timestamp'] = self.df['Timestamp'].apply(lambda x: self.round_time(x, start_time)).dt.strftime('%Y-%m-%d 00:00')

        self.df = self.df.groupby('Timestamp').agg({
            'Open': 'first',
            'Low': 'min',
            'High': 'max',
            'Close': 'last',
            'Volume': 'sum'
        }).reset_index()

        return self.df

    def toDataFrame(self):
        self.df = self.fetch_historical_data()
        self.df = self.preprocess_data()
        self.df = self.group_by_data()
        return self.df

class FiinIndicator:
    def __init__(self, df: pd.DataFrame):

        """
        Initialize the FiinIndicator class with a DataFrame containing stock data.

        Parameters:
        df (pd.DataFrame): A DataFrame containing stock data. 
        It should have columns such as 'Timestamp', 'Open', 'Low', 'High', 'Low' and 'volume'.
        """

        self.df = df
        self.open = df['Open']
        self.low = df['Low']
        self.high = df['High']
        self.close = df['Close']
        self.volume = df['Volume']

    def ema(self, window: int, col: pd.Series = None):

        """
        Calculate the Exponential Moving Average (EMA) of a data series.

        Parameters:
        window (int): Number of observations to use for calculating EMA.
        col (pd.Series, optional): Input data series. Defaults to the 'close' column of the current object.

        Returns:
        pd.Series: Calculated EMA data series.
        """

        if col is None:
            col = self.close
        ema = col.ewm(span=window, min_periods=window, adjust=False).mean()
        return ema
            
    def sma(self, window: int, col: pd.Series = None):

        """
        Calculate the Simple Moving Average (SMA) of a data series.

        Parameters:
        window (int): Number of observations to use for calculating SMA.
        col (pd.Series, optional): Input data series. Defaults to the 'close' column of the current object.

        Returns:
        - pd.Series: Calculated SMA data series.
        """

        if col is None:
            col = self.close
        sma = col.rolling(window=window, min_periods=window).mean()
        return sma
    
    def rsi(self, window: int = 14):

        """
        Calculate the Relative Strength Index (RSI) of a data series.

        Parameters:
        window (int): Number of observations to use for calculating RSI. Default is 14

        Returns:
        pd.Series: Calculated RSI values.
        """

        delta = self.close.diff() 
        gain = delta.where(delta > 0, 0) 
        loss = -delta.where(delta < 0, 0) 
        avg_gain = gain.ewm(com=window - 1, min_periods=window, adjust=False).mean() 
        avg_loss = loss.ewm(com=window - 1, min_periods=window, adjust=False).mean() 
        rs = avg_gain / avg_loss.abs() 
        rsi = 100 - (100 / (1 + rs)) 
        rsi[(avg_loss == 0) | (avg_loss == -avg_gain)] = 100  
        return rsi
    
    def macd(self, window_slow: int = 26, window_fast: int = 12):

        """
        Calculate the Moving Average Convergence Divergence (MACD) of a data series.

        Parameters:
        window_slow (int): Number of observations for the slow EMA in MACD calculation. Default is 26
        window_fast (int): Number of observations for the fast EMA in MACD calculation. Default is 12

        Returns:
        pd.Series: Calculated MACD values.
        """
         
        ema_fast = self.ema(window_fast)
        ema_slow = self.ema(window_slow)
        macd_line = ema_fast - ema_slow
        return macd_line

    def macd_signal(self, window_sign: int = 9):

        """
        Calculate the signal line (SIGNAL) for the MACD of a data series.

        Parameters:
        window_sign (int): Number of observations for the signal line calculation. Default is 9

        Returns:
        pd.Series: Calculated MACD signal line values.
        """

        macd_signal_line = self.macd().ewm(span=window_sign, min_periods=window_sign, adjust=False).mean()
        return macd_signal_line

    def macd_diff(self, window_slow: int = 26, window_fast: int = 12, window_sign: int = 9):
        
        """
        Calculate the MACD Histogram (MACD Diff) of a data series.

        Parameters:
        window_slow (int): Number of observations for the slow EMA in MACD calculation. Default is 26
        window_fast (int): Number of observations for the fast EMA in MACD calculation. Default is 12
        window_sign (int): Number of observations for the signal line calculation. Default is 9

        Returns:
        pd.Series: Calculated MACD Histogram (MACD Diff) values.
        """
        
        macd_diff_line = self.macd(window_slow, window_fast) - self.macd_signal(window_sign)
        return macd_diff_line

    def bollinger_mavg(self, window: int = 20):

        """
        Calculate the Bollinger Bands - Middle Band (MAVG) of a data series.

        Parameters:
        window (int): Number of observations for calculating the moving average. Default is 20

        Returns:
        pd.Series: Calculated Bollinger Bands - Middle Band values.
        """

        bollinger_mavg = self.sma(window)
        return bollinger_mavg

    def bollinger_std(self, window: int = 20):

        """
        Calculate the standard deviation of the Bollinger Bands (STD) of a data series.

        Parameters:
        window (int): Number of observations for calculating the standard deviation. Default is 20

        Returns:
        pd.Series: Calculated Bollinger Bands - Standard Deviation values.
        """

        try:
            rolling_windows = np.lib.stride_tricks.sliding_window_view(self.close, window)
            stds = np.std(rolling_windows, axis=1)
            stds = np.concatenate([np.full(window - 1, np.nan), stds])
            std = pd.Series(stds, index=self.close.index)
            return std
        except:
            std = pd.Series([np.nan] * self.close.shape[0])
            return std

    def bollinger_hband(self, window: int = 20, window_dev = 2):
        
        """
        Calculate the upper band of the Bollinger Bands (HBAND) of a data series.

        Parameters:
        - window (int): Number of observations for calculating the moving average. Default is 20
        - window_dev (int): Number of standard deviations for calculating the upper band. Default is 2

        Returns:
        - pd.Series: Calculated Bollinger Bands - Upper Band values.
        """

        bollinger_hband = self.sma(window) + (window_dev * self.bollinger_std(window))
        return bollinger_hband

    def bollinger_lband(self, window: int = 20, window_dev = 2):

        """
        Calculate the lower band of the Bollinger Bands (LBAND) of a data series.

        Parameters:
        window (int): Number of observations for calculating the moving average. Default is 20
        window_dev (int): Number of standard deviations for calculating the lower band. Default is 2

        Returns:
        pd.Series: Calculated Bollinger Bands - Lower Band values.
        """

        bollinger_lband = self.sma(window) - (window_dev * self.bollinger_std(window))
        return bollinger_lband
    
    def stoch(self, window: int = 14):

        """
        Calculate the Stochastic Oscillator (STOCH) of a data series.

        Parameters:
        window (int): Number of observations for calculating the Stochastic Oscillator. Default is 14

        Returns:
        pd.Series: Calculated Stochastic Oscillator values.
        """
        lowest_low = self.low.rolling(window=window).min()
        highest_high = self.high.rolling(window=window).max()
        stoch_k = 100 * (self.close - lowest_low) / (highest_high - lowest_low)
        return stoch_k

    def stoch_signal(self, window: int = 14, smooth_window: int = 3):

        """
        Calculate the signal line (SIGNAL) for the Stochastic Oscillator (STOCH) of a data series.

        Parameters:
        window (int): Number of observations for calculating the Stochastic Oscillator. Default is 14
        smooth_window (int): Number of observations for smoothing the signal line. Default is 3

        Returns:
        pd.Series: Calculated Stochastic Oscillator signal line values.
        """

        stoch_d = self.sma(window=smooth_window, col=self.stoch(window))
        return stoch_d
    
class FiinDataRealtime:
    def __init__(self,ticker=None,callback=None,access_token = None):
        self.object = FiinSession(USERNAME,PASSWORD)
        URL = REALTIME_API
        self.url = URL
        self.hub_connection = self._build_connection()
        self.connected = False 
        self.callback = callback
        self.access_token = access_token
        self.df = pd.DataFrame(columns=[
            'TotalMatchVolume', 'MarketStatus', 'TradingDate', 'MatchType', 'ComGroupCode',
            'OrganCode', 'Ticker', 'ReferencePrice', 'OpenPrice', 'ClosePrice', 'CeilingPrice',
            'FloorPrice', 'HighestPrice', 'LowestPrice', 'MatchPrice', 'PriceChange',
            'PercentPriceChange', 'MatchVolume', 'MatchValue', 'TotalMatchValue',
            'TotalBuyTradeVolume', 'TotalSellTradeVolume', 'DealPrice', 'TotalDealVolume',
            'TotalDealValue', 'ForeignBuyVolumeTotal', 'ForeignBuyValueTotal',
            'ForeignSellVolumeTotal', 'ForeignSellValueTotal', 'ForeignTotalRoom',
            'ForeignCurrentRoom'
        ])
        self.ticker = ticker
    def data_handler(self, message):
        if message is not None:
            self.df.loc[len(self.df)] = message[0]['data'][0].split('|') 
            if self.callback:
                self.callback(self.df[-1:])

    def _build_connection(self):
        return HubConnectionBuilder()\
            .with_url(self.url, options={
                "access_token_factory": lambda: self.access_token
            })\
            .with_automatic_reconnect({
                "type": "raw",
                "keep_alive_interval": 1,
                "reconnect_interval": [1, 3, 5, 7, 11]
            }).build()

    def receive_message(self, message):
        self.data_handler(message)

    def handle_error(self, error):
        print(f"Error: {error}")
    def on_connect(self):
        self.connected = True
        print("Connection established")
        self.join_groups()

    def on_disconnect(self):
        self.connected = False
        print("Disconnected from the hub")

    def join_groups(self):
        if self.connected:
            self.hub_connection.send("JoinGroup", [f"Realtime.Ticker.{self.ticker}"])
            print(f"Joined group: Realtime.Ticker.{self.ticker}")
        else:
            print("Cannot join groups, not connected")

    def start(self):
        if self.hub_connection.transport is not None:
            print("Already connected, stopping existing connection before starting a new one.")
            self.hub_connection.stop()

        self.hub_connection.on("ReceiveMessage", self.receive_message)
        self.hub_connection.on_close(self.handle_error)
        self.hub_connection.on_open(self.on_connect)
        self.hub_connection.on_close(self.on_disconnect)
        self.hub_connection.start()
        
        while True:
           time.sleep(1)

    def stop(self):
        if self.connected:
            print("Disconnecting...")
            self.hub_connection.stop()
        
