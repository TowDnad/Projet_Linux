import pandas as pd
import numpy as np

def buy_and_hold(prices, initial_capital=10000):
    shares = initial_capital / prices.iloc[0]
    portfolio_value = shares * prices
    return portfolio_value
