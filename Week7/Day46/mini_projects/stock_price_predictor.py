"""
Day 46 Mini Project: Stock Price Predictor
==========================================
Build an end-to-end stock price forecasting system.

This project demonstrates:
- Data acquisition and preprocessing
- Multiple forecasting approaches
- Model comparison and evaluation
- Making predictions

Note: This uses synthetic data for demonstration.
      For real data, use yfinance: pip install yfinance
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

print("=" * 70)
print("STOCK PRICE PREDICTOR - Mini Project")
print("=" * 70)

# ============================================================
# STEP 1: DATA ACQUISITION
# ============================================================
print("\n" + "=" * 70)
print("STEP 1: Data Acquisition")
print("=" * 70)

def generate_stock_data(symbol="DEMO", days=500, seed=42):
    """
    Generate realistic synthetic stock data.
    
    In production, replace with:
    import yfinance as yf
    df = yf.download(symbol, start=start_date, end=end_date)
    """
    np.random.seed(seed)
    
    # Trading days
    dates = pd.bdate_range(end=datetime.now(), periods=days)
    
    # Random walk with drift (geometric Brownian motion)
    daily_returns = np.random.normal(0.0005, 0.02, days)
    
    # Add some structure
    # Trend component
    trend = np.linspace(0, 0.3, days)
    
    # Volatility clustering (GARCH-like effect)
    volatility = 0.02 + 0.01 * np.sin(2 * np.pi * np.arange(days) / 60)
    returns = daily_returns * (1 + volatility) + trend / days
    
    # Generate prices
    initial_price = 100
    prices = initial_price * np.exp(np.cumsum(returns))
    
    # Generate OHLCV data
    high = prices * (1 + np.abs(np.random.normal(0, 0.01, days)))
    low = prices * (1 - np.abs(np.random.normal(0, 0.01, days)))
    open_price = (high + low) / 2 + np.random.normal(0, 0.5, days)
    volume = np.random.randint(1_000_000, 10_000_000, days)
    
    df = pd.DataFrame({
        'Date': dates,
        'Open': open_price,
        'High': high,
        'Low': low,
        'Close': prices,
        'Volume': volume
    })
    df.set_index('Date', inplace=True)
    
    return df

# Generate data
stock_data = generate_stock_data("DEMO", days=500)

print(f"\nStock Data Summary:")
print(f"Period: {stock_data.index[0].date()} to {stock_data.index[-1].date()}")
print(f"Total trading days: {len(stock_data)}")
print(f"\nFirst 5 rows:")
print(stock_data.head())

print(f"\nBasic Statistics:")
print(stock_data['Close'].describe())

# ============================================================
# STEP 2: DATA PREPROCESSING
# ============================================================
print("\n" + "=" * 70)
print("STEP 2: Data Preprocessing")
print("=" * 70)

def preprocess_stock_data(df):
    """Add technical indicators and features"""
    data = df.copy()
    
    # Returns
    data['Returns'] = data['Close'].pct_change()
    data['Log_Returns'] = np.log(data['Close']).diff()
    
    # Moving Averages
    data['MA_5'] = data['Close'].rolling(window=5).mean()
    data['MA_20'] = data['Close'].rolling(window=20).mean()
    data['MA_50'] = data['Close'].rolling(window=50).mean()
    
    # Exponential Moving Average
    data['EMA_12'] = data['Close'].ewm(span=12).mean()
    data['EMA_26'] = data['Close'].ewm(span=26).mean()
    
    # MACD
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['MACD_Signal'] = data['MACD'].ewm(span=9).mean()
    
    # Volatility (20-day rolling std of returns)
    data['Volatility'] = data['Returns'].rolling(window=20).std() * np.sqrt(252)
    
    # RSI (Relative Strength Index)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Bollinger Bands
    data['BB_Middle'] = data['Close'].rolling(window=20).mean()
    data['BB_Std'] = data['Close'].rolling(window=20).std()
    data['BB_Upper'] = data['BB_Middle'] + 2 * data['BB_Std']
    data['BB_Lower'] = data['BB_Middle'] - 2 * data['BB_Std']
    
    # Lag features
    for lag in [1, 5, 10]:
        data[f'Close_Lag_{lag}'] = data['Close'].shift(lag)
    
    return data

# Preprocess
stock_features = preprocess_stock_data(stock_data)
print(f"\nFeatures created: {len(stock_features.columns)}")
print(f"Columns: {list(stock_features.columns)}")
print(f"\nSample with features:")
print(stock_features[['Close', 'MA_20', 'RSI', 'MACD', 'Volatility']].dropna().head())

# ============================================================
# STEP 3: TRAIN-TEST SPLIT
# ============================================================
print("\n" + "=" * 70)
print("STEP 3: Train-Test Split")
print("=" * 70)

def time_based_split(df, train_ratio=0.8):
    """Split data chronologically"""
    n = len(df)
    train_size = int(n * train_ratio)
    
    train = df.iloc[:train_size].copy()
    test = df.iloc[train_size:].copy()
    
    return train, test

# Clean data (remove NaN from feature engineering)
clean_data = stock_features.dropna()

# Split
train_data, test_data = time_based_split(clean_data, train_ratio=0.8)

print(f"\nTraining set: {len(train_data)} days")
print(f"  Period: {train_data.index[0].date()} to {train_data.index[-1].date()}")
print(f"\nTest set: {len(test_data)} days")
print(f"  Period: {test_data.index[0].date()} to {test_data.index[-1].date()}")

# ============================================================
# STEP 4: MODEL 1 - BASELINE (Naive Forecast)
# ============================================================
print("\n" + "=" * 70)
print("STEP 4: Model 1 - Baseline (Naive Forecast)")
print("=" * 70)

def naive_forecast(train, test):
    """Predict using last known value"""
    last_value = train['Close'].iloc[-1]
    predictions = np.full(len(test), last_value)
    return predictions

naive_pred = naive_forecast(train_data, test_data)
print(f"\nNaive forecast: Always predict last training value = ${naive_pred[0]:.2f}")

# ============================================================
# STEP 5: MODEL 2 - MOVING AVERAGE
# ============================================================
print("\n" + "=" * 70)
print("STEP 5: Model 2 - Moving Average")
print("=" * 70)

def ma_forecast(train, test, window=20):
    """Predict using moving average"""
    # Start with the last MA value from training
    last_ma = train['Close'].rolling(window).mean().iloc[-1]
    
    # For simplicity, use constant forecast
    predictions = np.full(len(test), last_ma)
    return predictions

ma_pred = ma_forecast(train_data, test_data, window=20)
print(f"\nMA(20) forecast: ${ma_pred[0]:.2f}")

# ============================================================
# STEP 6: MODEL 3 - SIMPLE LINEAR REGRESSION
# ============================================================
print("\n" + "=" * 70)
print("STEP 6: Model 3 - Linear Regression")
print("=" * 70)

def linear_regression_forecast(train, test):
    """Simple linear regression on time"""
    # Prepare data
    X_train = np.arange(len(train)).reshape(-1, 1)
    y_train = train['Close'].values
    
    # Fit linear regression (numpy lstsq)
    X_train_bias = np.c_[np.ones(len(X_train)), X_train]
    coeffs = np.linalg.lstsq(X_train_bias, y_train, rcond=None)[0]
    
    # Predict for test period
    X_test = np.arange(len(train), len(train) + len(test)).reshape(-1, 1)
    X_test_bias = np.c_[np.ones(len(X_test)), X_test]
    predictions = X_test_bias @ coeffs
    
    return predictions, coeffs

lr_pred, lr_coeffs = linear_regression_forecast(train_data, test_data)
print(f"\nLinear regression: y = {lr_coeffs[0]:.2f} + {lr_coeffs[1]:.4f} * t")
print(f"First prediction: ${lr_pred[0]:.2f}")
print(f"Last prediction: ${lr_pred[-1]:.2f}")

# ============================================================
# STEP 7: MODEL 4 - ARIMA-LIKE (Simple AR)
# ============================================================
print("\n" + "=" * 70)
print("STEP 7: Model 4 - Simple AR Model")
print("=" * 70)

def simple_ar_forecast(train, test, lag=5):
    """Simple autoregressive model"""
    prices = train['Close'].values
    
    # Build lag matrix
    n = len(prices)
    X = np.column_stack([prices[i:n-lag+i] for i in range(lag)])
    y = prices[lag:]
    
    # Fit
    X_bias = np.c_[np.ones(len(X)), X]
    coeffs = np.linalg.lstsq(X_bias, y, rcond=None)[0]
    
    # Recursive prediction
    predictions = []
    history = list(prices[-lag:])
    
    for _ in range(len(test)):
        X_pred = np.array([1] + history[-lag:])
        next_pred = X_pred @ coeffs
        predictions.append(next_pred)
        history.append(next_pred)
    
    return np.array(predictions)

ar_pred = simple_ar_forecast(train_data, test_data, lag=5)
print(f"\nAR(5) forecast:")
print(f"  First prediction: ${ar_pred[0]:.2f}")
print(f"  Last prediction: ${ar_pred[-1]:.2f}")

# ============================================================
# STEP 8: MODEL EVALUATION
# ============================================================
print("\n" + "=" * 70)
print("STEP 8: Model Evaluation")
print("=" * 70)

def evaluate_model(actual, predicted, model_name):
    """Calculate evaluation metrics"""
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    mae = np.mean(np.abs(actual - predicted))
    mse = np.mean((actual - predicted) ** 2)
    rmse = np.sqrt(mse)
    
    # MAPE
    non_zero = actual != 0
    mape = np.mean(np.abs((actual[non_zero] - predicted[non_zero]) / actual[non_zero])) * 100
    
    # Direction accuracy (for trading)
    actual_direction = np.sign(np.diff(actual))
    pred_direction = np.sign(np.diff(predicted))
    direction_accuracy = np.mean(actual_direction == pred_direction) * 100
    
    print(f"\n{model_name}:")
    print(f"  MAE: ${mae:.2f}")
    print(f"  RMSE: ${rmse:.2f}")
    print(f"  MAPE: {mape:.2f}%")
    print(f"  Direction Accuracy: {direction_accuracy:.1f}%")
    
    return {'MAE': mae, 'RMSE': rmse, 'MAPE': mape, 'Dir_Acc': direction_accuracy}

actual_prices = test_data['Close'].values

print("\n--- Model Comparison ---")
results = {}
results['Naive'] = evaluate_model(actual_prices, naive_pred, "Naive Forecast")
results['MA(20)'] = evaluate_model(actual_prices, ma_pred, "Moving Average (20)")
results['Linear'] = evaluate_model(actual_prices, lr_pred, "Linear Regression")
results['AR(5)'] = evaluate_model(actual_prices, ar_pred, "AR(5) Model")

# ============================================================
# STEP 9: VISUALIZATION
# ============================================================
print("\n" + "=" * 70)
print("STEP 9: Visualization")
print("=" * 70)

# Create figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Full price history with train/test split
ax1 = axes[0, 0]
ax1.plot(train_data.index, train_data['Close'], 'b-', label='Training', alpha=0.7)
ax1.plot(test_data.index, test_data['Close'], 'g-', label='Test (Actual)', linewidth=2)
ax1.axvline(x=train_data.index[-1], color='r', linestyle='--', label='Split Point')
ax1.set_title('Stock Price History')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price ($)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Model predictions comparison
ax2 = axes[0, 1]
ax2.plot(test_data.index, actual_prices, 'g-', label='Actual', linewidth=2)
ax2.plot(test_data.index, naive_pred, 'r--', label='Naive', alpha=0.7)
ax2.plot(test_data.index, ma_pred, 'b--', label='MA(20)', alpha=0.7)
ax2.plot(test_data.index, lr_pred, 'm--', label='Linear', alpha=0.7)
ax2.plot(test_data.index, ar_pred, 'c--', label='AR(5)', alpha=0.7)
ax2.set_title('Model Predictions vs Actual')
ax2.set_xlabel('Date')
ax2.set_ylabel('Price ($)')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Model errors
ax3 = axes[1, 0]
errors = {
    'Naive': actual_prices - naive_pred,
    'MA(20)': actual_prices - ma_pred,
    'Linear': actual_prices - lr_pred,
    'AR(5)': actual_prices - ar_pred
}
bp = ax3.boxplot([errors[k] for k in errors], labels=errors.keys())
ax3.set_title('Prediction Errors Distribution')
ax3.set_ylabel('Error ($)')
ax3.axhline(y=0, color='r', linestyle='--', alpha=0.5)
ax3.grid(True, alpha=0.3)

# Plot 4: Metrics comparison
ax4 = axes[1, 1]
models = list(results.keys())
rmse_values = [results[m]['RMSE'] for m in models]
mape_values = [results[m]['MAPE'] for m in models]

x = np.arange(len(models))
width = 0.35

bars1 = ax4.bar(x - width/2, rmse_values, width, label='RMSE ($)', color='steelblue')
ax4.set_ylabel('RMSE ($)')
ax4.set_title('Model Performance Comparison')
ax4.set_xticks(x)
ax4.set_xticklabels(models)

ax4_twin = ax4.twinx()
bars2 = ax4_twin.bar(x + width/2, mape_values, width, label='MAPE (%)', color='coral')
ax4_twin.set_ylabel('MAPE (%)')

ax4.legend(loc='upper left')
ax4_twin.legend(loc='upper right')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('stock_prediction_results.png', dpi=100, bbox_inches='tight')
print("\n✅ Saved visualization to 'stock_prediction_results.png'")
plt.close()

# ============================================================
# STEP 10: FUTURE PREDICTIONS
# ============================================================
print("\n" + "=" * 70)
print("STEP 10: Future Predictions")
print("=" * 70)

# Use best performing model (AR in this demo)
def predict_future(data, days=10):
    """Predict next N days"""
    prices = data['Close'].values
    lag = 5
    
    # Fit AR model
    n = len(prices)
    X = np.column_stack([prices[i:n-lag+i] for i in range(lag)])
    y = prices[lag:]
    X_bias = np.c_[np.ones(len(X)), X]
    coeffs = np.linalg.lstsq(X_bias, y, rcond=None)[0]
    
    # Predict
    predictions = []
    history = list(prices[-lag:])
    
    last_date = data.index[-1]
    future_dates = pd.bdate_range(start=last_date + timedelta(days=1), periods=days)
    
    for _ in range(days):
        X_pred = np.array([1] + history[-lag:])
        next_pred = X_pred @ coeffs
        predictions.append(next_pred)
        history.append(next_pred)
    
    return pd.DataFrame({
        'Date': future_dates,
        'Predicted_Close': predictions
    })

# Predict next 10 trading days
future_predictions = predict_future(clean_data, days=10)

print(f"\nNext 10 Trading Days Forecast:")
print(future_predictions.to_string(index=False))

# ============================================================
# STEP 11: SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print("""
Completed Tasks:
✅ Generated synthetic stock data (or use yfinance for real data)
✅ Created technical indicators (MA, EMA, MACD, RSI, BB)
✅ Performed time-based train-test split
✅ Implemented 4 forecasting models:
   - Naive (baseline)
   - Moving Average
   - Linear Regression
   - Autoregressive (AR)
✅ Evaluated models with MAE, RMSE, MAPE
✅ Visualized results
✅ Generated future predictions

Best Model Performance:
""")

# Find best model
best_model = min(results.items(), key=lambda x: x[1]['RMSE'])
print(f"Best Model by RMSE: {best_model[0]}")
print(f"  RMSE: ${best_model[1]['RMSE']:.2f}")
print(f"  MAPE: {best_model[1]['MAPE']:.2f}%")

print("""
Next Steps to Improve:
1. Use real stock data from yfinance
2. Implement ARIMA with statsmodels
3. Build LSTM with TensorFlow/Keras
4. Try Prophet for better seasonality
5. Add more features (sentiment, volume patterns)
6. Implement ensemble methods
7. Add confidence intervals

⚠️ Disclaimer: This is for educational purposes only.
   Stock prediction is extremely difficult and unreliable.
   Never make investment decisions based on predictions!
""")

# Cleanup
import os
if os.path.exists('stock_prediction_results.png'):
    os.remove('stock_prediction_results.png')
print("✅ Cleaned up generated files")

print("\n" + "=" * 70)
print("✅ Mini Project Complete!")
print("=" * 70)
