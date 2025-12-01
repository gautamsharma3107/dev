"""
PREDICTIONS - End-to-End ML Project
=====================================
Day 28: Week 4 Mini-Project

Simple script for making predictions with trained models.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("PREDICTIONS - ML Project Pipeline")
print("=" * 60)

# ============================================================
# 1. Load or Train Model
# ============================================================

print("\n1. LOADING/TRAINING MODEL")
print("-" * 40)

# Try to load saved model, or train new one
try:
    model = joblib.load('best_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("✓ Loaded saved model and scaler")
except FileNotFoundError:
    print("Training new model...")
    
    # Create and train model
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'square_feet': np.random.randint(500, 5000, n_samples),
        'bedrooms': np.random.randint(1, 7, n_samples),
        'bathrooms': np.random.randint(1, 5, n_samples),
        'age_years': np.random.randint(0, 100, n_samples),
        'location_score': np.random.uniform(1, 10, n_samples).round(2),
        'garage_spaces': np.random.randint(0, 4, n_samples),
        'has_pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    }
    
    price = (
        data['square_feet'] * 100 +
        data['bedrooms'] * 15000 +
        data['bathrooms'] * 10000 -
        data['age_years'] * 500 +
        data['location_score'] * 5000 +
        data['garage_spaces'] * 8000 +
        data['has_pool'] * 20000 +
        np.random.normal(0, 20000, n_samples)
    )
    data['price'] = price.astype(int)
    
    df = pd.DataFrame(data)
    
    feature_columns = ['square_feet', 'bedrooms', 'bathrooms', 'age_years',
                       'location_score', 'garage_spaces', 'has_pool']
    
    X = df[feature_columns]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Save model and scaler
    joblib.dump(model, 'best_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    
    print("✓ New model trained and saved")

# ============================================================
# 2. Define Prediction Function
# ============================================================

print("\n2. PREDICTION FUNCTION")
print("-" * 40)

def predict_price(square_feet, bedrooms, bathrooms, age_years, 
                  location_score, garage_spaces, has_pool):
    """
    Predict house price based on features.
    
    Parameters:
    -----------
    square_feet : int - House size in square feet
    bedrooms : int - Number of bedrooms
    bathrooms : int - Number of bathrooms
    age_years : int - Age of the house in years
    location_score : float - Location score (1-10)
    garage_spaces : int - Number of garage spaces
    has_pool : int - 1 if has pool, 0 otherwise
    
    Returns:
    --------
    float : Predicted price
    """
    # Create feature array
    features = np.array([[square_feet, bedrooms, bathrooms, age_years,
                          location_score, garage_spaces, has_pool]])
    
    # Scale features
    features_scaled = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    
    return prediction

print("predict_price() function defined!")

# ============================================================
# 3. Single Prediction Example
# ============================================================

print("\n3. SINGLE PREDICTION EXAMPLE")
print("-" * 40)

# Example house
example_house = {
    'square_feet': 2500,
    'bedrooms': 4,
    'bathrooms': 3,
    'age_years': 10,
    'location_score': 8.5,
    'garage_spaces': 2,
    'has_pool': 1
}

predicted_price = predict_price(**example_house)

print("\nHouse Features:")
for key, value in example_house.items():
    print(f"  {key}: {value}")

print(f"\n💰 Predicted Price: ${predicted_price:,.2f}")

# ============================================================
# 4. Batch Predictions
# ============================================================

print("\n4. BATCH PREDICTIONS")
print("-" * 40)

# Multiple houses
houses = pd.DataFrame([
    {'square_feet': 1500, 'bedrooms': 2, 'bathrooms': 1, 'age_years': 30, 
     'location_score': 5.0, 'garage_spaces': 1, 'has_pool': 0},
    {'square_feet': 2000, 'bedrooms': 3, 'bathrooms': 2, 'age_years': 15, 
     'location_score': 7.0, 'garage_spaces': 2, 'has_pool': 0},
    {'square_feet': 3000, 'bedrooms': 4, 'bathrooms': 3, 'age_years': 5, 
     'location_score': 8.0, 'garage_spaces': 2, 'has_pool': 1},
    {'square_feet': 4000, 'bedrooms': 5, 'bathrooms': 4, 'age_years': 2, 
     'location_score': 9.0, 'garage_spaces': 3, 'has_pool': 1},
])

# Scale all features
features_scaled = scaler.transform(houses)

# Predict all at once
predictions = model.predict(features_scaled)

# Add predictions to dataframe
houses['predicted_price'] = predictions

print("\nBatch Predictions:")
print(houses.to_string(index=False))

# ============================================================
# 5. Interactive Prediction
# ============================================================

print("\n5. INTERACTIVE PREDICTION")
print("-" * 40)

def get_user_prediction():
    """Get house features from user and make prediction."""
    print("\nEnter house features for prediction:")
    
    try:
        square_feet = int(input("  Square feet: "))
        bedrooms = int(input("  Bedrooms: "))
        bathrooms = int(input("  Bathrooms: "))
        age_years = int(input("  Age (years): "))
        location_score = float(input("  Location score (1-10): "))
        garage_spaces = int(input("  Garage spaces: "))
        has_pool = int(input("  Has pool (0 or 1): "))
        
        price = predict_price(square_feet, bedrooms, bathrooms, age_years,
                              location_score, garage_spaces, has_pool)
        
        print(f"\n💰 Predicted Price: ${price:,.2f}")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Uncomment to run interactive prediction:
# get_user_prediction()

print("Interactive prediction function ready!")
print("(Uncomment get_user_prediction() to use)")

# ============================================================
# 6. Prediction with Confidence Interval
# ============================================================

print("\n6. PREDICTION WITH CONFIDENCE")
print("-" * 40)

def predict_with_confidence(square_feet, bedrooms, bathrooms, age_years,
                             location_score, garage_spaces, has_pool):
    """
    Make prediction with confidence interval using Random Forest.
    """
    features = np.array([[square_feet, bedrooms, bathrooms, age_years,
                          location_score, garage_spaces, has_pool]])
    features_scaled = scaler.transform(features)
    
    # Get predictions from all trees
    predictions_all_trees = []
    for tree in model.estimators_:
        pred = tree.predict(features_scaled)[0]
        predictions_all_trees.append(pred)
    
    predictions_all_trees = np.array(predictions_all_trees)
    
    # Calculate statistics
    mean_pred = predictions_all_trees.mean()
    std_pred = predictions_all_trees.std()
    lower_bound = mean_pred - 1.96 * std_pred
    upper_bound = mean_pred + 1.96 * std_pred
    
    return {
        'prediction': mean_pred,
        'std': std_pred,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound
    }

# Example with confidence
result = predict_with_confidence(**example_house)

print("\nPrediction with 95% Confidence Interval:")
print(f"  Predicted Price: ${result['prediction']:,.2f}")
print(f"  Standard Deviation: ${result['std']:,.2f}")
print(f"  95% CI: [${result['lower_bound']:,.2f}, ${result['upper_bound']:,.2f}]")

# ============================================================
# 7. Save Predictions
# ============================================================

print("\n7. SAVE PREDICTIONS")
print("-" * 40)

# Save batch predictions
houses.to_csv('predictions_output.csv', index=False)
print("Predictions saved to 'predictions_output.csv'")

# ============================================================
# 8. Prediction Pipeline Summary
# ============================================================

print("\n8. PREDICTION PIPELINE SUMMARY")
print("-" * 40)

print("""
Complete ML Prediction Pipeline:
================================

