import streamlit as st
import datetime
from datetime import date
from streamlit_gsheets import GSheetsConnection
from pathlib import Path
from urllib.parse import urlencode


# --- SIDEBAR ---

# --- auth ---

# --- PAGE CONFIG ---
st.set_page_config(page_title="Money Tracker", layout="centered")

# --- โหลดไฟล์ CSS มาใส่ในโค้ด Python ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- LOAD CSS ---
css_file = Path(__file__).parent / "style.css"
load_css(css_file)
button_css = Path(__file__).parent / "button_style.css"
load_css(button_css)
google_css = Path(__file__).parent / "google_button.css"
load_css(google_css)

# --- Animation พิมพ์ + สี gradiant ---
st.markdown("""
<div class="container">
    <div class="text">Money Tracker</div>
</div>
""", unsafe_allow_html=True)

st.write("This program helps you calculate your income, expenses, and remaining balance.")
st.write("---")

# --- CLOCK ---
st.markdown('<div id="Home"></div>', unsafe_allow_html=True)
current_time = datetime.datetime.now().strftime("%H:%M:%S")
current_date = datetime.datetime.now().strftime("%D")
st.markdown(f"### 🗓️ Current date: {current_date} | ⏱️ Current time: {current_time}")
st.write("---")


# --- ใช้ column จัดตำแหน่งปุ่ม login ---
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Login with Google"):
        st.login("google")