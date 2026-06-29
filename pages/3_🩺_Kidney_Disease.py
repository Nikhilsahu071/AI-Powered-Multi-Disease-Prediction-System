import streamlit as st
import joblib
import numpy as np
from reports.generate_report import create_pdf

# Load trained model
model = joblib.load("models/kidney_model.pkl")

st.title("🩺 Kidney Disease Prediction")

# ---------------- Patient Details ----------------

if "name" in st.session_state:
    st.success(f"👤 Patient: {st.session_state['name']}")

age = st.session_state.get("age", 30)
gender = st.session_state.get("gender", "Not Available")

st.write(f"**Age:** {age}")
st.write(f"**Gender:** {gender}")

st.markdown("---")

st.subheader("Enter Health Details")

bp = st.number_input(
    "Blood Pressure",
    min_value=50,
    max_value=250,
    value=80
)

sg = st.number_input(
    "Specific Gravity",
    min_value=1.000,
    max_value=1.030,
    value=1.020,
    format="%.3f"
)

al = st.number_input(
    "Albumin",
    min_value=0,
    max_value=5,
    value=0
)

su = st.number_input(
    "Sugar",
    min_value=0,
    max_value=5,
    value=0
)

bgr = st.number_input(
    "Blood Glucose Random",
    min_value=50,
    max_value=500,
    value=120
)

bu = st.number_input(
    "Blood Urea",
    min_value=1,
    max_value=300,
    value=40
)

sc = st.number_input(
    "Serum Creatinine",
    min_value=0.1,
    max_value=20.0,
    value=1.2
)

hemo = st.number_input(
    "Hemoglobin",
    min_value=3.0,
    max_value=20.0,
    value=15.0
)

# ---------------- Prediction ----------------

if st.button("🩺 Predict Kidney Disease"):

    input_data = np.array([[
        age,
        bp,
        sg,
        al,
        su,
        bgr,
        bu,
        sc,
        hemo
    ]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:

        st.error("⚠ High Risk of Kidney Disease")

        recommendation = """
• Consult a nephrologist.
• Drink plenty of water.
• Reduce salt intake.
• Control blood pressure.
• Get regular kidney tests.
"""

        result = "High Risk of Kidney Disease"

    else:

        st.success("✅ Low Risk of Kidney Disease")

        recommendation = """
• Continue healthy eating.
• Stay hydrated.
• Exercise regularly.
• Maintain normal blood pressure.
"""

        result = "Low Risk of Kidney Disease"

    st.session_state["kidney_result"] = result
    
    st.subheader("Prediction Confidence")

    st.progress(float(probability[0][prediction[0]]))

    st.write(
        f"Confidence: **{probability[0][prediction[0]]*100:.2f}%**"
    )

    st.subheader("Health Recommendation")

    st.info(recommendation)

    # ---------------- PDF ----------------

    if st.button("📄 Generate Kidney Report"):

        pdf_path = create_pdf(
            st.session_state.get("name", "Unknown"),
            st.session_state.get("age", "N/A"),
            st.session_state.get("gender", "N/A"),
            result,
            f"{probability[0][prediction[0]]*100:.2f}%",
            recommendation
        )

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                "⬇ Download Kidney Report",
                pdf,
                file_name="Kidney_Report.pdf",
                mime="application/pdf"
            )