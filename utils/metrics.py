import numpy as np
import pandas as pd

# Function to calculate returns
def calculate_returns(prices):
    returns = prices.pct_change().dropna()
    return returns

# Function to calculate Sharpe Ratio
def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - risk_free_rate / 252
    if excess_returns.std() == 0:
        return 0
    else:
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

# Function to calculate Maximum Drawdown
def calculate_max_drawdown(prices):
    cumulative = (1 + calculate_returns(prices)).cumprod()
    running_max = cumulative.expanding().max()
    drawdown = (cumulative - running_max) / running_max
    return drawdown.min()

# Function to calculate Volatility
def calculate_volatility(returns):
    return returns.std() * np.sqrt(252)

# Function to calculate Correlation Matrix
def calculate_correlation_matrix(data_dict):
    df = pd.DataFrame(data_dict)
    returns = df.pct_change().dropna()
    return returns.corr()