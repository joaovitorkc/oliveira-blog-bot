from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_DATABASE"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

connection = None
cursor = None

def create_connection():
    global connection, cursor
    if connection is None:
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                cursor = connection.cursor()
                print("Conectado ao banco de dados.")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

def get_cursor():
    if cursor is None:
        create_connection()
    return cursor

def close_connection():
    global connection, cursor
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    connection = None
    cursor = None
    print("Conexão fechada.")
