import pandas as pd
import joblib

# Load the trained model and scaler
rf_model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

def predict_price(area, bhk, distance, amenities, balconies):
    new_house = pd.DataFrame([[area, bhk, distance, amenities, balconies]], columns=features)
    new_house_scaled = scaler.transform(new_house)
    predicted_price = rf_model.predict(new_house_scaled)[0]
    return predicted_price
