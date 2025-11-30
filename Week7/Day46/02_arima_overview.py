"""
Day 46 - ARIMA Overview
=======================
Learn: ARIMA model for time series forecasting

Key Concepts:
- AR (AutoRegressive) component
- I (Integrated/Differencing) component
- MA (Moving Average) component
- Model selection and fitting
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ========== WHAT IS ARIMA? ==========
print("=" * 60)
print("WHAT IS ARIMA?")
print("=" * 60)

print("""
ARIMA = AutoRegressive Integrated Moving Average

A popular model for time series forecasting that combines:

1. AR (AutoRegressive) - p
   - Uses past values to predict current value
   - Y_t depends on Y_{t-1}, Y_{t-2}, ..., Y_{t-p}
   
2. I (Integrated) - d
   - Number of differencing operations
   - Makes the series stationary
   - d=1 means Y_t - Y_{t-1}
   
3. MA (Moving Average) - q
   - Uses past forecast errors
   - Y_t depends on ε_{t-1}, ε_{t-2}, ..., ε_{t-q}

ARIMA(p, d, q):
- p = order of AR component
- d = degree of differencing
- q = order of MA component

For seasonal data: SARIMA(p,d,q)(P,D,Q,s)
""")

# ========== UNDERSTANDING AR MODEL ==========
print("\n" + "=" * 60)
print("UNDERSTANDING AR MODEL")
print("=" * 60)

print("""
AR(p) Model: AutoRegressive of order p

Formula:
Y_t = c + φ₁Y_{t-1} + φ₂Y_{t-2} + ... + φₚY_{t-p} + ε_t

Where:
- c = constant
- φᵢ = AR coefficients
- ε_t = white noise error

Example AR(1):
Y_t = c + φ₁Y_{t-1} + ε_t

