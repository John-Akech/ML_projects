# app.py

import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("sonar_rf_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Sonar Rock vs Mine Classifier")

# 60 input fields
inputs = []
for i in range(60):
    val = st.number_input(f"Feature {i+1}", key=f"feature_{i}")
    inputs.append(val)

if st.button("Predict"):
    features = np.array(inputs).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    label = "Mine" if prediction[0] == 1 else "Rock"
    st.success(f"The object is predicted to be a: **{label}**")
