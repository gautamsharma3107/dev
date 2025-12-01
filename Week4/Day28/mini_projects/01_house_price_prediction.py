"""
MINI PROJECT 1: House Price Prediction
========================================
Day 28: Week 4 Mini-Project

Complete end-to-end ML project for predicting house prices.
This project demonstrates the full ML pipeline from data to predictions.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("MINI PROJECT: HOUSE PRICE PREDICTION")
print("=" * 70)

# ============================================================
# STEP 1: DATA GENERATION/LOADING
# ============================================================

print("\n" + "=" * 50)
print("STEP 1: DATA GENERATION")
print("=" * 50)

# Generate synthetic housing dataset
np.random.seed(42)
n_samples = 2000

# Generate features
data = {
    'square_feet': np.random.randint(800, 5000, n_samples),
    'bedrooms': np.random.randint(1, 7, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples),
    'age_years': np.random.randint(0, 80, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples).round(2),
    'garage_spaces': np.random.randint(0, 4, n_samples),
    'has_pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
    'has_garden': np.random.choice([0, 1], n_samples, p=[0.5, 0.5]),
    'floor_count': np.random.randint(1, 4, n_samples),
    'neighborhood': np.random.choice(['Downtown', 'Suburb', 'Rural', 'Urban'], n_samples)
}

# Generate target with realistic relationships
price = (
    data['square_feet'] * 150 +
    data['bedrooms'] * 20000 +
    data['bathrooms'] * 15000 -
    data['age_years'] * 1000 +
    data['location_score'] * 8000 +
    data['garage_spaces'] * 12000 +
    data['has_pool'] * 30000 +
    data['has_garden'] * 15000 +
    data['floor_count'] * 10000 +
    np.random.normal(0, 30000, n_samples)  # Add noise
)

data['price'] = np.maximum(price, 50000).astype(int)  # Ensure minimum price

# Create DataFrame
df = pd.DataFrame(data)

print(f"Dataset created with {len(df)} samples and {len(df.columns)} features")
print(f"\nFeatures: {list(df.columns[:-1])}")
print(f"Target: price")

# ============================================================
# STEP 2: EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("STEP 2: EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Basic statistics
print("\n📊 Dataset Statistics:")
print(df.describe())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Price distribution
print(f"\n💰 Price Statistics:")
print(f"   Min: ${df['price'].min():,}")
print(f"   Max: ${df['price'].max():,}")
print(f"   Mean: ${df['price'].mean():,.0f}")
print(f"   Median: ${df['price'].median():,.0f}")

# ============================================================
# STEP 3: DATA VISUALIZATION
# ============================================================

print("\n" + "=" * 50)
print("STEP 3: DATA VISUALIZATION")
print("=" * 50)

# Create visualization plots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('House Price Dataset - Exploratory Analysis', fontsize=14)

# 1. Price distribution
axes[0, 0].hist(df['price'], bins=30, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 0].set_title('Price Distribution')
axes[0, 0].set_xlabel('Price ($)')
axes[0, 0].set_ylabel('Frequency')

# 2. Price vs Square Feet
axes[0, 1].scatter(df['square_feet'], df['price'], alpha=0.3, color='green')
axes[0, 1].set_title('Price vs Square Feet')
axes[0, 1].set_xlabel('Square Feet')
axes[0, 1].set_ylabel('Price ($)')

# 3. Price vs Location Score
axes[0, 2].scatter(df['location_score'], df['price'], alpha=0.3, color='purple')
axes[0, 2].set_title('Price vs Location Score')
axes[0, 2].set_xlabel('Location Score')
axes[0, 2].set_ylabel('Price ($)')

# 4. Average Price by Bedrooms
avg_price_by_beds = df.groupby('bedrooms')['price'].mean()
axes[1, 0].bar(avg_price_by_beds.index, avg_price_by_beds.values, color='coral', edgecolor='black')
axes[1, 0].set_title('Average Price by Bedrooms')
axes[1, 0].set_xlabel('Bedrooms')
axes[1, 0].set_ylabel('Average Price ($)')

# 5. Price by Neighborhood
df.boxplot(column='price', by='neighborhood', ax=axes[1, 1])
axes[1, 1].set_title('Price by Neighborhood')
axes[1, 1].set_xlabel('Neighborhood')
axes[1, 1].set_ylabel('Price ($)')
plt.suptitle('')

# 6. Correlation heatmap
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', ax=axes[1, 2], cbar_kws={'shrink': 0.8})
axes[1, 2].set_title('Feature Correlations')

plt.tight_layout()
plt.savefig('house_price_eda.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Visualizations saved to 'house_price_eda.png'")

# ============================================================
# STEP 4: DATA PREPROCESSING
# ============================================================

print("\n" + "=" * 50)
print("STEP 4: DATA PREPROCESSING")
print("=" * 50)

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, columns=['neighborhood'], prefix='nbhd')

# Define features and target
feature_columns = [col for col in df_encoded.columns if col != 'price']
X = df_encoded[feature_columns]
y = df_encoded['price']

print(f"Total features after encoding: {len(feature_columns)}")
print(f"Feature names: {feature_columns}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✓ Features scaled using StandardScaler")

# ============================================================
# STEP 5: MODEL TRAINING
# ============================================================

print("\n" + "=" * 50)
print("STEP 5: MODEL TRAINING")
print("=" * 50)

# Define models
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=1.0),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=15, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=42)
}

# Train and evaluate all models
results = []

for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        'Model': name,
        'RMSE': rmse,
        'MAE': mae,
        'R²': r2
    })
    
    print(f"   RMSE: ${rmse:,.0f}")
    print(f"   MAE: ${mae:,.0f}")
    print(f"   R²: {r2:.4f}")

# ============================================================
# STEP 6: MODEL COMPARISON
# ============================================================

print("\n" + "=" * 50)
print("STEP 6: MODEL COMPARISON")
print("=" * 50)

results_df = pd.DataFrame(results).sort_values('R²', ascending=False)
print("\n📊 Model Performance Comparison:")
print(results_df.to_string(index=False))

# Identify best model
best_model_name = results_df.iloc[0]['Model']
best_model = models[best_model_name]
best_r2 = results_df.iloc[0]['R²']

print(f"\n🏆 Best Model: {best_model_name}")
print(f"   R² Score: {best_r2:.4f}")

# ============================================================
# STEP 7: CROSS-VALIDATION
# ============================================================

print("\n" + "=" * 50)
print("STEP 7: CROSS-VALIDATION")
print("=" * 50)

X_scaled = scaler.fit_transform(X)
cv_scores = cross_val_score(best_model, X_scaled, y, cv=5, scoring='r2')

print(f"\n5-Fold Cross-Validation Results for {best_model_name}:")
print(f"   CV Scores: {cv_scores.round(4)}")
print(f"   Mean R²: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# ============================================================
# STEP 8: FEATURE IMPORTANCE
# ============================================================

print("\n" + "=" * 50)
print("STEP 8: FEATURE IMPORTANCE")
print("=" * 50)

if hasattr(best_model, 'feature_importances_'):
    importance_df = pd.DataFrame({
        'Feature': feature_columns,
        'Importance': best_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("\n📈 Top 10 Most Important Features:")
    print(importance_df.head(10).to_string(index=False))
    
    # Plot feature importance
    plt.figure(figsize=(10, 6))
    top_features = importance_df.head(10)
    plt.barh(top_features['Feature'], top_features['Importance'], color='steelblue')
    plt.xlabel('Importance')
    plt.title(f'Top 10 Feature Importances - {best_model_name}')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('house_price_feature_importance.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("\n✓ Feature importance plot saved")

# ============================================================
# STEP 9: SAVE MODEL
# ============================================================

print("\n" + "=" * 50)
print("STEP 9: SAVE MODEL")
print("=" * 50)

# Save model and scaler
joblib.dump(best_model, 'house_price_model.pkl')
joblib.dump(scaler, 'house_price_scaler.pkl')
joblib.dump(feature_columns, 'house_price_features.pkl')

print("✓ Model saved to 'house_price_model.pkl'")
print("✓ Scaler saved to 'house_price_scaler.pkl'")
print("✓ Features saved to 'house_price_features.pkl'")

# ============================================================
# STEP 10: PREDICTION FUNCTION
# ============================================================

print("\n" + "=" * 50)
print("STEP 10: MAKING PREDICTIONS")
print("=" * 50)

def predict_house_price(square_feet, bedrooms, bathrooms, age_years, 
                        location_score, garage_spaces, has_pool, has_garden,
                        floor_count, neighborhood):
    """
    Predict house price based on features.
    """
    # Create feature dictionary
    features = {
        'square_feet': square_feet,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'age_years': age_years,
        'location_score': location_score,
        'garage_spaces': garage_spaces,
        'has_pool': has_pool,
        'has_garden': has_garden,
        'floor_count': floor_count,
        'nbhd_Downtown': 1 if neighborhood == 'Downtown' else 0,
        'nbhd_Rural': 1 if neighborhood == 'Rural' else 0,
        'nbhd_Suburb': 1 if neighborhood == 'Suburb' else 0,
        'nbhd_Urban': 1 if neighborhood == 'Urban' else 0
    }
    
    # Create DataFrame with correct column order
    input_df = pd.DataFrame([features])[feature_columns]
    
    # Scale and predict
    input_scaled = scaler.transform(input_df)
    prediction = best_model.predict(input_scaled)[0]
    
    return prediction

# Example predictions
print("\n🏠 Sample Predictions:")

houses = [
    {'square_feet': 2500, 'bedrooms': 4, 'bathrooms': 3, 'age_years': 5,
     'location_score': 8.5, 'garage_spaces': 2, 'has_pool': 1, 'has_garden': 1,
     'floor_count': 2, 'neighborhood': 'Suburb'},
    {'square_feet': 1200, 'bedrooms': 2, 'bathrooms': 1, 'age_years': 40,
     'location_score': 5.0, 'garage_spaces': 1, 'has_pool': 0, 'has_garden': 0,
     'floor_count': 1, 'neighborhood': 'Urban'},
    {'square_feet': 4000, 'bedrooms': 5, 'bathrooms': 4, 'age_years': 2,
     'location_score': 9.5, 'garage_spaces': 3, 'has_pool': 1, 'has_garden': 1,
     'floor_count': 2, 'neighborhood': 'Downtown'},
]

for i, house in enumerate(houses, 1):
    price = predict_house_price(**house)
    print(f"\n   House {i}:")
    print(f"   - {house['square_feet']} sqft, {house['bedrooms']} bed, {house['bathrooms']} bath")
    print(f"   - {house['neighborhood']}, {house['age_years']} years old")
    print(f"   💰 Predicted Price: ${price:,.0f}")

# ============================================================
# PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print(f"""
✅ Dataset: {len(df)} samples, {len(feature_columns)} features
✅ Best Model: {best_model_name}
✅ R² Score: {best_r2:.4f}
✅ Cross-Validation: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})
✅ Model saved and ready for deployment

Files Created:
- house_price_eda.png (Exploratory Data Analysis plots)
- house_price_feature_importance.png (Feature importance chart)
- house_price_model.pkl (Trained model)
- house_price_scaler.pkl (Feature scaler)
- house_price_features.pkl (Feature names)

This project demonstrates a complete ML pipeline:
1. Data loading/generation
2. Exploratory data analysis
3. Data visualization
4. Data preprocessing
5. Model training
6. Model comparison
7. Cross-validation
8. Feature importance analysis
9. Model saving
10. Making predictions
""")

print("=" * 70)
print("PROJECT COMPLETE! 🎉")
print("=" * 70)