Intuition: Today's value depends on yesterday's value
(like temperature, which doesn't change drastically day to day)
""")

# Simulate AR(1) process
np.random.seed(42)
n = 200
phi = 0.7  # AR coefficient
c = 10     # constant
epsilon = np.random.normal(0, 1, n)

# Generate AR(1) series
ar1 = np.zeros(n)
ar1[0] = c / (1 - phi)  # Start near equilibrium

for t in range(1, n):
    ar1[t] = c + phi * ar1[t-1] + epsilon[t]

print(f"\nSimulated AR(1) with φ = {phi}:")
print(f"Mean: {ar1.mean():.2f}")
print(f"Std: {ar1.std():.2f}")
print(f"Theoretical Mean: {c/(1-phi):.2f}")

# ========== UNDERSTANDING MA MODEL ==========
print("\n" + "=" * 60)
print("UNDERSTANDING MA MODEL")
print("=" * 60)

print("""
MA(q) Model: Moving Average of order q

Formula:
Y_t = μ + ε_t + θ₁ε_{t-1} + θ₂ε_{t-2} + ... + θₓε_{t-q}

Where:
- μ = mean of the series
- θᵢ = MA coefficients
- ε_t = white noise error

Example MA(1):
Y_t = μ + ε_t + θ₁ε_{t-1}

Intuition: Today's value is the mean plus today's error
plus some fraction of yesterday's error
""")

# Simulate MA(1) process
theta = 0.6  # MA coefficient
mu = 20      # mean

# Generate MA(1) series
ma1 = np.zeros(n)
for t in range(1, n):
    ma1[t] = mu + epsilon[t] + theta * epsilon[t-1]

print(f"\nSimulated MA(1) with θ = {theta}:")
print(f"Mean: {ma1.mean():.2f}")
print(f"Std: {ma1.std():.2f}")
print(f"Theoretical Mean: {mu}")

# ========== DIFFERENCING ==========
print("\n" + "=" * 60)
print("DIFFERENCING (THE 'I' IN ARIMA)")
print("=" * 60)

print("""
Differencing removes trends and makes data stationary.

First difference (d=1):
  Y'_t = Y_t - Y_{t-1}

Second difference (d=2):
  Y''_t = Y'_t - Y'_{t-1}
        = (Y_t - Y_{t-1}) - (Y_{t-1} - Y_{t-2})
        = Y_t - 2Y_{t-1} + Y_{t-2}

When to use:
- d=0: Data is already stationary
- d=1: Data has a trend
- d=2: Rarely needed (curved trend)

Rule: Don't over-difference! Usually d ≤ 2
""")

# Create data with trend
trend_data = np.linspace(0, 50, 100) + np.random.normal(0, 2, 100)
series = pd.Series(trend_data)

# Apply differencing
diff1 = series.diff().dropna()
diff2 = series.diff().diff().dropna()

print("\nOriginal Data Statistics:")
print(f"  Mean: {series.mean():.2f}, Std: {series.std():.2f}")

print("\nAfter First Differencing:")
print(f"  Mean: {diff1.mean():.2f}, Std: {diff1.std():.2f}")

print("\nAfter Second Differencing:")
print(f"  Mean: {diff2.mean():.2f}, Std: {diff2.std():.2f}")

# ========== CHOOSING p, d, q ==========
print("\n" + "=" * 60)
print("CHOOSING p, d, q PARAMETERS")
print("=" * 60)

print("""
Step 1: Determine d (Differencing)
- Plot the data
- Check ADF test for stationarity
- Difference until stationary (usually d ≤ 2)

Step 2: Determine p (AR order) using PACF
- Look at PACF plot
- p = number of lags that cut off sharply

Step 3: Determine q (MA order) using ACF
- Look at ACF plot  
- q = number of lags that cut off sharply

Rules of Thumb:
┌────────────────┬────────────────┬─────────────────┐
│    Pattern     │      ACF       │      PACF       │
├────────────────┼────────────────┼─────────────────┤
│     AR(p)      │ Gradual decay  │ Cuts off at p   │
│     MA(q)      │ Cuts off at q  │ Gradual decay   │
│   ARMA(p,q)    │ Gradual decay  │ Gradual decay   │
└────────────────┴────────────────┴─────────────────┘

Alternatively: Use auto_arima for automatic selection
""")

# ========== IMPLEMENTING ARIMA (Manual Approach) ==========
print("\n" + "=" * 60)
print("IMPLEMENTING ARIMA (Manual Approach)")
print("=" * 60)

print("""
Using statsmodels:

from statsmodels.tsa.arima.model import ARIMA

# Fit model
model = ARIMA(data, order=(p, d, q))
results = model.fit()

# Summary
print(results.summary())

# Forecast
forecast = results.forecast(steps=10)
""")

# Simple ARIMA-like forecast using basic approach
# (without statsmodels for demonstration)

def simple_ar_forecast(series, p=1, steps=10):
    """Simple AR model forecast"""
    series = np.array(series)
    n = len(series)
    
    # Fit AR coefficients using OLS (simplified)
    # Build design matrix
    X = np.column_stack([series[i:n-p+i] for i in range(p)])
    y = series[p:]
    
    # Solve for coefficients
    coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
    
    # Generate forecasts
    forecasts = []
    last_values = list(series[-p:])
    
    for _ in range(steps):
        next_val = np.dot(coeffs, last_values[-p:][::-1])
        forecasts.append(next_val)
        last_values.append(next_val)
    
    return forecasts, coeffs

# Create sample data
np.random.seed(42)
sample_data = ar1  # Use our AR(1) data from earlier

# Fit and forecast
forecasts, coeffs = simple_ar_forecast(sample_data, p=1, steps=10)

print(f"\nSimple AR(1) Model Results:")
print(f"Estimated coefficient: {coeffs[0]:.4f}")
print(f"True coefficient: {phi}")
print(f"\nForecasts for next 10 periods:")
for i, f in enumerate(forecasts, 1):
    print(f"  t+{i}: {f:.2f}")

# ========== MODEL EVALUATION ==========
print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print("""
Common metrics for time series models:

1. AIC (Akaike Information Criterion)
   - Lower is better
   - Penalizes complexity

2. BIC (Bayesian Information Criterion)
   - Lower is better
   - Stronger penalty for complexity

3. RMSE (Root Mean Square Error)
   - √(mean((actual - predicted)²))
   - Same units as data

4. MAE (Mean Absolute Error)
   - mean(|actual - predicted|)
   - Robust to outliers

5. MAPE (Mean Absolute Percentage Error)
   - mean(|actual - predicted| / |actual|) × 100
   - Percentage scale
""")

# Simple evaluation metrics
def evaluate_forecast(actual, predicted):
    """Calculate forecast evaluation metrics"""
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    mae = np.mean(np.abs(actual - predicted))
    mse = np.mean((actual - predicted) ** 2)
    rmse = np.sqrt(mse)
    
    # MAPE (avoid division by zero)
    non_zero = actual != 0
    mape = np.mean(np.abs((actual[non_zero] - predicted[non_zero]) / actual[non_zero])) * 100
    
    return {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'MAPE': mape
    }

# Demo evaluation
actual_values = sample_data[-10:]
simple_forecast = [sample_data[-11]] * 10  # Naive forecast (repeat last value)

metrics = evaluate_forecast(actual_values, simple_forecast)
print("\nEvaluation of Naive Forecast:")
for metric, value in metrics.items():
    print(f"  {metric}: {value:.4f}")

# ========== COMPLETE ARIMA WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE ARIMA WORKFLOW")
print("=" * 60)

print("""
Step-by-step ARIMA workflow:

1. VISUALIZE the data
   - Plot time series
   - Look for trends, seasonality

2. MAKE IT STATIONARY
   - ADF test
   - Difference if needed
   - Transform if needed (log)

3. IDENTIFY p, q
   - Plot ACF and PACF
   - Use information criteria
   - Or use auto_arima

4. FIT the model
   model = ARIMA(data, order=(p,d,q))
   results = model.fit()

5. DIAGNOSE residuals
   - Should be white noise
   - No autocorrelation
   - Normal distribution

6. FORECAST
   forecast = results.forecast(steps=n)

7. EVALUATE
   - Compare with test data
   - Calculate metrics
""")

# ========== SEASONAL ARIMA (SARIMA) ==========
print("\n" + "=" * 60)
print("SEASONAL ARIMA (SARIMA)")
print("=" * 60)

print("""
SARIMA(p,d,q)(P,D,Q,s) for seasonal data

Additional parameters:
- P = seasonal AR order
- D = seasonal differencing
- Q = seasonal MA order
- s = seasonal period (12 for monthly, 4 for quarterly)

Example: SARIMA(1,1,1)(1,1,1,12) for monthly data
- Non-seasonal: AR(1), diff(1), MA(1)
- Seasonal: SAR(1), Sdiff(1), SMA(1), period=12

Usage:
from statsmodels.tsa.statespace.sarimax import SARIMAX

model = SARIMAX(data, 
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12))
results = model.fit()
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Sales Forecasting")
print("=" * 60)

