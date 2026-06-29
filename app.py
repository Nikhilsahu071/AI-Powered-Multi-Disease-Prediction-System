import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI-Powered Multi Disease Prediction System",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.stApp{
    background:#F4F7FC;
}

.hero{

background:linear-gradient(90deg,#1565C0,#42A5F5);

padding:40px;

border-radius:20px;

color:white;

}

.hero h1{

color:white;

font-size:42px;

}

.hero p{

font-size:18px;

color:white;

}

div[data-testid="metric-container"]{
    background:#FFFFFF !important;
    border:1px solid #D1D5DB;
    border-radius:15px;
    padding:15px;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
}

div[data-testid="stMetricLabel"]{
    color:#1F2937 !important;
    font-weight:600;
}

div[data-testid="stMetricValue"]{
    color:#1565C0 !important;
    font-weight:700;
}
            
.feature-card{

background:white;

padding:25px;

border-radius:15px;

box-shadow:0px 3px 10px rgba(0,0,0,.08);

margin-bottom:15px;

color:#1F2937;

}

            .stMarkdown{
    color:#1F2937 !important;
}

p{
    color:#1F2937 !important;
}

label{
    color:#1F2937 !important;
}

h1,h2,h3,h4,h5{
    color:#0F172A !important;
}

div[data-testid="stMetricValue"]{
    color:#1565C0 !important;
}

div[data-testid="stMetricLabel"]{
    color:#1F2937 !important;
}
            
            h1,h2,h3,h4,h5,h6{
    color:#111827 !important;
}

p{
    color:#374151 !important;
}

[data-testid="stMarkdownContainer"]{
    color:#374151 !important;
}
            
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    logo = Path("images/hospital_logo.png")

    if logo.exists():
        st.image(str(logo), width=120)

    st.title("🏥 AI Health")

    st.caption("AI-Powered Healthcare")

    st.divider()

    st.success("🤖 Machine Learning Enabled")

    st.info("""
Supported Diseases

🩸 Diabetes

❤️ Heart

🩺 Kidney

🧬 Liver
""")

    st.divider()

    st.write("Version 1.0")

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""

<div class="hero">

<h1>

🏥 AI-Powered Multi Disease Prediction System

</h1>

<p>

Advanced Healthcare Diagnosis using Machine Learning

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# SYSTEM STATISTICS
# ==========================================================

st.markdown("""
<h2 style="
color:#0F172A;
font-size:32px;
font-weight:bold;
margin-bottom:20px;
">
📊 System Statistics
</h2>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="🩺 Disease Models",
        value="4"
    )

with c2:
    st.metric(
        label="🤖 ML Models",
        value="4"
    )

with c3:
    st.metric(
        label="📄 PDF Reports",
        value="Available"
    )

with c4:
    st.metric(
        label="🟢 Status",
        value="Active"
    )

st.write("")
st.write("")

# ==========================================================
# DISEASE MODULES
# ==========================================================

st.markdown("""
<h2 style="
color:#0F172A;
font-size:32px;
font-weight:bold;
margin-bottom:20px;
">
🩺 Disease Prediction Modules
</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ---------------- Diabetes ----------------

with col1:

    with st.container(border=True):

        st.subheader("🩸 Diabetes Prediction")

        st.write(
            "Predict diabetes risk using Machine Learning."
        )

        if st.button(
            "Open Diabetes Module",
            use_container_width=True
        ):
            st.switch_page(
                "pages/1_🩸_Diabetes_Prediction.py"
            )

# ---------------- Heart ----------------

with col2:

    with st.container(border=True):

        st.subheader("❤️ Heart Disease")

        st.write(
            "Predict heart disease using clinical data."
        )

        if st.button(
            "Open Heart Module",
            use_container_width=True
        ):
            st.switch_page(
                "pages/2_❤️_Heart_Disease.py"
            )

st.write("")

col3, col4 = st.columns(2)

# ---------------- Kidney ----------------

with col3:

    with st.container(border=True):

        st.subheader("🩺 Kidney Disease")

        st.write(
            "Predict kidney disease using laboratory values."
        )

        if st.button(
            "Open Kidney Module",
            use_container_width=True
        ):
            st.switch_page(
                "pages/3_🩺_Kidney_Disease.py"
            )

# ---------------- Liver ----------------

with col4:

    with st.container(border=True):

        st.subheader("🧬 Liver Disease")

        st.write(
            "Predict liver disease using AI models."
        )

        if st.button(
            "Open Liver Module",
            use_container_width=True
        ):
            st.switch_page(
                "pages/4_🧬_Liver_Disease.py"
            )

st.write("")
st.write("")

# ==========================================================
# FEATURES
# ==========================================================

st.divider()

st.header("⭐ Key Features")

f1, f2 = st.columns(2)

with f1:

    st.success("✔ Diabetes Prediction")

    st.success("✔ Heart Disease Prediction")

    st.success("✔ Kidney Disease Prediction")

    st.success("✔ Liver Disease Prediction")

with f2:

    st.success("✔ Interactive Dashboard")

    st.success("✔ PDF Report Generation")

    st.success("✔ Confidence Score")

    st.success("✔ Health Recommendation")


# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.divider()

st.header("📖 Project Overview")

st.write("""

The **AI-Powered Multi Disease Prediction System** is a Machine Learning
based healthcare application developed using **Python** and **Streamlit**.

It helps users predict the risk of multiple diseases based on medical
parameters and generates a professional PDF health report.

### Supported Diseases

- 🩸 Diabetes
- ❤️ Heart Disease
- 🩺 Kidney Disease
- 🧬 Liver Disease

### Main Objectives

- Early Disease Prediction
- AI Assisted Healthcare
- User Friendly Interface
- Medical Report Generation

""")
