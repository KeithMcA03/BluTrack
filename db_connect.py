import mysql.connector

# Connecting to the database
conn = mysql.connector.connect(
    host="10.209.55.95",          
    user="bis425_gr4",      
    password="sWjgL38VD$"     
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")

# Print out the tables
for table in cursor.fetchall():
    print(table)

cursor.close()
conn.close()
