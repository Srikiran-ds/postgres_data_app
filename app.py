import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
tab1, tab2, tab3 = st.tabs(["Update", "Read", "Analysis"])
#conn = tab2.connection("gsheets", type=GSheetsConnection)
tab2.write("connection success")
df = conn.read(worksheet="sample", ttl="0.5m")
if tab2.button("refresh"):
    df = conn.read(worksheet="sample", ttl="0.5m")
tab2.write(df)

# Add the new vendor data to the existing data
name = tab1.text_input(label="Name")
age = tab1.text_input(label="age")
submit_button = tab1.button(label="Submit Details")
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
    st.success("Vendor details successfully submitted!")
    #df = conn.read(worksheet="sample", ttl="0.5m")
    #st.write(df)