# Create synthetic monthly sales data with trend and seasonality
np.random.seed(42)
n_months = 48  # 4 years of data

# Components
months = pd.date_range('2020-01-01', periods=n_months, freq='MS')
trend = np.linspace(100, 200, n_months)
seasonal = 30 * np.sin(2 * np.pi * np.arange(n_months) / 12)  # Yearly cycle
noise = np.random.normal(0, 10, n_months)

sales = trend + seasonal + noise
sales_df = pd.DataFrame({'sales': sales}, index=months)

print("Monthly Sales Data (First 12 months):")
print(sales_df.head(12).to_string())

# Split data
train_size = 36  # 3 years for training
train = sales_df[:train_size]
test = sales_df[train_size:]

print(f"\nTraining data: {len(train)} months")
print(f"Test data: {len(test)} months")

# Simple forecast using moving average
ma_window = 3
last_ma = train['sales'].rolling(ma_window).mean().iloc[-1]

print(f"\nSimple Moving Average Forecast (window={ma_window}):")
print(f"Forecast value: {last_ma:.2f}")
print(f"\nActual test values:")
print(test.to_string())

# Calculate simple metrics
simple_pred = [last_ma] * len(test)
eval_metrics = evaluate_forecast(test['sales'].values, simple_pred)

print("\nSimple MA Forecast Metrics:")
for metric, value in eval_metrics.items():
    print(f"  {metric}: {value:.2f}")

# ========== AUTO ARIMA ==========
print("\n" + "=" * 60)
print("AUTO ARIMA")
print("=" * 60)

print("""
Auto ARIMA automatically selects best (p, d, q):

from pmdarima import auto_arima

model = auto_arima(data,
                   start_p=0, max_p=5,
                   start_q=0, max_q=5,
                   d=None,           # Auto-select d
                   seasonal=True,    # Include seasonality
                   m=12,            # Seasonal period
                   trace=True,      # Show progress
                   error_action='ignore',
                   suppress_warnings=True)

print(model.summary())
forecast = model.predict(n_periods=10)

Installation: pip install pmdarima
""")

# ========== COMMON PITFALLS ==========
print("\n" + "=" * 60)
print("COMMON PITFALLS")
print("=" * 60)

print("""
1. ❌ Over-differencing
   - If variance increases after differencing, stop!
   - Usually d ≤ 2

2. ❌ Ignoring seasonality
   - Use SARIMA for seasonal data
   - Check seasonal plots

3. ❌ Not checking residuals
   - Residuals should be white noise
   - Use Ljung-Box test

4. ❌ Using future data in training
   - Always use time-based split
   - Never shuffle time series

5. ❌ Too many parameters
   - Model may overfit
   - Use AIC/BIC to compare

6. ❌ Forecasting too far ahead
   - Accuracy decreases with horizon
   - Confidence intervals widen

Best Practices:
✅ Start simple (ARIMA(1,1,1))
✅ Always validate on holdout data
✅ Use rolling forecasts for evaluation
✅ Consider ensemble methods
""")

print("\n" + "=" * 60)
print("✅ ARIMA Overview - Complete!")
print("=" * 60)
