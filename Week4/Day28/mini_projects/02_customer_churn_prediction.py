"""
MINI PROJECT 2: Customer Churn Prediction (Classification)
===========================================================
Day 28: Week 4 Mini-Project

Complete end-to-end ML project for predicting customer churn.
This project demonstrates classification techniques and evaluation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, classification_report,
                             roc_curve, auc)
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("MINI PROJECT: CUSTOMER CHURN PREDICTION")
print("=" * 70)

# ============================================================
# STEP 1: DATA GENERATION/LOADING
# ============================================================

print("\n" + "=" * 50)
print("STEP 1: DATA GENERATION")
print("=" * 50)

# Generate synthetic customer churn dataset
np.random.seed(42)
n_samples = 3000

# Generate features
data = {
    'tenure_months': np.random.randint(1, 72, n_samples),
    'monthly_charges': np.random.uniform(20, 150, n_samples).round(2),
    'total_charges': np.zeros(n_samples),  # Will calculate
    'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
    'payment_method': np.random.choice(['Electronic', 'Mailed', 'Bank transfer', 'Credit card'], n_samples),
    'internet_service': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples),
    'online_security': np.random.choice([0, 1], n_samples),
    'tech_support': np.random.choice([0, 1], n_samples),
    'streaming_tv': np.random.choice([0, 1], n_samples),
    'paperless_billing': np.random.choice([0, 1], n_samples),
    'senior_citizen': np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
    'partner': np.random.choice([0, 1], n_samples),
    'dependents': np.random.choice([0, 1], n_samples),
    'num_support_tickets': np.random.randint(0, 10, n_samples)
}

# Calculate total charges
data['total_charges'] = (data['tenure_months'] * data['monthly_charges']).round(2)

# Generate churn based on realistic patterns
churn_prob = (
    0.1 +  # Base probability
    0.3 * (data['contract_type'] == 'Month-to-month') +
    0.15 * (data['monthly_charges'] > 80) +
    -0.2 * (data['tenure_months'] > 24) +
    -0.1 * data['online_security'] +
    -0.1 * data['tech_support'] +
    0.1 * data['paperless_billing'] +
    0.05 * data['num_support_tickets'] / 10 +
    np.random.uniform(-0.1, 0.1, n_samples)
)

churn_prob = np.clip(churn_prob, 0, 1)
data['churn'] = (np.random.random(n_samples) < churn_prob).astype(int)

# Create DataFrame
df = pd.DataFrame(data)

print(f"Dataset created with {len(df)} samples")
print(f"\nFeatures: {list(df.columns[:-1])}")
print(f"Target: churn (0 = Stayed, 1 = Churned)")

# ============================================================
# STEP 2: EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("STEP 2: EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Check class distribution
print("\n📊 Churn Distribution:")
churn_counts = df['churn'].value_counts()
print(f"   Stayed (0): {churn_counts[0]} ({churn_counts[0]/len(df)*100:.1f}%)")
print(f"   Churned (1): {churn_counts[1]} ({churn_counts[1]/len(df)*100:.1f}%)")

# Basic statistics
print("\n📈 Numerical Features Summary:")
print(df.describe())

# Churn rate by contract type
print("\n📋 Churn Rate by Contract Type:")
churn_by_contract = df.groupby('contract_type')['churn'].mean()
for contract, rate in churn_by_contract.items():
    print(f"   {contract}: {rate*100:.1f}%")

# ============================================================
# STEP 3: DATA VISUALIZATION
# ============================================================

print("\n" + "=" * 50)
print("STEP 3: DATA VISUALIZATION")
print("=" * 50)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Customer Churn Analysis', fontsize=14)

# 1. Churn distribution
churn_counts.plot(kind='bar', ax=axes[0, 0], color=['green', 'red'], edgecolor='black')
axes[0, 0].set_title('Churn Distribution')
axes[0, 0].set_xlabel('Churn')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_xticklabels(['Stayed', 'Churned'], rotation=0)

# 2. Churn by Contract Type
churn_by_contract.plot(kind='bar', ax=axes[0, 1], color='coral', edgecolor='black')
axes[0, 1].set_title('Churn Rate by Contract Type')
axes[0, 1].set_xlabel('Contract Type')
axes[0, 1].set_ylabel('Churn Rate')
axes[0, 1].set_xticklabels(churn_by_contract.index, rotation=45)

# 3. Monthly Charges by Churn
df.boxplot(column='monthly_charges', by='churn', ax=axes[0, 2])
axes[0, 2].set_title('Monthly Charges by Churn Status')
axes[0, 2].set_xlabel('Churn')
axes[0, 2].set_ylabel('Monthly Charges ($)')
plt.suptitle('')

# 4. Tenure by Churn
df.boxplot(column='tenure_months', by='churn', ax=axes[1, 0])
axes[1, 0].set_title('Tenure by Churn Status')
axes[1, 0].set_xlabel('Churn')
axes[1, 0].set_ylabel('Tenure (months)')
plt.suptitle('')

# 5. Churn by Internet Service
churn_by_internet = df.groupby('internet_service')['churn'].mean()
churn_by_internet.plot(kind='bar', ax=axes[1, 1], color='steelblue', edgecolor='black')
axes[1, 1].set_title('Churn Rate by Internet Service')
axes[1, 1].set_xlabel('Internet Service')
axes[1, 1].set_ylabel('Churn Rate')
axes[1, 1].set_xticklabels(churn_by_internet.index, rotation=45)

# 6. Correlation heatmap
numeric_df = df.select_dtypes(include=[np.number])
corr_with_churn = numeric_df.corr()['churn'].drop('churn').sort_values()
corr_with_churn.plot(kind='barh', ax=axes[1, 2], color='purple')
axes[1, 2].set_title('Correlation with Churn')
axes[1, 2].set_xlabel('Correlation')

plt.tight_layout()
plt.savefig('customer_churn_eda.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Visualizations saved to 'customer_churn_eda.png'")

# ============================================================
# STEP 4: DATA PREPROCESSING
# ============================================================

print("\n" + "=" * 50)
print("STEP 4: DATA PREPROCESSING")
print("=" * 50)

# Encode categorical variables
df_encoded = pd.get_dummies(df, columns=['contract_type', 'payment_method', 'internet_service'])

# Define features and target
feature_columns = [col for col in df_encoded.columns if col != 'churn']
X = df_encoded[feature_columns]
y = df_encoded['churn']

print(f"Total features after encoding: {len(feature_columns)}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Churn rate in train: {y_train.mean()*100:.1f}%")
print(f"Churn rate in test: {y_test.mean()*100:.1f}%")

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
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=10, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
}

# Train and evaluate all models
results = []

for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1
    })
    
    print(f"   Accuracy: {acc:.4f}")
    print(f"   Precision: {prec:.4f}")
    print(f"   Recall: {rec:.4f}")
    print(f"   F1-Score: {f1:.4f}")

# ============================================================
# STEP 6: MODEL COMPARISON
# ============================================================

print("\n" + "=" * 50)
print("STEP 6: MODEL COMPARISON")
print("=" * 50)

results_df = pd.DataFrame(results).sort_values('F1-Score', ascending=False)
print("\n📊 Model Performance Comparison:")
print(results_df.to_string(index=False))

# Identify best model
best_model_name = results_df.iloc[0]['Model']
best_model = models[best_model_name]
best_f1 = results_df.iloc[0]['F1-Score']

print(f"\n🏆 Best Model: {best_model_name}")
print(f"   F1-Score: {best_f1:.4f}")

# ============================================================
# STEP 7: DETAILED EVALUATION OF BEST MODEL
# ============================================================

print("\n" + "=" * 50)
print("STEP 7: DETAILED EVALUATION")
print("=" * 50)

# Get predictions from best model
y_pred = best_model.predict(X_test_scaled)
y_pred_proba = best_model.predict_proba(X_test_scaled)[:, 1]

# Confusion Matrix
print("\n📊 Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"   True Negatives: {cm[0, 0]}")
print(f"   False Positives: {cm[0, 1]}")
print(f"   False Negatives: {cm[1, 0]}")
print(f"   True Positives: {cm[1, 1]}")

# Classification Report
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Stayed', 'Churned']))

# Plot confusion matrix and ROC curve
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Confusion Matrix heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['Stayed', 'Churned'],
            yticklabels=['Stayed', 'Churned'])
axes[0].set_title(f'Confusion Matrix - {best_model_name}')
axes[0].set_xlabel('Predicted')
axes[0].set_ylabel('Actual')

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

axes[1].plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
axes[1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
axes[1].set_xlim([0.0, 1.0])
axes[1].set_ylim([0.0, 1.05])
axes[1].set_xlabel('False Positive Rate')
axes[1].set_ylabel('True Positive Rate')
axes[1].set_title(f'ROC Curve - {best_model_name}')
axes[1].legend(loc='lower right')

plt.tight_layout()
plt.savefig('customer_churn_evaluation.png', dpi=100, bbox_inches='tight')
plt.close()
print("\n✓ Evaluation plots saved to 'customer_churn_evaluation.png'")

print(f"\n📈 ROC-AUC Score: {roc_auc:.4f}")

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

# ============================================================
# STEP 9: CROSS-VALIDATION
# ============================================================

print("\n" + "=" * 50)
print("STEP 9: CROSS-VALIDATION")
print("=" * 50)

X_scaled = scaler.fit_transform(X)
cv_scores = cross_val_score(best_model, X_scaled, y, cv=5, scoring='f1')

print(f"\n5-Fold Cross-Validation Results for {best_model_name}:")
print(f"   CV Scores: {cv_scores.round(4)}")
print(f"   Mean F1: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# ============================================================
# STEP 10: SAVE MODEL
# ============================================================

print("\n" + "=" * 50)
print("STEP 10: SAVE MODEL")
print("=" * 50)

joblib.dump(best_model, 'churn_model.pkl')
joblib.dump(scaler, 'churn_scaler.pkl')
joblib.dump(feature_columns, 'churn_features.pkl')

print("✓ Model saved to 'churn_model.pkl'")
print("✓ Scaler saved to 'churn_scaler.pkl'")
print("✓ Features saved to 'churn_features.pkl'")

# ============================================================
# STEP 11: PREDICTION FUNCTION
# ============================================================

print("\n" + "=" * 50)
print("STEP 11: MAKING PREDICTIONS")
print("=" * 50)

def predict_churn(customer_data):
    """
    Predict churn probability for a customer.
    """
    # Create one-hot encoded features
    df_temp = pd.DataFrame([customer_data])
    df_encoded = pd.get_dummies(df_temp)
    
    # Ensure all columns are present
    for col in feature_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    
    # Reorder columns
    input_df = df_encoded[feature_columns]
    
    # Scale and predict
    input_scaled = scaler.transform(input_df)
    prediction = best_model.predict(input_scaled)[0]
    probability = best_model.predict_proba(input_scaled)[0][1]
    
    return prediction, probability

# Example predictions
print("\n👥 Sample Customer Predictions:")

customers = [
    {
        'tenure_months': 2, 'monthly_charges': 90, 'total_charges': 180,
        'contract_type': 'Month-to-month', 'payment_method': 'Electronic',
        'internet_service': 'Fiber optic', 'online_security': 0, 'tech_support': 0,
        'streaming_tv': 1, 'paperless_billing': 1, 'senior_citizen': 0,
        'partner': 0, 'dependents': 0, 'num_support_tickets': 5
    },
    {
        'tenure_months': 48, 'monthly_charges': 60, 'total_charges': 2880,
        'contract_type': 'Two year', 'payment_method': 'Bank transfer',
        'internet_service': 'DSL', 'online_security': 1, 'tech_support': 1,
        'streaming_tv': 0, 'paperless_billing': 0, 'senior_citizen': 0,
        'partner': 1, 'dependents': 1, 'num_support_tickets': 1
    },
]

for i, customer in enumerate(customers, 1):
    prediction, probability = predict_churn(customer)
    status = "🔴 HIGH RISK" if prediction == 1 else "🟢 LOW RISK"
    print(f"\n   Customer {i}: {status}")
    print(f"   - Tenure: {customer['tenure_months']} months")
    print(f"   - Contract: {customer['contract_type']}")
    print(f"   - Monthly Charges: ${customer['monthly_charges']}")
    print(f"   - Churn Probability: {probability*100:.1f}%")

# ============================================================
# PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print(f"""
✅ Dataset: {len(df)} customers
✅ Churn Rate: {df['churn'].mean()*100:.1f}%
✅ Best Model: {best_model_name}
✅ F1-Score: {best_f1:.4f}
✅ ROC-AUC: {roc_auc:.4f}
✅ Model saved and ready for deployment

Files Created:
- customer_churn_eda.png (Exploratory Data Analysis plots)
- customer_churn_evaluation.png (Confusion matrix & ROC curve)
- churn_model.pkl (Trained model)
- churn_scaler.pkl (Feature scaler)
- churn_features.pkl (Feature names)

Business Insights:
- Month-to-month contracts have highest churn rate
- Longer tenure customers are more loyal
- Technical support and online security reduce churn
- Higher monthly charges correlate with higher churn

Recommendations:
1. Offer incentives for long-term contracts
2. Improve technical support availability
3. Monitor high-risk customers proactively
4. Create retention campaigns for new customers
""")

print("=" * 70)
print("PROJECT COMPLETE! 🎉")
print("=" * 70)
