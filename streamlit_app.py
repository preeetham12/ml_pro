import streamlit as st
import requests

# Streamlit App UI
st.title("Breast Cancer Classification")
st.write("This app interacts with a deployed model to classify breast cancer.")

# Input Features
age = st.slider("Age (Years)", 0, 100, 30)
menopause = st.selectbox("Menopause Stage", ["premeno", "ge40", "lt40"])
tumor_size = st.slider("Tumor Size (in mm)", 0, 100, 20)
node_caps = st.selectbox("Node Caps", ["no", "yes"])
breast = st.selectbox("Breast Side", ["left", "right"])
breast_quad = st.selectbox("Breast Quadrant", ["left-up", "left-low", "right-up", "right-low", "central"])

# API URL
api_url = "http://127.0.0.1:8000/predict"

# Prediction
if st.button("Classify"):
    st.write("Sending data to the server...")
    try:
        payload = {
            "age": age,
            "menopause": menopause,
            "tumor_size": tumor_size,
            "node_caps": node_caps,
            "breast": breast,
            "breast_quad": breast_quad,
        }
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            prediction = response.json().get("prediction", "Error")
            st.success(f"The predicted class is: {prediction}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
