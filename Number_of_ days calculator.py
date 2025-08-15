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

# Get max possible year (today)
max_year = date.today().year
min_year = 1900
years = list(range(max_year, min_year - 1, -1))
months = list(range(1, 13))
days = list(range(1, 32))

# Sub-boxes for each date part
year = st.selectbox("Year", years, index=0)
month = st.selectbox("Month", months, index=date.today().month - 1)
day = st.selectbox("Day", days, index=date.today().day - 1)

if st.button("Calculate Number of Days"):
    try:
        dob = date(year, month, day)
        today = date.today()
        days_lived = (today - dob).days
        st.success(f"You have lived {days_lived} days.")
    except ValueError:
        st.error("Invalid date selected (e.g., February 30th). Please pick a valid date.")
