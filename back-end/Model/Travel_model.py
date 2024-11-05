# Import Necessary Libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import joblib

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/travel_dataset.xlsx")
MODEL_DIR = os.path.join(BASE_DIR, "trained_models")
MODEL_PATH = os.path.join(MODEL_DIR, "travel_price_model.pkl")

# Load dataset
def load_dataset(file_path=DATA_PATH):
    df = pd.read_excel(file_path)
    print("Dataset loaded successfully.")
    return df

# Preprocess data
def preprocess_data(df):
    # Define the relevant features and target
    features = [
        'Year', 'Month', 'Hours flown', 'Aircraft km flown', 'Aircraft departures',
        'Total rev pax (U/D)', 'Freight tonnes (U/D)', 'Mail tonnes (U/D)',
        'Total rev pax (TOB)', 'Freight tonnes (TOB)', 'Mail tonnes (TOB)',
        'Total RPK', 'Pax tonne km', 'Freight tonne km', 'Mail tonne km',
        'Total tonne km', 'Available seat km', 'Available tonne km', 'Available seats',
        'Pax load factor %', 'Weight load factor %', 'Total pax'
    ]
    target = 'Total pax'
    
    # Filter rows with complete data in selected features and target
    df_filtered = df.dropna(subset=features + [target])

    # Convert relevant columns to numerical data types
    df_filtered['Month'] = pd.to_numeric(df_filtered['Month'], errors='coerce').fillna(0).astype(int)
    df_filtered['Year'] = pd.to_numeric(df_filtered['Year'], errors='coerce').fillna(0).astype(int)
    
    # Ensure other features are of correct data types if necessary
    X = df_filtered[features]
    y = df_filtered[target]
    
    print("Data preprocessed successfully.")
    return X, y

# Train model and save it
def train_and_save_model(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost model with categorical support
    model = xgb.XGBRegressor(enable_categorical=True)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print("XGBoost Regressor Performance:")
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Save the model
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print("Model saved successfully.")

# Main function
def main():
    df = load_dataset()
    X, y = preprocess_data(df)
    train_and_save_model(X, y)

if __name__ == "__main__":
    main()
