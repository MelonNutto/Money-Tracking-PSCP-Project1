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

# ไว้แก้บัค gg spreadsheet
@st.cache_data(ttl=5)  # ไว้เคลียร์ cache กัน bug
def load_sheet_data(): 
    conn = st.connection("gsheets", type=GSheetsConnection)
    a = conn.read(worksheet="Expenses", usecols=range(3), ttl=5)
    return a

data = load_sheet_data()
st.dataframe(data, use_container_width=True)
