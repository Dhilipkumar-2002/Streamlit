Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from datetime import date
... import streamlit as st
... 
... st.set_page_config(page_title="Number of Days Lived Calculator", layout="centered")
... st.title("Number of Days Lived Calculator")
... 
... # Inputs
... st.subheader("Enter your Date of Birth")
... day = st.number_input("Day (dd)", min_value=1, max_value=31, step=1)
... month = st.number_input("Month (mm)", min_value=1, max_value=12, step=1)
... year = st.number_input("Year (yyyy)", min_value=1, max_value=date.today().year, step=1)
... 
... # Button click
... if st.button("Calculate Number of Days"):
...     try:
...         dob = date(year, month, day)  # Validate date
...         today = date.today()
...         days_lived = (today - dob).days
...         st.success(f"You have lived {days_lived} days.")
...     except ValueError:
