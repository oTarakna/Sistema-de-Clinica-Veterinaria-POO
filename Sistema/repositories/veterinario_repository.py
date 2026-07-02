from database.conexao import DBConnection
from models.classe_Veterinario import Veterinario
from typing import List, Optional

class VeterinarioRepository:
    def criar(self, vet: Veterinario) -> int:
        query = """INSERT INTO veterinarios (nome, cpf, telefone, email, crmv, especialidade) 
                   VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (vet.nome, vet.cpf, vet.telefone, vet.email, vet.crmv, vet.especialidade))
            return cursor.fetchone()[0]

    def buscar_por_id(self, id_vet: int) -> Optional[Veterinario]:
        query = "SELECT id, nome, cpf, telefone, email, crmv, especialidade FROM veterinarios WHERE id = %s;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (id_vet,))
            row = cursor.fetchone()
            if row:
                return Veterinario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return None

    def listar_todos(self) -> List[Veterinario]:
        query = "SELECT id, nome, cpf, telefone, email, crmv, especialidade FROM veterinarios ORDER BY id;"
        lista = []
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query)
            for row in cursor.fetchall():
                lista.append(Veterinario(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return lista
