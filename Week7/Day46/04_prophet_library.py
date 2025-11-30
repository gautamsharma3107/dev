"""
Day 46 - Prophet Library
========================
Learn: Facebook Prophet for time series forecasting

Key Concepts:
- Prophet model basics
- Seasonality handling
- Trend changepoints
- Adding regressors
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ========== WHAT IS PROPHET? ==========
print("=" * 60)
print("WHAT IS PROPHET?")
print("=" * 60)

print("""
Prophet: Open-source forecasting tool by Facebook (Meta)

Key Features:
✅ Easy to use - works out of the box
✅ Handles missing data automatically
✅ Robust to outliers
✅ Multiple seasonality (daily, weekly, yearly)
✅ Holiday effects
✅ Interpretable components
✅ Uncertainty intervals

Best For:
- Business forecasting
- Data with strong seasonal patterns
- Multiple seasonalities
- Holiday effects
- Missing data present

Installation:
pip install prophet
""")

# ========== PROPHET MODEL ==========
print("\n" + "=" * 60)
print("PROPHET MODEL")
print("=" * 60)

print("""
Prophet uses an additive model:

y(t) = g(t) + s(t) + h(t) + ε_t

Where:
- g(t) = Trend (linear or logistic growth)
- s(t) = Seasonality (Fourier series)
- h(t) = Holiday effects
- ε_t  = Error term

Key Advantages:
1. Automatic trend changepoint detection
2. Flexible seasonality modeling
3. Easy holiday incorporation
4. Interpretable components
""")

# ========== DATA FORMAT ==========
print("\n" + "=" * 60)
print("DATA FORMAT FOR PROPHET")
print("=" * 60)

print("""
Prophet requires specific column names:
- 'ds': datestamp (datetime)
- 'y': target value (numeric)

Example:
           ds          y
0  2024-01-01   100.5
1  2024-01-02   102.3
2  2024-01-03    98.7
...

Important:
- ds must be datetime format
- y must be numeric
- No index needed (use columns)
""")

# Create sample data in Prophet format
np.random.seed(42)
n_days = 730  # 2 years

dates = pd.date_range('2022-01-01', periods=n_days, freq='D')

# Create realistic pattern
trend = np.linspace(100, 150, n_days)
yearly_season = 20 * np.sin(2 * np.pi * np.arange(n_days) / 365.25)
weekly_season = 5 * np.sin(2 * np.pi * np.arange(n_days) / 7)
noise = np.random.normal(0, 5, n_days)

values = trend + yearly_season + weekly_season + noise

# Create Prophet-format DataFrame
df = pd.DataFrame({
    'ds': dates,
    'y': values
})

print("\nSample Data (Prophet format):")
print(df.head(10))
print(f"\nTotal records: {len(df)}")

# ========== BASIC PROPHET USAGE ==========
print("\n" + "=" * 60)
print("BASIC PROPHET USAGE")
print("=" * 60)

basic_code = """
from prophet import Prophet

# 1. Create and fit model
model = Prophet()
model.fit(df)

# 2. Create future dataframe
future = model.make_future_dataframe(periods=30)  # 30 days ahead

# 3. Make predictions
forecast = model.predict(future)

# 4. View results
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# 5. Plot
model.plot(forecast)
plt.show()

# 6. Plot components (trend, seasonality)
model.plot_components(forecast)
plt.show()
"""

print(basic_code)

# ========== SIMULATED PROPHET OUTPUT ==========
print("\n" + "=" * 60)
print("SIMULATED FORECAST OUTPUT")
print("=" * 60)

# Simulate what Prophet output looks like
def simulate_prophet_forecast(df, periods=30):
    """Simulate Prophet-like forecast"""
    # Last known values
    last_date = df['ds'].iloc[-1]
    last_value = df['y'].iloc[-1]
    
    # Create future dates
    future_dates = pd.date_range(last_date + timedelta(days=1), 
                                  periods=periods, freq='D')
    
    # Simple linear extrapolation with seasonality
    trend_slope = (df['y'].iloc[-30:].mean() - df['y'].iloc[:30].mean()) / len(df)
    
    forecasts = []
    for i, date in enumerate(future_dates):
        # Trend
        trend_val = last_value + trend_slope * (i + 1)
        
        # Yearly seasonality
        day_of_year = date.timetuple().tm_yday
        yearly = 20 * np.sin(2 * np.pi * day_of_year / 365.25)
        
        # Weekly seasonality
        day_of_week = date.weekday()
        weekly = 5 * np.sin(2 * np.pi * day_of_week / 7)
        
        yhat = trend_val + yearly + weekly
        
        forecasts.append({
            'ds': date,
            'yhat': yhat,
            'yhat_lower': yhat - 15,  # Simulated uncertainty
            'yhat_upper': yhat + 15
        })
    
    return pd.DataFrame(forecasts)

forecast_df = simulate_prophet_forecast(df, 30)

print("\nSimulated Forecast (next 30 days):")
print(forecast_df.to_string())

# ========== CONFIGURING PROPHET ==========
print("\n" + "=" * 60)
print("CONFIGURING PROPHET")
print("=" * 60)

config_code = """
# Default Prophet
model = Prophet()

