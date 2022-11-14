import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
