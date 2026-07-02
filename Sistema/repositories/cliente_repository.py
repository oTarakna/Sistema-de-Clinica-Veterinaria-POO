from database.conexao import DBConnection
from models.classe_Cliente import Cliente
from typing import List, Optional

class ClienteRepository:
    def criar(self, cliente: Cliente) -> int:
        query = """INSERT INTO clientes (nome, cpf, telefone, email, endereco) 
                   VALUES (%s, %s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco))
            id_gerado = cursor.fetchone()[0]
            return id_gerado

    def buscar_por_id(self, id_cliente: int) -> Optional[Cliente]:
        query = "SELECT id, nome, cpf, telefone, email, endereco FROM clientes WHERE id = %s;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (id_cliente,))
            row = cursor.fetchone()
            if row:
                return Cliente(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        query = "SELECT id, nome, cpf, telefone, email, endereco FROM clientes WHERE cpf = %s;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (cpf,))
            row = cursor.fetchone()
            if row:
                return Cliente(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def listar_todos(self) -> List[Cliente]:
        query = "SELECT id, nome, cpf, telefone, email, endereco FROM clientes ORDER BY id;"
        lista = []
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                lista.append(Cliente(row[0], row[1], row[2], row[3], row[4], row[5]))
        return lista

    def atualizar(self, cliente: Cliente) -> None:
        query = """UPDATE clientes SET nome=%s, cpf=%s, telefone=%s, email=%s, endereco=%s 
                   WHERE id=%s;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco, cliente.id))

    def deletar(self, id_cliente: int) -> None:
        query = "DELETE FROM clientes WHERE id = %s;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (id_cliente,))
