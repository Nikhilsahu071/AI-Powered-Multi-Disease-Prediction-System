import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Health Dashboard", page_icon="📊", layout="wide")

st.title("🏥 AI Healthcare Dashboard")
st.markdown("---")

# ==========================
# Patient Information
# ==========================

st.subheader("👤 Patient Profile")

name = st.session_state.get("name", "Not Available")
age = st.session_state.get("age", "Not Available")
gender = st.session_state.get("gender", "Not Available")

c1, c2, c3 = st.columns(3)

c1.metric("Patient", name)
c2.metric("Age", age)
c3.metric("Gender", gender)

st.markdown("---")

# ==========================
# Disease Results
# ==========================

st.subheader("🩺 Disease Prediction Summary")

diabetes = st.session_state.get("diabetes_result", "Not Tested")
heart = st.session_state.get("heart_result", "Not Tested")
kidney = st.session_state.get("kidney_result", "Not Tested")
liver = st.session_state.get("liver_result", "Not Tested")

col1, col2 = st.columns(2)

with col1:
    st.info(f"🩸 Diabetes : {diabetes}")
    st.info(f"❤️ Heart : {heart}")

with col2:
    st.info(f"🩺 Kidney : {kidney}")
    st.info(f"🧬 Liver : {liver}")

st.markdown("---")

# ==========================
# Overall Health Score
# ==========================

score = 100

for result in [diabetes, heart, kidney, liver]:
    if "High Risk" in str(result):
        score -= 25
    elif "Not Tested" in str(result):
        score -= 10

st.subheader("❤️ Overall Health Score")

st.progress(score / 100)

st.metric("Health Score", f"{score}%")

st.markdown("---")

# ==========================
# Charts
# ==========================

completed = sum(
    result != "Not Tested"
    for result in [diabetes, heart, kidney, liver]
)

pending = 4 - completed

pie = px.pie(
    values=[completed, pending],
    names=["Completed", "Pending"],
    title="Prediction Modules"
)

st.plotly_chart(pie, use_container_width=True)

status = pd.DataFrame({
    "Disease": ["Diabetes", "Heart", "Kidney", "Liver"],
    "Completed": [
        1 if diabetes != "Not Tested" else 0,
        1 if heart != "Not Tested" else 0,
        1 if kidney != "Not Tested" else 0,
        1 if liver != "Not Tested" else 0
    ]
})

bar = px.bar(
    status,
    x="Disease",
    y="Completed",
    color="Disease",
    title="Completed Predictions"
)

st.plotly_chart(bar, use_container_width=True)

st.markdown("---")

st.success("🎉 Dashboard Loaded Successfully")