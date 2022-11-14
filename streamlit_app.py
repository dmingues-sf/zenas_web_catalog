import snowflake.connector

streamlit.title("TEST")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
