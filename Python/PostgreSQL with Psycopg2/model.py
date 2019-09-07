import psycopg2

# Connecting to the data base:
connection = psycopg2.connect(
    database="postage",
    user="postgres",
    password="postgres",
    port=5433
)

# Creating a cursor:
cursor = connection.cursor()
# There are two types of cursors:
#  - Client-side cursors: pull the query for the client 
#  - Server-side cursors: control the flow of data when the client is handling
#    with a huge amount that is not possible to keeping entire in memory

# Executing a query
cursor.execute("select * from perfil")
# Get the rows obtained in the query:
rows = cursor.fetchall()

# To test with it work:
for row in rows:
    print(f"nome de usuario {row[0]}; nome real {row[1]};")

# Closing cursor
cursor.close()
# Closing connection
connection.close()