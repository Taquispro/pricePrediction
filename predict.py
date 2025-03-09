import pandas as pd
import joblib

# Load the trained model and scaler
rf_model = joblib.load("rf_model5.pkl")
scaler = joblib.load("scaler5.pkl")
features = joblib.load("features5.pkl")

def predict_price(area, bhk, distance, amenities, balconies):
    new_house = pd.DataFrame([[area, bhk, distance, amenities, balconies]], columns=features)
    new_house_scaled = scaler.transform(new_house)
    predicted_price = rf_model.predict(new_house_scaled)[0]
    return predicted_price
