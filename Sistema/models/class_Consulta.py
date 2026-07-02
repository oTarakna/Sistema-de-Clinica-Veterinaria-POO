from models.classe_Servico import Servico
from models.classe_Veterinario import Veterinario
from datetime import datetime

class Consulta(Servico):
    def __init__(self, id_servico: int, data_hora: datetime, valor_base: float, status: str, animal_id: int,
                 queixa_principal: str, diagnostico: str, prescricao: str, veterinario: Veterinario) -> None:
        super().__init__(id_servico, data_hora, valor_base, status, animal_id)
        self.__queixa_principal = queixa_principal
        self.__diagnostico = diagnostico
        self.__prescricao = prescricao
        self.__veterinario = veterinario

    @property
    def queixa_principal(self) -> str:
        return self.__queixa_principal

    @property
    def diagnostico(self) -> str:
        return self.__diagnostico

    @property
    def prescricao(self) -> str:
        return self.__prescricao

    @property
    def veterinario(self) -> Veterinario:
        return self.__veterinario

    def calcular_valor_total(self) -> float:
        return round(self._valor_base * 1.15, 2)

    def registrar_anamnese(self, queixa: str, diag: str) -> None:
        self.__queixa_principal = queixa
        self.__diagnostico = diag

    def __str__(self) -> str:
        return f"Consulta ID: {self._id} | Tipo: Consulta | Total: R${self.calcular_valor_total()} | Status: {self._status}"
