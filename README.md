# Financial Asset Analysis and Portfolio Backtester

This project is a Python-based financial analysis tool consisting of a Flask web application and an automated reporting system. It allows users to perform backtesting on single assets using different strategies (Buy & Hold, Momentum) and analyze the performance of weighted portfolios.
You can access the App on the following IP : http://13.61.190.129 

## Features

* **Web Dashboard**: A Flask-based interface to visualize asset performance and portfolio metrics interactively.
* **Single Asset Analysis**: Compare "Buy and Hold" strategies against "Momentum" trading strategies with customizable time windows.
* **Portfolio Backtesting**: Analyze multi-asset portfolios with custom weights, calculating aggregate performance over up to 5 years.
* **Key Financial Metrics**: Automatically calculates Sharpe Ratio, Maximum Drawdown, Volatility, and Correlation Matrices.
* **Automated Reporting**: A script to generate daily text-based summaries of asset and portfolio performance.
* **Cron Integration**: Shell script setup to automate the daily report generation at a specific time (default 20:00).

## Project Structure

The project is organized into the following modules based on the application logic:

* **app.py**: Main Flask application entry point.
* **config.py**: Configuration settings for assets, network ports, and file paths.
* **requirements.txt**: List of Python dependencies.
* **cron_setup.sh**: Shell script to initiate the automated cron job.
* **utils/**:
    * **data_fetcher.py**: Handles data retrieval from Stooq via pandas_datareader.
    * **metrics.py**: Contains mathematical functions for financial metrics (Sharpe ratio, volatility, etc.).
* **quant_a/**:
    * **single_asset.py**: Logic for analyzing individual asset strategies.
    * **strategies.py**: Implementation of Buy & Hold and Momentum strategies.
* **quant_b/**:
    * **portfolio.py**: Logic for calculating portfolio value and weighted returns.
* **scripts/**:
    * **daily_report.py**: Script generates a text report saved to the reports directory.

## Prerequisites

* Python 3.8+
* Virtual Environment 
* Internet connection for fetching market data

## Local Installation

1.  **Clone the repository and navigate to the project folder.**

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Dependencies include Flask, yfinance, pandas, numpy, matplotlib, plotly, and pandas-datareader.*

## Usage

### Web Application

The web application provides a visual interface for the analysis tools.

1.  **Start the server:**
    ```bash
    python app.py
    ```
    *The application is configured to run on host `0.0.0.0` and port `80` by default.*

2.  **Access the dashboard:**
    Open your web browser and navigate to the server's IP address or localhost.

