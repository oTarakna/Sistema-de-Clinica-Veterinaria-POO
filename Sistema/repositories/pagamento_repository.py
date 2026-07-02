from database.conexao import DBConnection
from models.classe_Pagamento import Pagamento
from typing import List

class PagamentoRepository:
    def criar(self, pagamento: Pagamento) -> int:
        query = """INSERT INTO pagamentos (valor_total, forma_pagamento, pago, servico_id) 
                   VALUES (%s, %s, %s, %s) RETURNING id;"""
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query, (pagamento.valor_total, pagamento.forma_pagamento, pagamento.pago, pagamento.servico_id))
            return cursor.fetchone()[0]

    def listar_todos(self) -> List[Pagamento]:
        query = "SELECT id, valor_total, forma_pagamento, pago, servico_id FROM pagamentos ORDER BY id;"
        lista = []
        with DBConnection.get_cursor() as cursor:
            cursor.execute(query)
            for row in cursor.fetchall():
                lista.append(Pagamento(row[0], float(row[1]), row[2], row[3], row[4]))
        return lista