# Customized Prophet
model = Prophet(
    # Growth
    growth='linear',        # or 'logistic' for bounded growth
    
    # Changepoints
    changepoint_prior_scale=0.05,  # Flexibility (0.001-0.5)
    changepoints=None,             # Auto-detect or specify dates
    n_changepoints=25,             # Number of potential changepoints
    
    # Seasonality
    yearly_seasonality=True,       # Yearly pattern
    weekly_seasonality=True,       # Weekly pattern
    daily_seasonality=False,       # Daily pattern (sub-daily data)
    seasonality_mode='additive',   # or 'multiplicative'
    seasonality_prior_scale=10,    # Seasonality flexibility
    
    # Holidays
    holidays=holidays_df,          # DataFrame of holidays
    holidays_prior_scale=10,       # Holiday effect flexibility
    
    # Uncertainty
    interval_width=0.8,            # Uncertainty interval (80%)
    
    # Other
    mcmc_samples=0                 # 0 for MAP, >0 for full Bayesian
)
"""

print(config_code)

# ========== HANDLING SEASONALITY ==========
print("\n" + "=" * 60)
print("HANDLING SEASONALITY")
print("=" * 60)

print("""
Built-in Seasonalities:
- yearly_seasonality: True/False/auto
- weekly_seasonality: True/False/auto
- daily_seasonality: True/False/auto

Auto-detection:
- yearly: data spans > 2 years
- weekly: data spans > 2 weeks
- daily: data spans > 2 days (sub-daily data)

Seasonality Modes:
- 'additive': seasonal effect adds to trend
- 'multiplicative': seasonal effect scales with trend

When to use multiplicative:
- Sales that grow AND become more seasonal
- Revenue with percentage variations
""")

seasonality_code = """
# Add custom seasonality
model = Prophet(weekly_seasonality=False)

# Monthly seasonality
model.add_seasonality(
    name='monthly',
    period=30.5,
    fourier_order=5
)

# Quarterly seasonality
model.add_seasonality(
    name='quarterly',
    period=91.25,
    fourier_order=8
)

# Conditional seasonality (e.g., NFL season)
def is_nfl_season(ds):
    date = pd.to_datetime(ds)
    return (date.month > 8) | (date.month < 2)

df['on_season'] = df['ds'].apply(is_nfl_season)

model.add_seasonality(
    name='weekly_on_season',
    period=7,
    fourier_order=3,
    condition_name='on_season'
)
"""

print(seasonality_code)

# ========== HOLIDAYS ==========
print("\n" + "=" * 60)
print("HANDLING HOLIDAYS")
print("=" * 60)

print("""
Prophet can model holiday effects that repeat yearly.

Holiday DataFrame format:
- holiday: name of holiday
- ds: date of holiday
- lower_window: days before (e.g., -1)
- upper_window: days after (e.g., 1)
""")

# Create sample holidays
holidays = pd.DataFrame({
    'holiday': 'major_event',
    'ds': pd.to_datetime(['2022-12-25', '2023-12-25', 
                          '2022-01-01', '2023-01-01',
                          '2022-07-04', '2023-07-04']),
    'lower_window': 0,
    'upper_window': 1
})

print("\nSample Holidays DataFrame:")
print(holidays)

holiday_code = """
# Create holidays DataFrame
holidays = pd.DataFrame({
    'holiday': ['christmas', 'christmas', 'new_year', 'new_year'],
    'ds': pd.to_datetime(['2022-12-25', '2023-12-25', 
                          '2022-01-01', '2023-01-01']),
    'lower_window': -1,  # Include day before
    'upper_window': 1    # Include day after
})

