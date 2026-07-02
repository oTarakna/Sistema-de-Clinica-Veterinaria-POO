from models.classe_Servico import Servico
from datetime import datetime

class Exame(Servico):
    def __init__(self, id_servico: int, data_hora: datetime, valor_base: float, status: str, animal_id: int,
                 tipo_exame: str, resultado: str, laboratorio_parceiro: str) -> None:
        super().__init__(id_servico, data_hora, valor_base, status, animal_id)
        self.__tipo_exame = tipo_exame
        self.__resultado = resultado
        self.__laboratorio_parceiro = laboratorio_parceiro

    @property
    def tipo_exame(self) -> str:
        return self.__tipo_exame

    @property
    def resultado(self) -> str:
        return self.__resultado

    @property
    def laboratorio_parceiro(self) -> str:
        return self.__laboratorio_parceiro

    def calcular_valor_total(self) -> float:
        return round(self._valor_base + 45.00, 2)

    def atualizar_resultado(self, laudo: str) -> None:
        self.__resultado = laudo
        self.finalizar_servico()

    def __str__(self) -> str:
        return f"Exame ID: {self._id} | Tipo: {self.__tipo_exame} | Total: R${self.calcular_valor_total()}"
