import psycopg2

# Connecting to the data base:
connection = psycopg2.connect(
    host="drayton80",
    database="postage",
    user="postgres",
    password="correa80",
    port=5433
)

# Closing connection
connection.close()