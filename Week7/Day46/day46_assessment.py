"""
DAY 46 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 46 ASSESSMENT - Time Series Basics")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What are the four main components of a time series?
a) Mean, Median, Mode, Range
b) Trend, Seasonality, Cyclical, Residual
c) Input, Output, Hidden, Bias
d) AR, I, MA, SARIMA

Your answer: """)

print("""
Q2. In ARIMA(p, d, q), what does 'd' represent?
a) The number of autoregressive terms
b) The degree of differencing
c) The number of moving average terms
d) The daily seasonality period

Your answer: """)

print("""
Q3. What is the correct data format for Prophet?
a) Columns named 'date' and 'value'
b) Columns named 'ds' and 'y'
c) Columns named 'timestamp' and 'target'
d) Any column names work

Your answer: """)

print("""
Q4. Why is stationarity important in time series analysis?
a) It makes the data smaller
b) Most forecasting models assume constant statistical properties
c) It removes all patterns from the data
d) It is required only for neural networks

Your answer: """)

print("""
Q5. What is the input shape for LSTM in time series?
a) (features, samples)
b) (samples, features)
c) (samples, timesteps, features)
d) (timesteps, features, samples)

Your answer: """)

print("""
Q6. What does ADF test check for in time series?
a) Autocorrelation
b) Stationarity
c) Seasonality
d) Trend direction

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to create sequences for LSTM from
    a time series. Given data and window_size, return X, y arrays.
    
    Example: data = [1,2,3,4,5], window_size = 2
    Should return: X = [[1,2], [2,3], [3,4]], y = [3,4,5]
""")

# Write your code here:




print("""
Q8. (2 points) Write code to calculate MAPE (Mean Absolute 
    Percentage Error) between actual and predicted values.
    Handle division by zero.
""")

# Write your code here:




print("""
Q9. (2 points) Write code to perform first-order differencing
    on a pandas Series to make it stationary.
    Return the differenced series without NaN values.
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Compare and contrast ARIMA and LSTM for time 
     series forecasting. When would you choose one over the other?
     
Your answer:
""")

# Write your explanation here as comments:
# 




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) Trend, Seasonality, Cyclical, Residual
Q2: b) The degree of differencing
Q3: b) Columns named 'ds' and 'y'
Q4: b) Most forecasting models assume constant statistical properties
Q5: c) (samples, timesteps, features)
Q6: b) Stationarity

Section B:
Q7:
import numpy as np

def create_sequences(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size])
    return np.array(X), np.array(y)

# Test
data = [1, 2, 3, 4, 5]
X, y = create_sequences(data, 2)
print(f"X: {X}")  # [[1, 2], [2, 3], [3, 4]]
print(f"y: {y}")  # [3, 4, 5]

Q8:
import numpy as np

def calculate_mape(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    
    # Handle division by zero
    non_zero = actual != 0
    if not np.any(non_zero):
        return float('inf')
    
    mape = np.mean(np.abs((actual[non_zero] - predicted[non_zero]) 
                          / actual[non_zero])) * 100
    return mape

# Test
actual = [100, 150, 200]
predicted = [110, 140, 220]
print(f"MAPE: {calculate_mape(actual, predicted):.2f}%")  # ~8.33%

Q9:
import pandas as pd

def difference_series(series):
    '''First-order differencing to make series stationary'''
    # Difference: Y_t - Y_{t-1}
    differenced = series.diff()
    # Remove NaN from first position
    return differenced.dropna()

# Test
data = pd.Series([10, 15, 25, 40, 60])
diff = difference_series(data)
print(diff)  # 5, 10, 15, 20

Section C:
Q10:
ARIMA:
- Best for linear patterns and simple trends
- Works with small datasets (100+ samples)
- Fast training, interpretable
- Requires stationarity
- Good for quick prototyping

LSTM:
- Best for complex, non-linear patterns
- Needs large datasets (1000+ samples)
- Captures long-term dependencies
- No stationarity requirement
- Better for multivariate forecasting

Choose ARIMA when:
- Small dataset
- Need interpretability
- Simple patterns
- Quick results needed

Choose LSTM when:
- Large dataset available
- Complex non-linear patterns
- Multiple features to consider
- ARIMA doesn't provide enough accuracy
"""
