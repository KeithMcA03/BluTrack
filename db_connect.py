import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="10.209.55.95",
        user="bis425_g4",
        password="sWjgl38VD$",
        database="bis425_g4"
    )