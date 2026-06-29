import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/heart_model.pkl")

st.title("❤️ Heart Disease Prediction")

# Show patient details
if "name" in st.session_state:
    st.success(f"👤 Patient: {st.session_state['name']}")

age = st.session_state.get("age", 30)
gender = st.session_state.get("gender", "Male")

st.write(f"**Age:** {age}")
st.write(f"**Gender:** {gender}")

# Input fields
sex = st.selectbox("Sex", [0, 1], help="0 = Female, 1 = Male")

cp = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3]
)

trestbps = st.number_input(
    "Resting Blood Pressure",
    80,
    220,
    120
)

chol = st.number_input(
    "Cholesterol",
    100,
    600,
    200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1]
)

restecg = st.selectbox(
    "Resting ECG",
    [0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1]
)

oldpeak = st.number_input(
    "Oldpeak",
    0.0,
    10.0,
    1.0
)
slope = st.selectbox("Slope", [0, 1, 2])

ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])

thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

if st.button("❤️ Predict Heart Disease"):

    input_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
        recommendation = """
• Consult a cardiologist.
• Reduce cholesterol.
• Exercise regularly.
• Avoid smoking and alcohol.
"""
        result = "High Risk of Heart Disease"

    else:
        st.success("✅ Low Risk of Heart Disease")
        recommendation = """
• Maintain a healthy lifestyle.
• Exercise regularly.
• Eat a balanced diet.
"""
        result = "Low Risk of Heart Disease"

    st.session_state["heart_result"] = result

    st.subheader("Prediction Confidence")

    st.progress(float(probability[0][prediction[0]]))

    st.write(
        f"Confidence: **{probability[0][prediction[0]]*100:.2f}%**"
    )

    st.subheader("Health Recommendation")

    st.info(recommendation)