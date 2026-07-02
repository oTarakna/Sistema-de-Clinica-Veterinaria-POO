# arquivo: repositories/agendamento_repository.py
from database.conexao import DBConnection
from models.classe_Agendamento import Agendamento
from repositories.cliente_repository import ClienteRepository
from repositories.animal_repository import AnimalRepository
from repositories.veterinario_repository import VeterinarioRepository
from typing import List

class AgendamentoRepository:
    def __init__(self):
        self._cli_repo = ClienteRepository()
        self._ani_repo = AnimalRepository()
        self._vet_repo = VeterinarioRepository()

    def criar(self, agendamento: Agendamento) -> int:
        query = """INSERT INTO agendamentos (data_hora, status, cliente_id, animal_id, veterinario_id) 
                   VALUES (%s, %s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (agendamento.data_hora, agendamento.status, agendamento.cliente.id, 
                                   agendamento.animal.id, agendamento.veterinario.id))
            return cursor.fetchone()[0]

    def listar_todos(self) -> List[Agendamento]:
        query = "SELECT id, data_hora, status, cliente_id, animal_id, veterinario_id FROM agendamentos ORDER BY data_hora;"
        lista = []
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query)
            for row in cursor.fetchall():
                cli = self._cli_repo.buscar_por_id(row[3])
                ani = self._ani_repo.buscar_por_id(row[4])
                vet = self._vet_repo.buscar_por_id(row[5])
                if cli and ani and vet:
                    lista.append(Agendamento(row[0], row[1], row[2], cli, ani, vet))
        return lista
