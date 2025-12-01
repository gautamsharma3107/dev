"""
Day 30 - Mini Project: Simple Neural Network on Tabular Data
=============================================================
Build a complete neural network to predict whether a customer will churn.

This project covers:
1. Data loading and preprocessing
2. Building a neural network
3. Training with callbacks
4. Evaluation and prediction
5. Model saving
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# Set seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

print("=" * 70)
print("MINI PROJECT: Customer Churn Prediction Neural Network")
print("=" * 70)

# ========== STEP 1: CREATE SYNTHETIC CUSTOMER DATA ==========
print("\n" + "=" * 70)
print("STEP 1: Creating Synthetic Customer Data")
print("=" * 70)

# Generate synthetic customer data
n_samples = 2000

# Create features
np.random.seed(42)
data = {
    'tenure': np.random.randint(1, 72, n_samples),  # Months as customer
    'monthly_charges': np.random.uniform(20, 100, n_samples),
    'total_charges': np.random.uniform(100, 8000, n_samples),
    'num_support_tickets': np.random.randint(0, 10, n_samples),
    'num_products': np.random.randint(1, 5, n_samples),
    'contract_length': np.random.choice([1, 12, 24], n_samples),  # Months
    'age': np.random.randint(18, 80, n_samples),
    'is_senior': np.random.choice([0, 1], n_samples),
    'has_partner': np.random.choice([0, 1], n_samples),
    'has_dependents': np.random.choice([0, 1], n_samples),
}

# Create DataFrame
df = pd.DataFrame(data)

# Create target variable (churn) based on features
# Higher churn probability for: short tenure, high charges, many support tickets, short contract
churn_probability = (
    (df['tenure'] < 12).astype(int) * 0.2 +
    (df['monthly_charges'] > 70).astype(int) * 0.15 +
    (df['num_support_tickets'] > 5).astype(int) * 0.25 +
    (df['contract_length'] == 1).astype(int) * 0.2 +
    np.random.uniform(0, 0.2, n_samples)
)
df['churn'] = (churn_probability > 0.4).astype(int)

print(f"Dataset shape: {df.shape}")
print(f"\nFeature columns: {list(df.columns[:-1])}")
print(f"Target column: churn")
print(f"\nClass distribution:")
print(df['churn'].value_counts())
print(f"\nSample data:")
print(df.head())

# ========== STEP 2: DATA PREPROCESSING ==========
print("\n" + "=" * 70)
print("STEP 2: Data Preprocessing")
print("=" * 70)

# Separate features and target
X = df.drop('churn', axis=1).values
y = df['churn'].values

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split data
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

print(f"\nTraining samples: {len(X_train)}")
print(f"Validation samples: {len(X_val)}")
print(f"Test samples: {len(X_test)}")

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

print("\n✅ Data scaled (StandardScaler)")

# ========== STEP 3: BUILD THE NEURAL NETWORK ==========
print("\n" + "=" * 70)
print("STEP 3: Building the Neural Network")
print("=" * 70)

# Define model architecture
model = Sequential([
    # Input layer
    Dense(64, activation='relu', input_shape=(X_train.shape[1],), name='input_layer'),
    BatchNormalization(),
    Dropout(0.3),
    
    # Hidden layers
    Dense(32, activation='relu', name='hidden_1'),
    BatchNormalization(),
    Dropout(0.2),
    
    Dense(16, activation='relu', name='hidden_2'),
    Dropout(0.1),
    
    # Output layer
    Dense(1, activation='sigmoid', name='output')
], name='churn_predictor')

print("Model Architecture:")
model.summary()

# ========== STEP 4: COMPILE THE MODEL ==========
print("\n" + "=" * 70)
print("STEP 4: Compiling the Model")
print("=" * 70)

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("✅ Model compiled")
print(f"   Optimizer: Adam (lr=0.001)")
print(f"   Loss: binary_crossentropy")
print(f"   Metrics: accuracy")

# ========== STEP 5: SET UP CALLBACKS ==========
print("\n" + "=" * 70)
print("STEP 5: Setting Up Callbacks")
print("=" * 70)

# Early stopping
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True,
    verbose=1
)

print("✅ EarlyStopping configured")
print("   - Monitor: val_loss")
print("   - Patience: 10 epochs")
print("   - Restore best weights: True")

# ========== STEP 6: TRAIN THE MODEL ==========
print("\n" + "=" * 70)
print("STEP 6: Training the Model")
print("=" * 70)

print("\nTraining started...\n")

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[early_stopping],
    verbose=1
)

print(f"\n✅ Training complete!")
print(f"   Epochs run: {len(history.history['loss'])}")

# ========== STEP 7: EVALUATE THE MODEL ==========
print("\n" + "=" * 70)
print("STEP 7: Evaluating the Model")
print("=" * 70)

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)

print(f"\nTest Results:")
print(f"   Loss: {test_loss:.4f}")
print(f"   Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# Get predictions
y_pred_prob = model.predict(X_test, verbose=0)
y_pred = (y_pred_prob > 0.5).astype(int).flatten()

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))

# Confusion matrix
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# ========== STEP 8: MAKE PREDICTIONS ON NEW DATA ==========
print("\n" + "=" * 70)
print("STEP 8: Making Predictions on New Customers")
print("=" * 70)

# Simulate new customer data
new_customers = pd.DataFrame({
    'tenure': [3, 48, 12],
    'monthly_charges': [85, 45, 70],
    'total_charges': [255, 2160, 840],
    'num_support_tickets': [7, 1, 3],
    'num_products': [1, 3, 2],
    'contract_length': [1, 24, 12],
    'age': [25, 55, 35],
    'is_senior': [0, 0, 0],
    'has_partner': [0, 1, 1],
    'has_dependents': [0, 1, 0]
})

print("New Customers:")
print(new_customers)

# Scale and predict
new_customers_scaled = scaler.transform(new_customers.values)
predictions = model.predict(new_customers_scaled, verbose=0)

print("\nChurn Predictions:")
for i, (prob, pred) in enumerate(zip(predictions.flatten(), (predictions > 0.5).astype(int).flatten())):
    risk = "HIGH RISK" if pred == 1 else "Low Risk"
    print(f"   Customer {i+1}: {prob:.4f} probability → {risk}")

# ========== STEP 9: SAVE THE MODEL ==========
print("\n" + "=" * 70)
print("STEP 9: Saving the Model")
print("=" * 70)

# Save model (using current directory for cross-platform compatibility)
import os
save_dir = './saved_models'
os.makedirs(save_dir, exist_ok=True)

model.save(f'{save_dir}/churn_predictor.keras')
print(f"✅ Model saved to '{save_dir}/churn_predictor.keras'")

# Save scaler for production use
import pickle
with open(f'{save_dir}/churn_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print(f"✅ Scaler saved to '{save_dir}/churn_scaler.pkl'")

# ========== PROJECT SUMMARY ==========
print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print(f"""
Dataset:
   - {n_samples} synthetic customer records
   - 10 features (tenure, charges, support tickets, etc.)
   - Binary target: churn (0/1)

Model Architecture:
   - Input: 10 features
   - Hidden: 64 → 32 → 16 neurons with ReLU
   - Regularization: BatchNorm + Dropout
   - Output: 1 neuron with Sigmoid

Training:
   - Optimizer: Adam (lr=0.001)
   - Loss: Binary Crossentropy
   - Early stopping after {len(history.history['loss'])} epochs

Results:
   - Test Accuracy: {test_accuracy*100:.2f}%
   - Test Loss: {test_loss:.4f}

Files Saved:
   - Model: ./saved_models/churn_predictor.keras
   - Scaler: ./saved_models/churn_scaler.pkl
""")

print("=" * 70)
print("🎉 CONGRATULATIONS! You've completed the Day 30 Mini-Project!")
print("=" * 70)
print("""
What you learned:
✅ Creating synthetic data for ML
✅ Data preprocessing and scaling
✅ Building a neural network for classification
✅ Using callbacks (EarlyStopping)
✅ Model evaluation and metrics
✅ Making predictions on new data
✅ Saving models for production

Next Steps:
- Try different architectures (more/fewer layers)
- Experiment with hyperparameters
- Use real datasets (Kaggle has many!)
- Add more callbacks (ModelCheckpoint, LearningRateScheduler)
""")
