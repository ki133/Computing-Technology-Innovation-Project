# Import Necessary Libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/Cleaned_Done_price_dataset.csv")
MODEL_DIR = os.path.join(BASE_DIR, "trained_models")
MODEL_PATH = os.path.join(MODEL_DIR, "price_model.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "price_encoder.pkl")

# Load dataset
def load_dataset(file_path=DATA_PATH):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
    return df

# Preprocess data
def preprocess_data(df):
    X = df[['Year', 'Month', 'Port1', 'Port2', 'Route']]
    y = df['$Real']
    X_encoded = pd.get_dummies(X, columns=['Port1', 'Port2', 'Route'])
    print("Data preprocessed successfully.")
    return X_encoded, y

# Train models and save the best one
def train_and_save_model(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    rf_model = RandomForestRegressor()
    rf_model.fit(X_train, y_train)

    # Evaluate model
    y_pred = rf_model.predict(X_test)
    print("Random Forest Regressor Performance:")
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Save model and encoder structure
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(rf_model, MODEL_PATH)
    joblib.dump(X.columns, ENCODER_PATH)  # Save columns used for encoding
    print("Model and encoder saved successfully.")

# Main function
def main():
    df = load_dataset()
    X, y = preprocess_data(df)
    train_and_save_model(X, y)

if __name__ == "__main__":
    main()
