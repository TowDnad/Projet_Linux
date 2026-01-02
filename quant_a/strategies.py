import pandas as pd
import numpy as np

def buy_and_hold(prices, initial_capital=10000):
    shares = initial_capital / prices.iloc[0]
    portfolio_value = shares * prices
    return portfolio_value


def momentum_strategy(prices, window=20, initial_capital=10000):
    returns = prices.pct_change()
    momentum = returns.rolling(window=window).mean()
    
    position = np.where(momentum > 0, 1, 0)
    position = pd.Series(position, index=prices.index)
    
    strategy_returns = position.shift(1) * returns
    strategy_returns.fillna(0, inplace=True)
    
    portfolio_value = initial_capital * (1 + strategy_returns).cumprod()
    return portfolio_value