import streamlit as st

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query to retrieve user data.
df = conn.query('SELECT * FROM users;')

# Create a Streamlit table to display user data and add a delete button.
for row in df.itertuples():
    st.write(f"{row.name} has an email: {row.email}")
    
    # Add a delete button for each user
    if st.button(f"Delete {row.name}"):
        # Use the user's unique identifier (e.g., user_id) to delete the record
        conn.query(f'DELETE FROM users WHERE user_id = {row.user_id};')
        st.success(f"{row.name}'s record has been deleted.")

# Display the updated results in a table using Markdown.
st.write(df)
