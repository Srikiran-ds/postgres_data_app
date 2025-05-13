import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
st.write("connection success or what")

df = conn.read(worksheet="sample", ttl="10m")
st.write(df)
# Add the new vendor data to the existing data
name = st.text_input(label="Name")
age = st.text_input(label="age")
submit_button = st.button(label="Submit Details")
if submit_button:
    new_data = pd.DataFrame(
                [
                    {
                        "Name": name,
                        "Age": age,
                    }
                ]  )
updated_df = pd.concat([df, new_data], ignore_index=True)

# Update Google Sheets with the new vendor data
conn.update(worksheet="sample", data=updated_df)
