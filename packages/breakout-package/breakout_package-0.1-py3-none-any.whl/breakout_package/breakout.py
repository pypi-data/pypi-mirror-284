import numpy as np
import pandas as pd

API_TOKEN = "YOUR_SECURE_API_TOKEN"

def authenticate(token):
    if token != API_TOKEN:
        raise PermissionError("Invalid API token")

def breakout(data, target, alpha, can_len=1.03, can_len2=1.05, token=None):
    authenticate(token)
    try:
        data = data.reset_index()
        data["diff"] = data["Close"].diff()
        data["up"] = np.where(data["diff"] > 0, data["diff"], 0)
        data["down"] = np.where(data["diff"] < 0, -data["diff"], 0)
        data["EMAup"] = data["up"].ewm(alpha=alpha, adjust=False).mean()
        data["EMAdown"] = data["down"].ewm(alpha=alpha, adjust=False).mean()
        data["RS"] = data["EMAup"] / data["EMAdown"]
        data["RSI"] = 100 - (100 / (1 + data["RS"]))
    except Exception as e:
        print(f"Error in calculate_rsi1: {e}")
    try:
        data["Trade condition"] = (
            (data["RSI"] > target) &
            (data["RSI"].shift(1) < target) &
            (data["RSI"].shift(2) < target) &
            (data["RSI"].shift(3) < target) &
            (data["RSI"].shift(4) < target) &
            (data["Close"] > data["Open"]*can_len) &
            (data["High"] > data["Low"]*can_len2)
        )
    except Exception as e:
        print(f"Error in calculate_trade_conditions1: {e}")
    return data[['Date','Open',"High", "Low", "Close", "Adj Close", "Volume", "Trade condition"]]
