import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Title and description
st.title("💰 Salary Prediction App")
st.write(
    "This app predicts an employee's **salary** based on their "
    "**years of experience**, using a Linear Regression model trained "
    "on historical salary data."
)

st.divider()

# Sidebar - dataset info
with st.sidebar:
    st.header("About")
    st.write(
        "This app uses a simple Linear Regression model trained on a "
        "Years of Experience vs Salary dataset."
    )
    st.subheader("Model Performance")
    try:
        with open("metrics.txt") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.write("Metrics not available.")

    st.subheader("Dataset Preview")
    try:
        df = pd.read_csv("salary_data.csv")
        st.dataframe(df.head())
    except FileNotFoundError:
        st.write("Dataset not found.")

# Main input
st.subheader("Enter Years of Experience")
years_experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=3.0,
    step=0.1,
    help="Enter a number between 0 and 50 years."
)

# Prediction history (session-based)
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Predict Salary", type="primary"):
    input_df = pd.DataFrame({"YearsExperience": [years_experience]})
    prediction = model.predict(input_df)[0]
    prediction = max(prediction, 0)

    st.success(f"### Predicted Salary: ${prediction:,.2f}")

    st.session_state.history.append(
        {"Years of Experience": years_experience, "Predicted Salary": f"${prediction:,.2f}"}
    )

# Show prediction history
if st.session_state.history:
    st.subheader("Prediction History")
    st.table(pd.DataFrame(st.session_state.history))

st.divider()
st.caption("Built with Streamlit · Model: Linear Regression · Dataset: Salary Dataset")
