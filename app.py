import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
st.write("connection success or what")

df = conn.read(sheet="sample", ttl="10m")
st.write(df)
