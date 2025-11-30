# Day 46 Quick Reference Cheat Sheet

## Time Series Components
```
Y(t) = Trend + Seasonality + Cyclical + Noise

- Trend: Long-term direction
- Seasonality: Regular patterns (daily, weekly, yearly)
- Cyclical: Non-fixed period patterns
- Noise: Random variations
```

## Stationarity
```python
# Check stationarity with ADF test
from statsmodels.tsa.stattools import adfuller

result = adfuller(series)
if result[1] < 0.05:
    print("Stationary")  # Reject null hypothesis
else:
    print("Non-stationary")

# Make stationary with differencing
differenced = series.diff().dropna()
```

## ARIMA Model
```python
from statsmodels.tsa.arima.model import ARIMA

# ARIMA(p, d, q)
# p = AR order (PACF cutoff)
# d = differencing (usually 0-2)
# q = MA order (ACF cutoff)

model = ARIMA(data, order=(1, 1, 1))
results = model.fit()

# Forecast
forecast = results.forecast(steps=10)
print(results.summary())
```

## SARIMA (Seasonal)
```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# SARIMA(p,d,q)(P,D,Q,s)
model = SARIMAX(data, 
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12))  # monthly
results = model.fit()
```

## Auto ARIMA
```python
from pmdarima import auto_arima

model = auto_arima(data,
                   start_p=0, max_p=5,
                   start_q=0, max_q=5,
                   seasonal=True,
                   m=12,
                   trace=True)
forecast = model.predict(n_periods=10)
```

## LSTM Data Preparation
```python
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# 1. Scale data
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data.reshape(-1, 1))

# 2. Create sequences
def create_sequences(data, window):
    X, y = [], []
    for i in range(len(data) - window):
        X.append(data[i:i+window])
        y.append(data[i+window])
    return np.array(X), np.array(y)

X, y = create_sequences(scaled, window_size=10)

# 3. Reshape for LSTM: (samples, timesteps, features)
X = X.reshape(X.shape[0], X.shape[1], 1)
```

## LSTM Model
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(window, 1)),
    Dropout(0.2),
    LSTM(32),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32,
          validation_split=0.1)

# Predict
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)
```

## Prophet
```python
from prophet import Prophet

# Data format: columns 'ds' (datetime) and 'y' (value)
df = pd.DataFrame({'ds': dates, 'y': values})

# Fit
model = Prophet(yearly_seasonality=True,
                weekly_seasonality=True)
model.add_country_holidays(country_name='US')
model.fit(df)

# Forecast
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot
model.plot(forecast)
model.plot_components(forecast)
```

## Evaluation Metrics
```python
import numpy as np

def evaluate(actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    mse = np.mean((actual - predicted) ** 2)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return {'MAE': mae, 'RMSE': rmse, 'MAPE': mape}
```

## Time Series Train-Test Split
```python
# NEVER use random split!
# Always preserve time order

train_size = int(len(data) * 0.8)
train = data[:train_size]
test = data[train_size:]
```

## Rolling Window
```python
# Moving averages
df['MA_7'] = df['value'].rolling(window=7).mean()
df['MA_30'] = df['value'].rolling(window=30).mean()

# Rolling statistics
df['rolling_std'] = df['value'].rolling(window=30).std()
```

## Resampling
```python
# Downsample
weekly = df.resample('W').mean()
monthly = df.resample('M').sum()

# Upsample (requires interpolation)
hourly = df.resample('H').interpolate()
```

## Quick Comparison

| Model | Data Size | Complexity | Speed | Best For |
|-------|-----------|------------|-------|----------|
| ARIMA | Small | Linear | Fast | Simple patterns |
| LSTM | Large | Non-linear| Slow | Complex patterns |
| Prophet | Medium | Multiple seasonality | Fast | Business forecasting |

## Common Patterns

```python
# ACF/PACF interpretation
# ACF decays slowly → Non-stationary or AR
# ACF cuts off → MA process
# PACF cuts off → AR process

# Model selection
# AR(p): PACF cuts off at lag p
# MA(q): ACF cuts off at lag q
# ARMA(p,q): Both decay gradually
```

---
**Keep this handy for Day 46 topics!** 🚀
