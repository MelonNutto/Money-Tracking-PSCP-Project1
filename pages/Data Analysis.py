import streamlit as st
import datetime
from datetime import date
from streamlit_gsheets import GSheetsConnection
from pathlib import Path
from urllib.parse import urlencode

# --- GG SHEET ---
st.title("📊 DATA TABLE")
st.write("---")
st.write("")
url = "https://docs.google.com/spreadsheets/d/1r-Bk-wYsJV3WePfOC5XSTqFeeyOwnybpqVWupEBRvHA/edit?usp=sharing"

# ไว้แก้บัค gg spreadsheet
@st.cache_data(ttl=60)  # ไว้เคลียร์ cache กัน bug
def load_sheet_data(spreadsheet_url):
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn.read(spreadsheet=spreadsheet_url, usecols=[0, 1, 2])

data = load_sheet_data(url)
st.dataframe(data, use_container_width=True)
