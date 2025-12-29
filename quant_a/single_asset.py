import sys
sys.path.append('..')

from utils.data_fetcher import get_current_price, get_historical_data
from utils.metrics import calculate_sharpe_ratio, calculate_max_drawdown
from quant_a.strategies import buy_and_hold, momentum_strategy


def analyze_single_asset(symbol, strategy_type='buy_and_hold', window=20):
    current_price = get_current_price(symbol)
    historical_data = get_historical_data(symbol)
    
    if historical_data is None or current_price is None:
        return None
    
    prices = historical_data['close']
    
    if strategy_type == 'buy_and_hold':
        strategy_values = buy_and_hold(prices)
    elif strategy_type == 'momentum':
        strategy_values = momentum_strategy(prices, window)
    else:
        strategy_values = buy_and_hold(prices)
    
    strategy_returns = strategy_values.pct_change().dropna()
    sharpe = calculate_sharpe_ratio(strategy_returns)
    max_dd = calculate_max_drawdown(strategy_values)
    
    results = {
        'current_price': current_price,
        'prices': prices,
        'strategy_values': strategy_values,
        'sharpe_ratio': sharpe,
        'max_drawdown': max_dd
    }
    
    return results