import streamlit as st

# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")

# Perform query to retrieve user data.
df = conn.query('SELECT * FROM users;')

# Create a Streamlit table to display user data and add a delete button.
for index, row in df.iterrows():
    # Display user information
    st.write(f"Name: {row['name']}, Email: {row['email']}")
    
    # Add a delete button for each user
    if st.button(f"Delete {row['name']}"):
        try:
            # Trigger a query to delete the corresponding user's record from the database
            conn.query(f"DELETE FROM users WHERE id = {row['id']};")
            st.success(f"{row['name']}'s record has been deleted.")
            
            # Remove the deleted row from the displayed DataFrame
            df.drop(index, inplace=True)
        except Exception as e:
            st.error(f"An error occurred while deleting {row['name']}'s record: {str(e)}")

# Display the updated results in a table using Markdown.
st.write(df)
