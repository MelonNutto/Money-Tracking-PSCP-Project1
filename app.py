import streamlit as st

st.set_page_config(page_title="Money Tracker", layout="wide")

# --- HEADER ---
st.title("Money Tracker")
st.write("This program helps you calculate your income, expenses, and remaining balance.")

st.write("---")

# --- INPUT SECTION ---
income = st.number_input("Enter your total income", min_value=0.0, step=100.0)
expense = st.number_input("Enter your total expenses", min_value=0.0, step=100.0)

# --- CALCULATION ---
if st.button("Calculate"):
    balance = income - expense

    # --- RESULT ---
    st.success(f"✅ Your remaining balance is: **${balance:,.2f}**")