1. Load Model:
   - model = joblib.load('best_model.pkl')
   - scaler = joblib.load('scaler.pkl')

2. Prepare Features:
   - Create feature array in correct order
   - Scale features using saved scaler

3. Make Prediction:
   - prediction = model.predict(features_scaled)

4. Post-process (optional):
   - Add confidence intervals
   - Round to appropriate precision
   - Convert to business format

5. Save/Display Results:
   - Save to CSV/database
   - Display to user
   - Log for monitoring
""")

# ============================================================
# EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
1. Create a prediction API:
   - Build a Flask/FastAPI endpoint
   - Accept JSON input with features
   - Return predicted price

2. Add input validation:
   - Check for valid ranges
   - Handle missing values
   - Return helpful error messages

3. Create a simple web interface:
   - Form to input features
   - Display prediction results
   - Show confidence interval

4. Implement batch prediction from file:
   - Read houses from CSV
   - Make predictions for all
   - Save results to new CSV

5. Add prediction logging:
   - Log all predictions with timestamp
   - Track model performance over time
""")

# ============================================================
# KEY TAKEAWAYS
# ============================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Save trained models using joblib/pickle
✅ Create reusable prediction functions
✅ Always scale input features the same way
✅ Handle single and batch predictions
✅ Add confidence intervals when possible
✅ Validate input data before prediction
✅ Log predictions for monitoring
✅ Build APIs for production deployment
""")
