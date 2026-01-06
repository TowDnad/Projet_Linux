import pandas as pd 
import numpy as np
from utils.data_fetcher import get_current_price, get_historical_data
from utils.metrics import calculate_sharpe_ratio, calculate_max_drawdown, calculate_volatility, calculate_correlation_matrix

# Function to get portfolio data
def get_portfolio_data(symbols, years):
    current_prices = {}
    historical_data = {}

    for symbol in symbols:
        price = get_current_price(symbol)
        hist = get_historical_data(symbol, years)

        if price is not None:
            current_prices[symbol] = price

        if hist is not None:
            historical_data[symbol] = hist["close"]

    return current_prices, historical_data

# Function to calculate portfolio value
def calculate_portfolio_value(historical_data, weights, initial_capital=10000):
    df = pd.DataFrame(historical_data).dropna()

    normalized_prices = df / df.iloc[0]
    weighted_prices = normalized_prices.mul(weights, axis=1)

    portfolio_value = initial_capital * weighted_prices.sum(axis=1)

    return portfolio_value

# Function to calculate portfolio value with rebalancing
def calculate_portfolio_value_rebalanced(
    historical_data,
    weights,
    initial_capital=10000,
    rebalance_freq="M"  # "M" monthly, "Q" quarterly, "A" yearly
):
    """
    Portfolio value with periodic rebalancing.
    """
    prices = pd.DataFrame(historical_data).dropna()

    returns = prices.pct_change().dropna()
    portfolio_value = pd.Series(index=returns.index, dtype=float)

    current_weights = np.array(weights, dtype=float)
    portfolio_value.iloc[0] = initial_capital

    last_rebalance_date = returns.index[0]

    for t in range(1, len(returns)):
        date = returns.index[t]

        # Apply returns
        portfolio_value.iloc[t] = portfolio_value.iloc[t - 1] * (
            1 + np.dot(current_weights, returns.iloc[t])
        )

        # Rebalance condition
        if date.to_period(rebalance_freq) != last_rebalance_date.to_period(rebalance_freq):
            current_weights = np.array(weights, dtype=float)
            last_rebalance_date = date

    return portfolio_value


# Main function to analyze portfolio
def analyze_portfolio(symbols, weights=None, years=5, rebalance_freq=None):
    if weights is None:
        weights = np.ones(len(symbols)) / len(symbols)
    else:
        weights = np.array(weights, dtype=float)
        weights = weights / weights.sum()

    current_prices, historical_data = get_portfolio_data(symbols, years)
    
    if not historical_data:
        return None

    if rebalance_freq:
        portfolio_value = calculate_portfolio_value_rebalanced(
            historical_data,
            weights,
            rebalance_freq=rebalance_freq
        )
    else:
        portfolio_value = calculate_portfolio_value(
            historical_data,
            weights
        )


    n_observations = len(portfolio_value)
    
    portfolio_returns = portfolio_value.pct_change().dropna()

    results = {
        "current_prices": current_prices,
        "historical_data": historical_data,
        "portfolio_value": portfolio_value,
        "sharpe_ratio": calculate_sharpe_ratio(portfolio_returns),
        "max_drawdown": calculate_max_drawdown(portfolio_value),
        "volatility": calculate_volatility(portfolio_returns),
        "correlation_matrix": calculate_correlation_matrix(historical_data),
        "weights": weights,
        "n_observations": n_observations
    }

    return results