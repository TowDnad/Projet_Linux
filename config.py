import os

# Data refresh settings
REFRESH_INTERVAL = 300  # 5 minutes in seconds

# Assets configuration
SINGLE_ASSET = "AAPL.US"
PORTFOLIO_ASSETS = ["AAPL.US", "MSFT.US", "GOOGL.US"]

# Cron job settings
DAILY_REPORT_TIME = '20:00'  # 8pm
REPORTS_DIR = 'data/daily_reports'

# Flask settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
DEBUG = False