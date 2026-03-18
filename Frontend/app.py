import streamlit as st
import requests

st.title("ML Prediction App")

input1 = st.number_input("Enter value 1")
input2 = st.number_input("Enter value 2")
input3 = st.number_input("Enter value 3")
input4 = st.number_input("Enter value 4")

if st.button("Predict"):
    url = "https://capstone-project-1-0icy.onrender.com/predict"

    data = {
        "data": [input1, input2, input3, input4]
    }

    try:
        response = requests.post(url, json=data)  # ✅ IMPORTANT

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result}")
        else:
            st.error(f"Error: {response.text}")

    except:
        st.error("Error connecting to API")