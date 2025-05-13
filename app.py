import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
st.write("connection success")

df = conn.read(sheet="Expenses", ttl="10m")
st.write(df)
