import streamlit as st
import joblib
import numpy as np
from reports.generate_report import create_pdf

# Load model
model = joblib.load("models/liver_model.pkl")

st.title("🧬 Liver Disease Prediction")

# ---------------- Patient Details ----------------

if "name" in st.session_state:
    st.success(f"👤 Patient: {st.session_state['name']}")

age = st.session_state.get("age", 30)
gender_text = st.session_state.get("gender", "Male")

# Convert gender for model
gender = 1 if gender_text.lower() == "male" else 0

st.write(f"**Age:** {age}")
st.write(f"**Gender:** {gender_text}")

st.markdown("---")

st.subheader("Enter Liver Test Details")

tb = st.number_input("Total Bilirubin", 0.1, 50.0, 1.0)

db = st.number_input("Direct Bilirubin", 0.1, 30.0, 0.3)

alp = st.number_input("Alkaline Phosphotase", 50, 2500, 200)

alt = st.number_input("Alamine Aminotransferase (ALT)", 5, 2000, 30)

ast = st.number_input("Aspartate Aminotransferase (AST)", 5, 2000, 35)

tp = st.number_input("Total Proteins", 2.0, 10.0, 6.5)

albumin = st.number_input("Albumin", 1.0, 6.0, 3.5)

agr = st.number_input("Albumin & Globulin Ratio", 0.1, 3.0, 1.0)

# ---------------- Prediction ----------------

if st.button("🧬 Predict Liver Disease"):

    input_data = np.array([[
        age,
        gender,
        tb,
        db,
        alp,
        alt,
        ast,
        tp,
        albumin,
        agr
    ]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:

        st.error("⚠ High Risk of Liver Disease")

        recommendation = """
• Consult a liver specialist.
• Avoid alcohol.
• Eat a healthy diet.
• Get liver function tests regularly.
"""

        result = "High Risk of Liver Disease"

    else:

        st.success("✅ Low Risk of Liver Disease")

        recommendation = """
• Maintain a balanced diet.
• Exercise regularly.
• Avoid excessive alcohol.
"""

        result = "Low Risk of Liver Disease"

    st.session_state["liver_result"] = result

    st.subheader("Prediction Confidence")

    confidence = probability[0][prediction[0]]

    st.progress(float(confidence))

    st.write(f"Confidence: **{confidence*100:.2f}%**")

    st.subheader("Health Recommendation")

    st.info(recommendation)

    # PDF Report
    if st.button("📄 Generate Liver Report"):

        pdf_path = create_pdf(
            st.session_state.get("name", "Unknown"),
            st.session_state.get("age", "N/A"),
            st.session_state.get("gender", "N/A"),
            result,
            f"{confidence*100:.2f}%",
            recommendation
        )

        with open(pdf_path, "rb") as pdf:
            st.download_button(
                "⬇ Download Liver Report",
                pdf,
                file_name="Liver_Report.pdf",
                mime="application/pdf"
            )