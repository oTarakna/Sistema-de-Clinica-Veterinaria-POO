# arquivo: test_conn.py
from database.conexao import DBConnection

print("Tentando conectar ao PostgreSQL...")
try:
    with DBConnection.get_cursor() as cursor:
        cursor.execute("SELECT version();")
        versao = cursor.fetchone()
        print("\n Conexão realizada com sucesso!")
        print(f"Versão do PostgreSQL: {versao[0]}")
except Exception as e:
    print(f"\n Falha na conexão. Erro encontrado:\n{e}")
