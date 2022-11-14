import snowflake.connector
import streamlit

streamlit.title("TEST")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
