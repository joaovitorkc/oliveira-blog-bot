from src.connection.db_connection import get_cursor

def execute_query(query):
    cursor = get_cursor()  
    if cursor:
        try:
            print(f"Executando a query")
            cursor.execute(query)  
            return cursor.fetchall()  
        except Exception as e:
            print(f"Erro ao executar a query: {e}")
            return []
