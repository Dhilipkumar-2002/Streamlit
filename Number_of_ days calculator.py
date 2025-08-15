from datetime import date
import streamlit as st

# Page config
st.set_page_config(page_title="Number of Days Lived Calculator", layout="centered")
st.title("Number of Days Lived Calculator")
st.subheader("Enter your Date of Birth")
# Background color
page_bg = """
<style>
    .stApp {
        background-color: #004953;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.title("Number of Days Lived Calculator")

# Date picker input
dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

# Button click
if st.button("Calculate Number of Days"):
    today = date.today()
    days_lived = (today - dob).days
    st.success(f"You have lived {days_lived} days.")