# Add to model
model = Prophet(holidays=holidays)

# Or add built-in country holidays
model = Prophet()
model.add_country_holidays(country_name='US')
# Available: US, UK, DE, FR, etc.
"""

print(holiday_code)

# ========== TREND CHANGEPOINTS ==========
print("\n" + "=" * 60)
print("TREND CHANGEPOINTS")
print("=" * 60)

print("""
Changepoints: Points where trend growth rate changes

Prophet auto-detects changepoints in first 80% of data.

Parameters:
- n_changepoints: Number of potential changepoints (default 25)
- changepoint_range: Proportion of history for changepoints (0.8)
- changepoint_prior_scale: Flexibility (0.05 default)
  - Larger = more flexible (may overfit)
  - Smaller = less flexible (may underfit)
""")

changepoint_code = """
# View detected changepoints
print(model.changepoints)

# Set specific changepoints
model = Prophet(changepoints=['2023-01-01', '2023-06-15'])

# Adjust flexibility
# More flexible (fits sudden changes)
model = Prophet(changepoint_prior_scale=0.5)

# Less flexible (smoother trend)
model = Prophet(changepoint_prior_scale=0.01)
"""

print(changepoint_code)

# ========== ADDING REGRESSORS ==========
print("\n" + "=" * 60)
print("ADDING REGRESSORS")
print("=" * 60)

print("""
Add external variables that influence the forecast.

Examples:
- Temperature for ice cream sales
- Marketing spend for revenue
- Economic indicators
""")

regressor_code = """
# Add regressor columns to your data
df['marketing_spend'] = marketing_data
df['temperature'] = temp_data

# Add to model
model = Prophet()
model.add_regressor('marketing_spend')
model.add_regressor('temperature', 
                    prior_scale=0.5,
                    mode='multiplicative')

model.fit(df)

# Important: Future dataframe must include regressors!
future = model.make_future_dataframe(periods=30)
future['marketing_spend'] = future_marketing  # You must provide these
future['temperature'] = future_temp

forecast = model.predict(future)
"""

print(regressor_code)

# ========== CROSS-VALIDATION ==========
print("\n" + "=" * 60)
print("CROSS-VALIDATION")
print("=" * 60)

print("""
Prophet includes time-series cross-validation.

Parameters:
- initial: Training period
- period: Spacing between cutoff dates
- horizon: Forecast horizon
""")

cv_code = """
from prophet.diagnostics import cross_validation, performance_metrics

# Cross-validation
# - Start with 365 days
# - Add 180 days each cut
# - Forecast 30 days ahead
cv_results = cross_validation(
    model,
    initial='365 days',
    period='180 days',
    horizon='30 days'
)

# Calculate metrics
metrics = performance_metrics(cv_results)
print(metrics[['horizon', 'mse', 'rmse', 'mae', 'mape']])

# Plot cross-validation results
from prophet.plot import plot_cross_validation_metric
fig = plot_cross_validation_metric(cv_results, metric='mape')
"""

print(cv_code)

# ========== MODEL EVALUATION ==========
print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

# Simple evaluation demo
train = df[:-30]  # All but last 30 days
test = df[-30:]   # Last 30 days

# Naive forecast (last value)
naive_pred = np.full(len(test), train['y'].iloc[-1])

# Simple moving average forecast
ma_pred = np.full(len(test), train['y'].rolling(30).mean().iloc[-1])

# Calculate metrics
def calculate_metrics(actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    mse = np.mean((actual - predicted) ** 2)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return {'MAE': mae, 'RMSE': rmse, 'MAPE': mape}

print("\nBaseline Model Comparisons:")
print("\nNaive (Last Value):")
naive_metrics = calculate_metrics(test['y'].values, naive_pred)
for k, v in naive_metrics.items():
    print(f"  {k}: {v:.2f}")

print("\n30-Day Moving Average:")
ma_metrics = calculate_metrics(test['y'].values, ma_pred)
for k, v in ma_metrics.items():
    print(f"  {k}: {v:.2f}")

# ========== COMPLETE PROPHET WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE PROPHET WORKFLOW")
print("=" * 60)

workflow_code = """
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import pandas as pd
import matplotlib.pyplot as plt

