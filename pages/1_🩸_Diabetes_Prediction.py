import streamlit as st
import joblib
import numpy as np
from reports.generate_report import create_pdf

# Load the trained model
model = joblib.load("models/diabetes_model.pkl")

st.title("🩸 Diabetes Prediction")
if "name" in st.session_state:
    st.success(f"Patient: {st.session_state['name']}")

st.write("Enter the patient's health details below.")

# Input fields
pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose Level", 0, 300, 120)
blood_pressure = st.number_input("Blood Pressure", 0, 200, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=st.session_state.get("age", 30)
)

# Prediction
if st.button("🔍 Predict"):

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)
    st.session_state["prediction"] = prediction
    st.session_state["probability"] = probability

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")

    if prediction[0] == 1:
        result = "High Risk of Diabetes"
    else:
        result = "Low Risk of Diabetes"

    st.session_state["diabetes_result"] = result

    st.subheader("Prediction Confidence")
    st.progress(float(probability[0][prediction[0]]))

    st.write(
        f"Confidence: **{probability[0][prediction[0]]*100:.2f}%**"
    )

    st.subheader("Health Recommendation")

    if prediction[0] == 1:
        st.warning("""
- Consult a doctor.
- Reduce sugar intake.
- Exercise regularly.
- Maintain a healthy weight.
- Monitor blood glucose regularly.
        """)
    else:
        st.success("""
- Continue a healthy lifestyle.
- Eat a balanced diet.
- Exercise regularly.
- Get regular health checkups.
        """)

if "prediction" in st.session_state:

    if st.button("📄 Generate PDF Report"):

        prediction = st.session_state["prediction"]
        probability = st.session_state["probability"]

        if prediction[0] == 1:
            result = "High Risk of Diabetes"
            recommendation = "Consult a doctor, exercise regularly, reduce sugar intake."
        else:
            result = "Low Risk of Diabetes"
            recommendation = "Maintain a healthy lifestyle and regular exercise."

        pdf_path = create_pdf(
            st.session_state.get("name", "Unknown"),
            st.session_state.get("age", "N/A"),
            st.session_state.get("gender", "N/A"),
            result,
            f"{probability[0][prediction[0]]*100:.2f}%",
            recommendation
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                "⬇ Download Health Report",
                pdf_file,
                file_name="Health_Report.pdf",
                mime="application/pdf"
            )