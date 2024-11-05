# Import Necessary Libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import warnings

# Suppress any warning messages for a cleaner output
warnings.filterwarnings("ignore")

# Define the dynamic file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/cleaned_flight_data.csv")  # Adjusted to be relative to the script's location

# Load and preprocess dataset
def load_dataset(file_path=DATA_PATH):
    # Load dataset
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
    # Filter and normalize dataset
    df = df[df['Airline'] != 'All Airlines']
    df['Airline'] = df['Airline'].replace({
        'virgin Australia': 'Virgin Australia',
        'QantasLink': 'Qantas Link',
        'Rex Airlines': 'Regional Express',
        'Tiger Air': 'Tigerair Australia'
    })
    df['Delayed'] = np.where(df['Departures Delayed'] > 0, 1, 0)
    df['Month'] = pd.to_numeric(df['Month'], errors='coerce').fillna(0).astype(int)
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
    return df

# Train and save model and encoder
def train_and_save_model(df):
    # OneHotEncoder setup
    categorical_features = ['Airline', 'Departing Port', 'Arriving Port']
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    encoded_features = pd.DataFrame(
        encoder.fit_transform(df[categorical_features]),
        columns=encoder.get_feature_names_out(categorical_features),
        index=df.index
    )
    
    # Prepare features and target
    X = pd.concat([df[['Month', 'Year']], encoded_features], axis=1)
    y = df['Delayed']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    
    # Save model and encoder in a 'trained_models' directory
    model_dir = os.path.join(BASE_DIR, "trained_models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(rf_model, os.path.join(model_dir, 'flight_delay_model.pkl'))
    joblib.dump(encoder, os.path.join(model_dir, 'encoder.pkl'))
    print("Model and encoder saved successfully.")

    return rf_model, encoder

# Main function to run the training and save process
def main():
    df = load_dataset()
    model, encoder = train_and_save_model(df)
    print("Training completed and models are saved.")

if __name__ == "__main__":
    main()