# 1. PREPARE DATA
df = pd.read_csv('data.csv')
df['ds'] = pd.to_datetime(df['date'])
df['y'] = df['value']
df = df[['ds', 'y']]

# 2. CONFIGURE MODEL
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    changepoint_prior_scale=0.05,
    seasonality_mode='additive'
)

# Add holidays
model.add_country_holidays(country_name='US')

# Add custom seasonality if needed
model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

# 3. FIT MODEL
model.fit(df)

# 4. MAKE PREDICTIONS
future = model.make_future_dataframe(periods=90)  # 90 days ahead
forecast = model.predict(future)

# 5. VISUALIZE
# Main forecast
fig1 = model.plot(forecast)
plt.title('Forecast')
plt.savefig('forecast.png')

# Components
fig2 = model.plot_components(forecast)
plt.savefig('components.png')

# 6. EVALUATE
cv = cross_validation(model, initial='365 days', 
                      period='180 days', horizon='30 days')
metrics = performance_metrics(cv)
print(metrics[['horizon', 'mape', 'rmse']].head())

# 7. SAVE/LOAD MODEL
import json
with open('model.json', 'w') as f:
    json.dump(model_to_json(model), f)

with open('model.json', 'r') as f:
    model = model_from_json(json.load(f))

# 8. GET FORECAST VALUES
final_forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
final_forecast.to_csv('forecast_results.csv', index=False)
"""

print(workflow_code)

# ========== PROPHET VS OTHER METHODS ==========
print("\n" + "=" * 60)
print("PROPHET VS OTHER METHODS")
print("=" * 60)

print("""
┌─────────────────┬───────────┬──────────┬───────────┐
│     Aspect      │  Prophet  │  ARIMA   │   LSTM    │
├─────────────────┼───────────┼──────────┼───────────┤
│ Ease of Use     │ ★★★★★    │ ★★★☆☆   │ ★★☆☆☆    │
│ Missing Data    │ Handles   │ No       │ Needs fix │
│ Multiple Season │ Built-in  │ SARIMA   │ Manual    │
│ Holidays        │ Built-in  │ Manual   │ Manual    │
│ Interpretability│ High      │ Medium   │ Low       │
│ Non-linear      │ Limited   │ No       │ Yes       │
│ Data Required   │ Medium    │ Small    │ Large     │
│ Training Speed  │ Fast      │ Fast     │ Slow      │
└─────────────────┴───────────┴──────────┴───────────┘

Use Prophet when:
✅ Business forecasting
✅ Clear seasonalities
✅ Holiday effects matter
✅ Need quick results
✅ Interpretability important

Consider alternatives when:
❌ Very complex non-linear patterns
❌ Sub-hourly data (too granular)
❌ Real-time predictions needed
❌ Minimal seasonality
""")

# ========== COMMON ISSUES ==========
print("\n" + "=" * 60)
print("COMMON ISSUES AND SOLUTIONS")
print("=" * 60)

print("""
1. FLAT FORECAST
   Problem: Prediction is a flat line
   Solution: 
   - Increase changepoint_prior_scale
   - Check if data has sufficient variation
   - Ensure dates are parsed correctly

2. OVERFITTING
   Problem: Fits training data too well, poor validation
   Solution:
   - Decrease changepoint_prior_scale
   - Decrease seasonality_prior_scale
   - Use cross-validation

3. POOR SEASONALITY
   Problem: Seasonality doesn't match patterns
   Solution:
   - Try multiplicative seasonality
   - Add custom seasonality
   - Increase fourier_order

4. INSTALLATION ISSUES
   Problem: Prophet install fails
   Solution:
   # Install dependencies first
   pip install pystan==2.19.1.1
   pip install prophet

5. MEMORY ERRORS
   Problem: Large datasets cause memory issues
   Solution:
   - Aggregate data (daily instead of hourly)
   - Sample data for prototyping
   - Use mcmc_samples=0 (MAP estimation)
""")

print("\n" + "=" * 60)
print("✅ Prophet Library - Complete!")
print("=" * 60)
