import streamlit as st
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="tai.db.elephantsql.com",
    database="bjvsinga",
    user="bjvsinga",
    password="Eifswy6LwMR_XxhhLOuADg3oU-mWoOc2",
)
cur = conn.cursor()

# Create a form to collect the user's registration information
form = st.form("registration_form")
name = form.text_input("Name")
email = form.text_input("Email")
password = form.text_input("Password")
submit = form.form_submit_button("Submit")

# If the user submits the form, validate the data and save it to the database
if submit:
    # Check if any of the fields are empty
    if not name or not email or not password:
        st.error("Please fill in all fields.")
    else:
        try:
            # Insert the user's registration information into the database using parameterized query
            cur.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password),
            )
            conn.commit()

            # Display a success message to the user
            st.success("Your registration was successful!")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Close the database connection
cur.close()
conn.close()
