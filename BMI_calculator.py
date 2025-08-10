import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("BMI Calculator")

w = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
h = st.number_input("Height (cm)", min_value=1.0, step=0.1)

if st.button("Calculate BMI"):
    bmi = w / ((h / 100) ** 2)
    st.write(f"**Your BMI:** {bmi:.2f}")
    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi <= 24.9:
        st.success("Normal weight")
    elif 25 <= bmi <= 29.9:
        st.info("Overweight")
    elif 30 <= bmi <= 39.9:
        st.error("Obese")
    else:
        st.error("Extremely Obese")



