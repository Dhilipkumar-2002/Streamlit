import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("BMI Calculator")

w = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
h = st.number_input("Height (cm)", min_value=1.0, step=0.1)

if st.button("Calculate BMI"):
    bmi = w / ((h / 100) ** 2)
    st.write(f"**Your BMI:** {bmi:.2f}")
    if bmi < 18.5:
        st.warning("You are Underweight, you must hit the gym and take suffucient intake of protein, fibre and carbohydrate.")
    elif 18.5 <= bmi <= 24.9:
        st.success("You are Normal weight, You are at your optimal weight, check for fat percentage in your body")
    elif 25 <= bmi <= 29.9:
        st.info("You are Overweight, Regular Excercise and consistenely following proper diet wouild improve you health, Buddy")
    elif 30 <= bmi <= 39.9:
        st.error("You are Obese, Consult a doctor and take care of your health")
    else:
        st.error("You are Extremely Obese, must admit to hospital --> immediately")





