!pip install streamlit
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load saved model and scaler
model = joblib.load("xgboost_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Diabetes Prediction App (XGBoost)")

def user_input_features():
    features = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
                'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare',
                'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age',
                'Education', 'Income']
    data = {}
    for feature in features:
        if feature == 'BMI':
            data[feature] = st.slider(feature, 10, 100, 25)
        else:
            data[feature] = st.slider(feature, 0, 10, 1)
    return pd.DataFrame([data])

df = user_input_features()
scaled = scaler.transform(df)
prediction = model.predict(scaled)

st.subheader("Prediction Result")
st.write("Diabetes Class:", int(prediction[0]))
