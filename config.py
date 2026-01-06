import os

# Data refresh settings
REFRESH_INTERVAL = 300  # 5 minutes in seconds

# Assets configuration (for fallback api)
SINGLE_ASSET = "AAPL"
PORTFOLIO_ASSETS = ["AAPL", "MSFT", "GOOGL"]

# Cron job settings
DAILY_REPORT_TIME = '20:00'  # 8pm
REPORTS_DIR = 'data/daily_reports'

# Flask settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 80
DEBUG = False

# available assets for selection
AVAILABLE_ASSETS = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "GOOGL": "Alphabet (Google)",
    "AMZN": "Amazon",
    "META": "Meta Platforms",
    "NVDA": "NVIDIA",
    "TSLA": "Tesla",
    "BRK-B": "Berkshire Hathaway",
    "JPM": "JPMorgan Chase",
    "JNJ": "Johnson & Johnson",
    "V": "Visa",
    "MA": "Mastercard",
    "PG": "Procter & Gamble",
    "UNH": "UnitedHealth Group",
    "HD": "Home Depot",
    "DIS": "Walt Disney",
    "BAC": "Bank of America",
    "KO": "Coca-Cola",
    "PEP": "PepsiCo",
    "XOM": "Exxon Mobil"
}




