from flask import Flask, render_template, jsonify, request
import plotly.graph_objs as go
import plotly.utils
import json
import config as config

from quant_a.single_asset import analyze_single_asset
from quant_b.portfolio import analyze_portfolio

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/single-asset")
def get_single_asset():
    symbol = request.args.get("symbol", config.SINGLE_ASSET)
    strategy = request.args.get("strategy", "buy_and_hold")
    window = int(request.args.get("window", 20))

    results = analyze_single_asset(symbol, strategy, window)

    if results is None:
        return jsonify({"error": "Failed to fetch data"}), 500

    # 🔹 Normalisation base 100
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
        title=f"{symbol} – {strategy.replace('_', ' ').title()} Strategy",
        xaxis_title="Date",
        yaxis_title="Indexed Value (Base 100)",
        hovermode="x unified"
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    response_data = {
        "current_price": float(results["current_price"]),
        "sharpe_ratio": float(results["sharpe_ratio"]),
        "max_drawdown": float(results["max_drawdown"]),
        "graph": graph_json
    }

    return jsonify(response_data)
