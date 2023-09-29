import streamlit as st

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query to retrieve user data.
df = conn.query('SELECT * FROM users;')


    # Add a delete button for each user
if st.button(f"Delete {row.name}"):
    conn.query(f'DELETE FROM users WHERE user_id = {row.user_id};')
    st.success(f"{row.name}'s record has been deleted.")


# Display the updated results in a table using Markdown.
st.write(df)
