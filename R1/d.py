# streamlit_app.py
import streamlit as st
# Initialize connection.
conn = st.experimental_connection("postgresql", type="sql")
# Perform query.
df = conn.query('SELECT * FROM users;')
# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.email}:")
    # Display the results in a table with custom formatting.
# Display the results in a table using Markdown.
# Print the results
st.write(df)