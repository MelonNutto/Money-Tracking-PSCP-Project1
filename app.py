import streamlit as st
import datetime
import time
from datetime import date


# --- PAGE CONFIG ---
st.set_page_config(page_title="Money Tracker", layout="wide")

# --- CSS animation พิมพ์ + gradiant ---
st.markdown("""
    <style>
    body {
        background: #0e1117;
        margin: 0;
        padding: 0;
        color: white;
        text-align: center;
    }

    .container {
        display: inline-block;
        margin-top: 40px;
    }

    .text {
        font-size: 5em;
        letter-spacing: 10px;
        font-family: 'Blippo', fantasy;
        border-right: 5px solid;
        width: 0;
        white-space: nowrap;
        overflow: hidden;
        animation:
            typing 0.55s steps(20, end) forwards,
            cursor .6s step-end infinite alternate,
            gradient 5s linear infinite;
        color: transparent;
        background-image: linear-gradient(to left, 	#7289da, #3498db, #b9b9b9);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-background-size: 500%;
        background-size: 500%;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes cursor {
        50% { border-color: transparent; }
    }

    @keyframes gradient {
        0% { background-position: 0 100%; }
        50% { background-position: 100% 0; }
        100% { background-position: 0 100%; }
    }
    </style>
""", unsafe_allow_html=True)

# --- ทำ Animation พิมพ์ + สี gradiant ---
st.markdown("""
<div class="container">
    <div class="text">Money Tracker</div>
</div>
""", unsafe_allow_html=True)

st.write("This program helps you calculate your income, expenses, and remaining balance.")
st.write("---")

# --- CLOCK PLACEHOLDER ---
clock_placeholder = st.empty()
st.write("---")

# --- INPUTS ---
date_select = st.date_input("Select your date", format = "DD/MM/YYYY")
income = st.number_input("Enter your total income", min_value=0.0, step=100.0)
expense = st.number_input("Enter your total expenses", min_value=0.0, step=100.0)

# --- CALCULATION (รอเอาลงบันทึก) ---
st.write("")
if st.button("Calculate"):
    balance = income - expense
    if balance > 0:
        st.success(f"✅ Your remaining balance is: **${balance:,.2f}**")
    else:
        st.error(f"❌ Your remaining balance is: **${balance:,.2f}**")

# --- LIVE CLOCK ---
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_placeholder.markdown(f"### ⏱️ Current time: {current_time}")
    # --- รีทุกๆ 1 วิ ---
    time.sleep(1)
