import streamlit as st
import psycopg2
from psycopg2 import sql

# Database connection
def create_connection():
    try:
        conn = psycopg2.connect(
            host="pg-20229fa0-kiran-b069.h.aivencloud.com",  # Update with your PostgreSQL host
            database="defaultdb",  # Update with your database name
            user="avnadmin",  # Update with your username
            password="AVNS_MDKyGWGnf00wVG_AwCl"  # Update with your password
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Insert data into the database
def insert_data(conn, table, data):
    try:
        with conn.cursor() as cursor:
            columns = data.keys()
            values = [data[column] for column in columns]
            insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values})").format(
                table=sql.Identifier(table),
                fields=sql.SQL(', ').join(map(sql.Identifier, columns)),
                values=sql.SQL(', ').join(sql.Placeholder() * len(values))
            )
            cursor.execute(insert_query, values)
            conn.commit()
            st.success("Data inserted successfully!")
    except Exception as e:
        st.error(f"Error inserting data: {e}")

# Streamlit app
st.title("PostgreSQL Data Entry App")

conn = create_connection()

if conn:
    table_name = st.text_input("Enter the table name:")
    if table_name:
        st.header(f"Insert Data into {table_name}")
        input_data = {}
        column_name = st.text_input("Enter column name:")
        column_value = st.text_input("Enter column value:")
        if column_name and column_value:
            input_data[column_name] = column_value
        if st.button("Submit"):
            insert_data(conn, table_name, input_data)

conn.close()
