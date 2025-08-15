from datetime import date
import streamlit as st

# Page config
st.set_page_config(page_title="Number of Days Lived Calculator", layout="centered")

# Custom CSS for colors and layout
st.markdown("""
    <style>
        .stApp {
            background-color: #E0FFF5;
        }
        h1, h2, h3 {
            color: #FFD700;
            font-family: 'Trebuchet MS', sans-serif;
            text-shadow: 1px 1px 2px #002833;
        }
        .result-card {
            padding: 18px;
            border-radius: 10px;
            background: #004953;
            border: 2px solid #FFD700;
            color: #FFFFFF;
            text-align: center;
            margin-top: 25px;
        }
        .stButton>button {
            background-color: #004953;
            color: #FFD700;
            font-size: large;
            border-radius: 12px;
            border: 2px solid #FFD700;
            box-shadow: 0 2px 8px rgba(0,40,51,0.08);
            transition: background 0.2s, color 0.2s;
        }
        .stButton>button:hover {
            background-color: #FF6F61;
            color: #FFF;
            border: 2px solid #FFD700;
        }
        .stSelectbox {
            background-color: #E0FFF5;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,73,83,0.10);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎈 Number of Days Lived Calculator 🎈")
st.subheader("📅 Enter your Date of Birth")

# Year, month, and day pickers as columns
today = date.today()
min_year = 1900
years = list(range(today.year, min_year - 1, -1))
months = list(range(1, 13))
days = list(range(1, 32))

col1, col2, col3 = st.columns(3)
with col1:
    day = st.selectbox("Day", days, index=today.day - 1)
with col2:
    month = st.selectbox("Month", months, index=today.month - 1)
with col3:
    year = st.selectbox("Year", years, index=0)

# Button click
if st.button("Calculate Number of Days"):
    try:
        dob = date(year, month, day)
        if dob > today:
            st.error("Date of birth cannot be in the future!")
        else:
            days_lived = (today - dob).days
            st.markdown(f"""
                <div class="result-card">
                    <h2>🎉 You have lived <span style="color:#FFD700;">{days_lived}</span> days! 🎉</h2>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
    except ValueError:
        st.error("Invalid date selected (e.g., February 30th). Please pick a valid date.")

