from flask import Flask, render_template, jsonify, request
import plotly.graph_objs as go
import plotly.utils
import json
import config as config

from quant_a.single_asset import analyze_single_asset
from quant_b.portfolio import analyze_portfolio

app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return render_template("index.html")

# API Endpoints
@app.route("/api/assets")
def get_assets():
    return jsonify(config.AVAILABLE_ASSETS)

# Single Asset Analysis Endpoint
@app.route("/api/single-asset")
def get_single_asset():
    symbol = request.args.get("symbol", config.SINGLE_ASSET)
    strategy = request.args.get("strategy", "buy_and_hold")
    window = int(request.args.get("window", 20))

    years = int(request.args.get("years", 5))
    results = analyze_single_asset(symbol, strategy, window, years)

    if results is None:
        return jsonify({"error": "Failed to fetch data"}), 500

    # Normalisation on base 100
    prices_norm = results["prices"] / results["prices"].iloc[0] * 100
    strategy_norm = results["strategy_values"] / results["strategy_values"].iloc[0] * 100

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=prices_norm.index,
        y=prices_norm.values,
        mode="lines",
        name="Asset Price (Base 100)",
        line=dict(color="blue")
    ))

    fig.add_trace(go.Scatter(
        x=strategy_norm.index,
        y=strategy_norm.values,
        mode="lines",
        name="Strategy Value (Base 100)",
        line=dict(color="green")
    ))

    fig.update_layout(
        title=f"{symbol} – {strategy.replace('_', ' ').title()} Strategy ({years}Y Backtest)",
        xaxis_title="Date",
        yaxis_title="Indexed Value (Base 100)",
        hovermode="x unified"
    )


    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    response_data = {
        "current_price": float(results["current_price"]),
        "sharpe_ratio": float(results["sharpe_ratio"]),
        "max_drawdown": float(results["max_drawdown"]),
        "n_observations": results["n_observations"],
        "n_trades": results["n_trades"],
        "graph": graph_json
    }


    return jsonify(response_data)

# Portfolio Analysis Endpoint
@app.route("/api/portfolio")
def get_portfolio():
    symbols = request.args.getlist("symbols")
    if not symbols:
        symbols = config.PORTFOLIO_ASSETS

    weights_str = request.args.getlist("weights")
    if weights_str and len(weights_str) == len(symbols):
        weights = [float(w) for w in weights_str]
    else:
        weights = None

    rebalance_freq = request.args.get("rebalance", None)
    
    years = int(request.args.get("years", 5))
    results = analyze_portfolio(symbols, weights, years, rebalance_freq)

    if results is None:
        return jsonify({"error": "Failed to fetch data"}), 500

    fig = go.Figure()

    # Normalisation on base 100 for each asset
    for symbol, prices in results["historical_data"].items():
        prices_norm = prices / prices.iloc[0] * 100

        fig.add_trace(go.Scatter(
            x=prices_norm.index,
            y=prices_norm.values,
            mode="lines",
            name=f"{symbol} (Base 100)",
            line=dict(width=1.5)
        ))

    # Normalisation on base 100 for the whole portfolio
    portfolio_norm = (
        results["portfolio_value"] / results["portfolio_value"].iloc[0] * 100
    )

    fig.add_trace(go.Scatter(
        x=portfolio_norm.index,
        y=portfolio_norm.values,
        mode="lines",
        name="Portfolio (Base 100)",
        line=dict(color="black", width=3)
    ))

    fig.update_layout(
        title=f"Portfolio Analysis ({years}Y Backtest, Base 100)",
        xaxis_title="Date",
        yaxis_title="Indexed Value (Base 100)",
        hovermode="x unified"
    )


    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    response_data = {
        "current_prices": results["current_prices"],
        "sharpe_ratio": float(results["sharpe_ratio"]),
        "max_drawdown": float(results["max_drawdown"]),
        "volatility": float(results["volatility"]),
        "n_observations": results["n_observations"],
        "graph": graph_json
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=config.DEBUG
    )
