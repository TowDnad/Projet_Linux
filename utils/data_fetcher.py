import pandas_datareader.data as web
from datetime import datetime 

# Function to get the current price of a symbol
def get_current_price(symbol):
    try:
        df = web.DataReader(symbol,'stooq') 
        
        if df.empty:
            return None
        else:
            return float(df["Close"].iloc[0])
        
    except Exception as e:
        print(f"Error fetching current price for {symbol}: {e}")
        return None

# Function to get historical data for a symbol    
def get_historical_data(symbol, days=365):
    try:
        end = datetime.now()
        start = end.replace(year=end.year - 1)
        
        df = web.DataReader(symbol,"stooq", start, end)
        
        if df.empty:
            return None
        
        df = df.sort_index()
        df = df.rename(columns={"Open":"open", "High":"high", "Low":"low", "Close":"close", "Volume":"volume"})
        
        return df[["open", "high", "low", "close", "volume"]]
    
    except Exception as e:
        print(f"Error fetching historical data for {symbol}: {e}")
        return None
        