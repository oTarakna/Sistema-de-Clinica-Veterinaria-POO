from database.conexao import DBConnection
from models.classe_Servico import Servico
from models.classe_Consulta import Consulta
from models.classe_Exame import Exame
from repositories.veterinario_repository import VeterinarioRepository
from typing import List

class ServicoRepository:
    def __init__(self):
        self._vet_repo = VeterinarioRepository()

    def criar_consulta(self, consulta: Consulta, prontuario_id: int) -> int:
        query = """INSERT INTO servicos (tipo, data_hora, valor_base, status, prontuario_id, queixa_principal, diagnostico, prescricao, veterinario_id) 
                   VALUES ('CONSULTA', %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (consulta.data_hora, consulta.valor_base, consulta.status, prontuario_id,
                                   consulta.queixa_principal, consulta.diagnostico, consulta.prescricao, consulta.veterinario.id))
            return cursor.fetchone()[0]

    def criar_exame(self, exame: Exame, prontuario_id: int) -> int:
        query = """INSERT INTO servicos (tipo, data_hora, valor_base, status, prontuario_id, tipo_exame, resultado, laboratorio_parceiro) 
                   VALUES ('EXAME', %s, %s, %s, %s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (exame.data_hora, exame.valor_base, exame.status, prontuario_id,
                                   exame.tipo_exame, exame.resultado, exame.laboratorio_parceiro))
            return cursor.fetchone()[0]

    def listar_por_prontuario(self, prontuario_id: int, animal_id: int) -> List[Servico]:
        query = """SELECT id, tipo, data_hora, valor_base, status, queixa_principal, 
                          diagnostico, prescricao, veterinario_id, tipo_exame, resultado, laboratorio_parceiro 
                   FROM servicos WHERE prontuario_id = %s ORDER BY data_hora;"""
        servicos: List[Servico] = []
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (prontuario_id,))
            for row in cursor.fetchall():
                id_s, tipo, dt, v_base, stat = row[0], row[1], row[2], float(row[3]), row[4]
                if tipo == 'CONSULTA':
                    vet = self._vet_repo.buscar_por_id(row[8])
                    servicos.append(Consulta(id_s, dt, v_base, stat, animal_id, row[5], row[6], row[7], vet))
                else:
                    servicos.append(Exame(id_s, dt, v_base, stat, animal_id, row[9], row[10], row[11]))
        return servicos
