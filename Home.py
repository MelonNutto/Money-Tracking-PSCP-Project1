import streamlit as st
import datetime
from datetime import date
from streamlit_gsheets import GSheetsConnection
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Money Tracker", layout="centered")

# --- โหลดไฟล์ css ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = Path(__file__).parent / "Homestyles.css"
load_css(css_file)
button_css = Path(__file__).parent / "button_style.css"
load_css(button_css)

# --- โหลด css มาใช้กับ Money Tracker ---
st.markdown("""
<div class="container">
    <div class="text">Money Tracker</div>
</div>
""", unsafe_allow_html=True)

st.write("This program helps you calculate your income, expenses, and remaining balance.")
st.write("---")

# --- CLOCK ---
count = st_autorefresh(interval=1000, key="clock_refresh")
clock_placeholder = st.empty()
st.write("---")

current_time = datetime.datetime.now().strftime("%H:%M:%S")
current_date = datetime.datetime.now().strftime("%D")
clock_placeholder.markdown(f"### 🗓️ Current date: {current_date} | ⏱️ Current time: {current_time}")

# --- GG Sheet Input ---
st.subheader("🔗 Connect your Google Sheet")
st.write("")

if 'sheet_url' not in st.session_state:
    st.session_state.sheet_url = ""

sheet_url = st.text_input(
    "Enter your Google Sheets URL:",
    placeholder="Paste your Google Sheets link here...",
    value=st.session_state.sheet_url
)

if sheet_url:
    st.session_state.sheet_url = sheet_url
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        st.success("✅ Connected successfully!")
    except Exception as e:
        st.error(f"❌ Failed to connect: {e}")