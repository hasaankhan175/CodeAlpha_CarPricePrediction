import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("car_price_model.pkl")

st.set_page_config(page_title="Car Price Predictor", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Enter car details to predict selling price")

# ---------------- INPUTS ---------------- #

car_age = st.number_input("Car Age (Years)", min_value=0, max_value=50, value=5)

present_price = st.number_input("Present Price (in lakhs)", value=10.0)

driven_kms = st.number_input("Driven Kilometers", value=35000)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}

selling_type = st.selectbox("Selling Type", ["Dealer", "Individual"])
selling_map = {"Dealer": 1, "Individual": 0}

transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
trans_map = {"Manual": 0, "Automatic": 1}

owner = st.selectbox("Number of Owners", [0, 1, 3])

# ---------------- PREDICTION ---------------- #

if st.button("Predict Price"):
    input_data = np.array([[
        car_age,
        present_price,
        driven_kms,
        fuel_map[fuel_type],
        selling_map[selling_type],
        trans_map[transmission],
        owner
    ]])

    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Selling Price: {prediction[0]:.2f} lakhs")
