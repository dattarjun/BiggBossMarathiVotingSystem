import mysql.connector

# MySQL Database Configuration
db_connection = mysql.connector.connect(
    host='localhost',       # Database Host (usually localhost)
    user='root',  # Your MySQL username
    password='root',  # Your MySQL password
    database='bigboss_voting3'  # Name of the database
)
