import pandas as pd 
from utils.data_fetcher import get_current_price, get_historical_data
from utils.metrics import calculate_sharpe_ratio, caculate_max_drawdown, calculate_volatility, calculate_correlation_matrix

# Function to get portfolio data
def get_portfolio_data(symbols):
    current_prices = {}
    historical_data = {}
    
    for symbol in symbols:
        price = get_current_price(symbol)
        hist = get_historical_data(symbol)
        
        if price is not None:
            current_prices[symbol] = price
        if hist is not None:
            historical_data[symbol] = hist
            
    return current_prices, historical_data
