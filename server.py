from flask import Flask, jsonify  # ❌ Remove requests from here
from flask_cors import CORS
import requests  # ✅ Import separately
from predict import predict_price

app = Flask(__name__)
CORS(app)

BASE_URL = "https://major-estate.onrender.com/api/listing/get/"  # Your frontend API URL

@app.route('/predict/<listing_id>', methods=['GET'])
def get_price(listing_id):
    try:
        # Fetch listing data from frontend API
        response = requests.get(f"{BASE_URL}{listing_id}")

        # If request fails, return an error
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch listing data"}), response.status_code

        # Extract relevant data from API response
        data = response.json()
        print(data)
        area = data.get("area", 0)  # Default to 0 if missing
        bhk = data.get("bedrooms", 0)
        distance = data.get("distance", 0)
        amenities = data.get("ameneties", 0)
        balconies = data.get("balconies", 0)

        # Validate data
        if None in [area, bhk, distance, amenities, balconies]:
            return jsonify({"error": "Missing required fields"}), 400

        # Call prediction function
        predicted_price = predict_price(area, bhk, distance, amenities, balconies)

        return jsonify(predicted_price)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)  # Run on all network interfaces

