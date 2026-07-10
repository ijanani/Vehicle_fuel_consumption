import streamlit as st
import pandas as pd
   
from feature_engineering import FeatureEngineer

import joblib

model = joblib.load("fuel_model.pkl")
preprocessing = joblib.load("preprocessing.pkl")

# Load model and preprocessing pipeline
model = joblib.load("fuel_model.pkl")
preprocessing = joblib.load("preprocessing.pkl")

# -----------------------------
# Page
# -----------------------------
st.set_page_config(page_title="Vehicle Fuel Consumption Predictor")

st.title("🚗 Vehicle Fuel Consumption Predictor")
st.write("Enter your vehicle details below.")

# -----------------------------
# User Inputs
# -----------------------------
vehicle_year = st.number_input(
    "Vehicle Year",
    min_value=1980,
    max_value=2026,
    value=2020
)

cc_rating = st.number_input(
    "Engine Size (cc)",
    min_value=500,
    max_value=8000,
    value=2000
)

gross_vehicle_mass = st.number_input(
    "Gross vehicle mass (kg)",
    min_value=500,
    max_value=80000,
    value=2000
)

body_type = st.selectbox(
    "Body Type",
    [   'UTILITY',         'LIGHT VAN',     'STATION WAGON',
         'HATCHBACK',        'SPORTS CAR',            'SALOON',
         'HEAVY VAN',       'CONVERTIBLE',           'MINIBUS',
   'FLAT-DECK TRUCK',       'OTHER TRUCK',
     'SERVICE COACH', 'ARTICULATED TRUCK']
)

motive_power = st.selectbox(
    "Motive Power",
    [ 'PETROL' , 'DIESEL' , 'PETROL HYBRID', 'PLUGIN PETROL HYBRID' ,'DIESEL HYBRID']
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Fuel Consumption"):

    input_df = pd.DataFrame({
        "VEHICLE_YEAR": [vehicle_year],
        "CC_RATING": [cc_rating],
        "GROSS_VEHICLE_MASS": [gross_vehicle_mass],
        "BODY_TYPE": [body_type],
        "MOTIVE_POWER": [motive_power]
    })

    processed = preprocessing.transform(input_df)

    prediction = model.predict(processed)[0]

    st.success(
        f"Predicted Fuel Consumption: {prediction:.2f} L/100 km"
    )

    emission_factor = {
        "PETROL": 2.36,
        "DIESEL": 2.67,
    }

    if motive_power in emission_factor:
        estimated_co2 = prediction * emission_factor[motive_power]

        st.info(
            f"Estimated CO₂ Emissions: {estimated_co2:.2f} kg CO₂-e/100 km"
        )