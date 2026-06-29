import streamlit as st

st.title("👤 Patient Information")

name = st.text_input("Patient Name")

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=st.session_state.get("age", 25)
)


phone = st.text_input("Phone Number")

email = st.text_input("Email")

if st.button("Save Details"):

    st.session_state["name"] = name
    st.session_state["gender"] = gender
    st.session_state["age"] = age
    st.session_state["phone"] = phone
    st.session_state["email"] = email

    st.success("Patient Details Saved Successfully!")