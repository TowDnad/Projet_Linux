import sys
sys.path.append('..')

import os
from datetime import datetime
import config as config
from quant_a.single_asset import analyze_single_asset
from quant_b.portfolio import analyze_portfolio

def generate_daily_report():
    os.makedirs(config.REPORTS_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_file = os.path.join(config.REPORTS_DIR, f'report_{timestamp}.txt')
    
    with open(report_file, 'w') as f:
        f.write(f"Daily Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*60 + "\n\n")
        
        f.write("SINGLE ASSET ANALYSIS\n")
        f.write("-"*60 + "\n")
        single_results = analyze_single_asset(config.SINGLE_ASSET)
        
        if single_results:
            f.write(f"Symbol: {config.SINGLE_ASSET}\n")
            f.write(f"Current Price: ${single_results['current_price']:.2f}\n")
            f.write(f"Sharpe Ratio: {single_results['sharpe_ratio']:.4f}\n")
            f.write(f"Max Drawdown: {single_results['max_drawdown']:.4f}\n")
            
            prices = single_results['prices']
            f.write(f"Open Price (today): ${prices.iloc[-1]:.2f}\n")
            f.write(f"Close Price (yesterday): ${prices.iloc[-2]:.2f}\n")
            
            daily_volatility = prices.pct_change().std()
            f.write(f"Daily Volatility: {daily_volatility:.4f}\n")
        else:
            f.write("Error fetching single asset data\n")
        
        f.write("\n")
        f.write("PORTFOLIO ANALYSIS\n")
        f.write("-"*60 + "\n")
        portfolio_results = analyze_portfolio(config.PORTFOLIO_ASSETS)
        
        if portfolio_results:
            f.write(f"Assets: {', '.join(config.PORTFOLIO_ASSETS)}\n")
            f.write("Current Prices:\n")
            for symbol, price in portfolio_results['current_prices'].items():
                f.write(f"  {symbol}: ${price:.2f}\n")
            f.write(f"Portfolio Sharpe Ratio: {portfolio_results['sharpe_ratio']:.4f}\n")
            f.write(f"Portfolio Max Drawdown: {portfolio_results['max_drawdown']:.4f}\n")
            f.write(f"Portfolio Volatility: {portfolio_results['volatility']:.4f}\n")
        else:
            f.write("Error fetching portfolio data\n")
    
    print(f"Daily report generated: {report_file}")

if __name__ == '__main__':
    generate_daily_report()