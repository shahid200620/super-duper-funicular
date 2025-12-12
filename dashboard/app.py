import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

ROOT = r'C:\Users\mdsha\super-duper-funicular'

MODEL_PATH = ROOT + r'\models\final_model.pkl'
DATA_PATH = ROOT + r'\data\health_data_cleaned.csv'
COST_SUMMARY = ROOT + r'\reports\cost_summary.csv'
IMPORTANCE_PATH = ROOT + r'\reports\permutation_importance_full.csv'

st.title("Healthcare Outcome Predictor Dashboard")

# Load model and data
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)
X = df.drop(columns=['outcome'])

# Sidebar: patient selector
st.sidebar.header("Pick a patient")
index = st.sidebar.number_input("Patient index", 0, len(X)-1, 0)

patient = X.iloc[[index]]
st.write("### Selected Patient Details")
st.write(patient.T)

if st.button("Predict"):
    prob = model.predict_proba(patient)[0,1]
    recommended = "A" if prob >= 0.5 else "B"
    treatment_costs = {'A':2500, 'B':1000}
    hospital_cost = 15000
    expected_cost = treatment_costs[recommended] + (1-prob)*hospital_cost

    st.write("### Prediction Results")
    st.write("**Probability of positive outcome:**", round(prob,3))
    st.write("**Recommended treatment:**", recommended)
    st.write("**Expected patient cost:**", round(expected_cost,2))

# Global Feature Importance
if os.path.exists(IMPORTANCE_PATH):
    st.write("### Top Important Features")
    imp = pd.read_csv(IMPORTANCE_PATH).head(10)
    st.table(imp[['feature','importance_mean']])
else:
    st.write("Run interpretability notebook first.")

# Cost Summary
if os.path.exists(COST_SUMMARY):
    st.write("### Cost Summary")
    cs = pd.read_csv(COST_SUMMARY, index_col=0)
    st.write(cs)
