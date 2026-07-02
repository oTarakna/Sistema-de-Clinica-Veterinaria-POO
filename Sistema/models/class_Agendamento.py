from datetime import datetime
from models.classe_Cliente import Cliente
from models.classe_Animal import Animal
from models.classe_Veterinario import Veterinario

class Agendamento:
    def __init__(self, id_agendamento: int, data_hora: datetime, status: str,
                 cliente: Cliente, animal: Animal, veterinario: Veterinario) -> None:
        self.__id = id_agendamento
        self.__data_hora = data_hora
        self.__status = status
        self.__cliente = cliente
        self.__animal = animal
        self.__veterinario = veterinario

    @property
    def id(self) -> int:
        return self.__id

    @property
    def data_hora(self) -> datetime:
        return self.__data_hora

    @property
    def status(self) -> str:
        return self.__status

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def animal(self) -> Animal:
        return self.__animal

    @property
    def veterinario(self) -> Veterinario:
        return self.__veterinario

    def confirmar_agendamento(self) -> None:
        self.__status = "Confirmado"

    def cancelar_agendamento(self, motivo: str) -> None:
        self.__status = f"Cancelado ({motivo})"

    def __str__(self) -> str:
        return f"Agenda {self.__id}: {self.__data_hora.strftime('%d/%m/%Y %H:%M')} | Paciente: {self.__animal.nome} | Vet: {self.__veterinario.nome} | Status: {self.__status}"
