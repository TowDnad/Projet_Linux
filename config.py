import os

# Data refresh settings
REFRESH_INTERVAL = 300  # 5 minutes in seconds

# Assets configuration
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
    "TSLA": "Tesla",
    "NVDA": "NVIDIA"
}

