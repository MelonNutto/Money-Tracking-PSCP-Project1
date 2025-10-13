import streamlit as st
import datetime
import time
from pathlib import Path

# --- โหลดไฟล์ CSS มาใส่ในโค้ด Python ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- CSS ปุ่ม ---
button_css = Path(__file__).parent / "button2_style.css"
load_css(button_css)
css_file = Path(__file__).parent / "style2.css"
load_css(css_file)

# --- Animation พิมพ์ + สี gradiant ---
st.markdown("""
<div class="container">
    <div class="text">Calculation</div>
</div>
""", unsafe_allow_html=True)
st.write("---")

# --- CLOCK ---

# --- CLOCK PLACEHOLDER ---
clock_placeholder = st.empty()
st.write("---")

st.markdown('<div id="Home"></div>', unsafe_allow_html=True)
current_time = datetime.datetime.now().strftime("%H:%M:%S")
current_date = datetime.datetime.now().strftime("%D")
clock_placeholder.markdown(f"### 🗓️ Current date: {current_date} | ⏱️ Current time: {current_time}")
# st.write("---")
time.sleep(0.5) #มี Delay ของ St.rerun เลยต้อง Sleep น้อยกว่า 1 วิ
st.rerun()
# --- INPUTS ---
st.write("")
date_select = st.date_input("Select your date", format="DD/MM/YYYY")
income = st.number_input("Enter your total income", min_value=0.0, step=100.0)
expense = st.number_input("Enter your total expenses", min_value=0.0, step=100.0)

# --- CALCULATION ---
st.write("")
if st.button("Calculate"):
    balance = income - expense
    st.write("")
    if balance > 0:
        st.write("")
        st.success(f"✅ Your remaining balance is: **${balance:,.2f}**")
    else:
        st.write("")
        st.error(f"❌ Your remaining balance is: **${balance:,.2f}**")
st.write("---")