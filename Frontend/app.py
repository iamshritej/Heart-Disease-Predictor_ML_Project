import streamlit as st
import requests

st.title("❤️ Heart Disease Predictor")

st.write("Enter patient details:")

# Input fields (based on dataset)
age = st.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol Level", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (1 = Yes, 0 = No)", [0, 1])
restecg = st.selectbox("Rest ECG (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.number_input("ST Depression (Oldpeak)", value=1.0)
slope = st.selectbox("Slope of Peak Exercise (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0-3)", [0, 1, 2, 3])

# Convert categorical input
sex = 1 if sex == "Male" else 0

features = [
    age, sex, cp, trestbps, chol, fbs,
    restecg, thalach, exang, oldpeak,
    slope, ca, thal
]

if st.button("Predict"):
    response = requests.post(
        "https://heart-disease-api-wqg9.onrender.com/predict",
        json={"features": features}
    )

    result = response.json()

    if result['prediction'] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease")
st.write("Model Accuracy: ~85%")