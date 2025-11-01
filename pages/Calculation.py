import streamlit as st
import datetime
import time
from pathlib import Path
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import streamlit as st

# --- โหลดไฟล์ CSS มาใส่ในโค้ด Python ---
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Load Database
conn = st.connection("gsheets", type=GSheetsConnection)
exist_data = conn.read(worksheet="Expenses", usecols=list(range(3)), ttl=5)

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

# --- INPUTS ---
st.write("")
with st.form("Data"):
    date_select = st.date_input("Select your date", format="DD/MM/YYYY")
    income = st.number_input("Enter your total income", min_value=0.0, step=100.0)
    expense = st.number_input("Enter your total expenses", min_value=0.0, step=100.0)

    submit = st.form_submit_button("Calculate")
# --- CALCULATION ---
st.write("")
if submit:
    balance = income - expense
    new_data = pd.DataFrame([{
        'Date': date_select,
        "Income": income,
        "Expense": expense,
        "Net": balance
    }])

    updated = pd.concat([exist_data, new_data])
    conn.update(worksheet="Expenses", data=updated)
    st.success("Saved")


    st.write("")
    if balance > 0:
        st.write("")
        st.success(f"✅ Your remaining balance is: **${balance:,.2f}**")
    else:
        st.write("")
        st.error(f"❌ Your remaining balance is: **${balance:,.2f}**")
    st.write("---")
