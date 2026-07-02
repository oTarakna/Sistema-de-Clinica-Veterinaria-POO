from abc import ABC, abstractmethod
from datetime import datetime

class Servico(ABC):
    def __init__(self, id_servico: int, data_hora: datetime, valor_base: float, status: str, animal_id: int) -> None:
        self._id = id_servico
        self._data_hora = data_hora
        self._valor_base = valor_base
        self._status = status
        self._animal_id = animal_id

    @property
    def id(self) -> int:
        return self._id

    @property
    def data_hora(self) -> datetime:
        return self._data_hora

    @property
    def valor_base(self) -> float:
        return self._valor_base

    @property
    def status(self) -> str:
        return self._status

    @property
    def animal_id(self) -> int:
        return self._animal_id

    @abstractmethod
    def calcular_valor_total(self) -> float:
        pass

    def finalizar_servico(self) -> None:
        self._status = "Finalizado"
