import streamlit as st
import datetime
from datetime import date
from streamlit_gsheets import GSheetsConnection
from pathlib import Path
from urllib.parse import urlencode
import pandas as pd

# --- GG SHEET ---
st.title("📊 DATA TABLE")
st.write("---")
st.write("")

# Check if sheet URL is set
if 'sheet_url' not in st.session_state or not st.session_state.sheet_url:
    st.warning("⚠️ Please connect your Google Sheet on the Home page first!")
    st.stop()

# ไว้แก้บัค gg spreadsheet
@st.cache_data(ttl=5)  # ไว้เคลียร์ cache กัน bug
def load_sheet_data(sheet_url): 
    conn = st.connection("gsheets", type=GSheetsConnection)
    a = conn.read(spreadsheet=sheet_url, worksheet="Expenses", usecols=range(4), ttl=5)
    return a

try:
    # เช็คว่ามีลิ้งค์ gg sheet ไหม
    data = load_sheet_data(st.session_state.sheet_url)
    st.dataframe(data, use_container_width=True)
except Exception as e:
    # --- เช็คว่า error อะไร ---
    st.error(f"❌ Error loading data: {e}")
    st.info("ให้ตั้งชื่อแผ่นงานว่า 'Expenses' และคอลัมน์ชื่อ Date, Income, Expense, Net")