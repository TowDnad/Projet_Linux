import pandas as pd 
from utils.data_fetcher import get_current_price, get_historical_data
from utils.metrics import calculate_sharpe_ratio, calculate_max_drawdown, calculate_volatility, calculate_correlation_matrix

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

# Function to calculate portfolio value
def calculate_portfolio_value(historical_data, weights, initial_capital=10000):
    df = pd.DataFrame(historical_data).dropna()
    
    normalized_prices = df / df.iloc[0]
    weighted_prices = normalized_prices.mul(weights, axis=1)
    
    portfolio_value = initial_capital * weighted_prices.sum(axis=1)
    
    return portfolio_value

# Main function to analyze portfolio
def analyze_portfolio(symbols, weights=None):
    if weights is None:
        weights = [1.0 / len(symbols)] * len(symbols)

    current_prices, historical_data = get_portfolio_data(symbols)

    if not historical_data:
        return None

    portfolio_value = calculate_portfolio_value(
        historical_data, weights
    )

    portfolio_returns = portfolio_value.pct_change().dropna()

    results = {
        "current_prices": current_prices,
        "historical_data": historical_data,
        "portfolio_value": portfolio_value,
        "sharpe_ratio": calculate_sharpe_ratio(portfolio_returns),
        "max_drawdown": calculate_max_drawdown(portfolio_value),
        "volatility": calculate_volatility(portfolio_returns),
        "correlation_matrix": calculate_correlation_matrix(historical_data),
        "weights": weights
    }

    return results