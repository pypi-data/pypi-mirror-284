from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np
import requests

class FiinSession:
    def __init__(self, username, password, link_access_token, link_api, link_body_access_token):

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
        self.urlGetToken = link_access_token
        self.urlGetDataStock = link_api
        self.bodyGetToken = link_body_access_token
        # self.bodyGetToken = {
        #     'grant_type' : 'password', 
        #     'client_id' : 'FiinTrade.Customer.Client', 
        #     'client_secret' : 'fiintrade-Cus2023', 
        #     'scope' : 'openid fiintrade.customer', 
        #     'username' : None,
        #     'password' : None
        # }

    def login(self):
        self.bodyGetToken['username'] = self.username  # 'fiinquant.staging@fiingroup.vn'
        self.bodyGetToken['password'] = self.password  # 'sdksoiILelrbJ909)_)aOKknn456'

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
        
    def is_expired_token(self): # expired => False, still valid => True
        try:
            expires_in = self.expired_token
            current_time = int(time.time())
            if expires_in < current_time: # expired 
                self.is_login = False
                return False
            else:
                self.is_login = True
                return True
        except:
            self.is_login = False
            return False
    
    def get_access_token(self):
        if not self.is_expired_token():
            self.login()
        return self.access_token
    
    def FiinData(self, 
                 urlGetDataStock: str,
                 sticker: str, 
                 from_date: datetime, 
                 to_date: datetime, 
                 multiplier: int = 1, 
                 timespan: str = 'minute', 
                 limit: int = 1000):
        """
        Fetch financial data for a given sticker symbol within a specified date range.

        Parameters:
        sticker (str): The ticker symbol of the financial instrument.
        from_date (datetime): The start time of the data fetching period. format 'YYYY-MM-DD hh:mm:ss'
        to_date (datetime): The end time of the data fetching period. format 'YYYY-MM-DD hh:mm:ss'
        multiplier (int): The time period multiplier (e.g., 1 means 1 minute, 2 means 2 minutes). Default is 1.
        timespan (str): The granularity of the data ('minute', 'hour', 'day'). Default is 'minute'.
        limit (int): The maximum number of data points to fetch. Default is 1000.
        """


        access_token = self.get_access_token()
        
        return FiinData(access_token, self.urlGetDataStock, sticker, from_date, to_date, multiplier, timespan, limit)

    def FiinIndicator(self, df: pd.DataFrame):
        """
        Initialize the FiinIndicator function with a DataFrame containing stock data.

        Parameters:
        df (pd.DataFrame): A DataFrame containing stock data. 
        It should have columns such as 'Timestamp', 'Open', 'Low', 'High', 'Low' and 'volume'.
        """
        return FiinIndicator(df)

class FiinData:
    def __init__(self,
                 access_token: str,
                 urlGetDataStock: str,
                 sticker: str, 
                 from_date, 
                 to_date, 
                 multiplier: int = 1, 
                 timespan: str = 'minute', 
                 limit: int = 1000,):
        
        self.sticker = sticker
        self.from_date = from_date
        self.to_date = to_date
        self.multiplier = multiplier
        self.timespan = timespan
        self.limit = limit
        self.access_token = access_token
        self.urlGetDataStock = urlGetDataStock
        # self.urlGetDataStock = 'https://fiinquant-staging.fiintrade.vn/TradingView/GetStockChartData'

        self.df = self.fetch_historical_data()
        self.df = self.preprocess_data()
        self.df = self.group_by_data()
        

    def fetch_historical_data(self):
        # parameters for API
        param = {
            'Code' : self.sticker, 
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
        ema = self.close.ewm(span=window, min_periods=window, adjust=False).mean()
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


# client = FiinSession(
#     username='fiinquant.staging@fiingroup.vn',
#     password='sdksoiILelrbJ909)_)aOKknn456'
# )

# df = client.FiinData(
#     sticker="HPG", 
#     from_date='2024-06-09 09:15', 
#     to_date='2024-07-11 14:29', 
#     multiplier=1, 
#     timespan='day', 
#     limit=100000).toDataFrame()

# fi = client.FiinIndicator(df)
# df['EMA_5'] = fi.ema(window=5)
# df['SMA_5'] = fi.sma(window=5)

# ################################################################
# client = FiinSession(
#     username='fiinquant.staging@fiingroup.vn',
#     password='sdksoiILelrbJ909)_)aOKknn456'
# )

# df = FiinData(client, sticker="HPG", 
#               from_date='2024-06-09 09:15', 
#               to_date='2024-07-11 14:29',
#               multiplier=1, 
#               timespan='minute', # day, hour, minute
#               limit=10000).toDataFrame()

# fi = FiinIndicator(df)
# df['EMA_5'] = fi.ema(window=5)
# df['SMA_5'] = fi.sma(window=5)
# df['RSI'] = fi.rsi()
# df['MACD'] = fi.macd()
# print(df)