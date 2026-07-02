from database.conexao import DBConnection
from models.classe_Prontuario import Prontuario
from models.classe_Animal import Animal
from typing import Optional

class ProntuarioRepository:
    def criar(self, animal_id: int) -> int:
        query = "INSERT INTO prontuarios (animal_id) VALUES (%s) RETURNING id;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (animal_id,))
            return cursor.fetchone()[0]

    def buscar_por_animal(self, animal_id: int) -> Optional[int]:
        query = "SELECT id FROM prontuarios WHERE animal_id = %s;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (animal_id,))
            row = cursor.fetchone()
            if row:
                return row[0]
        return None
