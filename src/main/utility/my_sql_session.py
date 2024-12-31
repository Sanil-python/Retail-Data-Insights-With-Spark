import mysql.connector
from resources.dev import config

def get_mysql_connection():
    connection = mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE
    )
    return connection

# def get_mysql_connection():
#     try:
#         connection = mysql.connector.connect(
#             host=config.HOST,
#             user=config.USER,
#             password=config.PASSWORD,
#             database=config.DATABASE
#         )
#         print("Connection successful")
#         return connection
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None














# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password",
#     database="manish"
# )
#
# # Check if the connection is successful
# if connection.is_connected():
#     print("Connected to MySQL database")
#
# cursor = connection.cursor()
#
# # Execute a SQL query
# query = "SELECT * FROM manish.testing"
# cursor.execute(query)
#
# # Fetch and print the results
# for row in cursor.fetchall():
#     print(row)
#
# # Close the cursor
# cursor.close()
#
# connection.close()
