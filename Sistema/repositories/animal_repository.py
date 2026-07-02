from database.conexao import DBConnection
from models.classe_Animal import Animal
from typing import List, Optional
from datetime import date

class AnimalRepository:
    def criar(self, animal: Animal) -> int:
        query = """INSERT INTO animais (nome, especie, raca, data_nascimento, peso, cliente_id) 
                   VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (animal.nome, animal.especie, animal.raca, animal.data_nascimento, animal.peso, animal.cliente_id))
            return cursor.fetchone()[0]

    def buscar_por_id(self, id_animal: int) -> Optional[Animal]:
        query = "SELECT id, nome, especie, raca, data_nascimento, peso, cliente_id FROM animais WHERE id = %s;"
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (id_animal,))
            row = cursor.fetchone()
            if row:
                return Animal(row[0], row[1], row[2], row[3], row[4], float(row[5]), row[6])
        return None

    def listar_por_tutor(self, id_cliente: int) -> List[Animal]:
        query = "SELECT id, nome, especie, raca, data_nascimento, peso, cliente_id FROM animais WHERE cliente_id = %s;"
        lista = []
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (id_cliente,))
            for row in cursor.fetchall():
                lista.append(Animal(row[0], row[1], row[2], row[3], row[4], float(row[5]), row[6]))
        return lista
