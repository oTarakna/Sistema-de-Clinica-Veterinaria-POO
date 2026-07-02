# arquivo: models/animal.py
from datetime import date

class Animal:
    def __init__(self, id_animal: int, nome: str, especie: str, raca: str, data_nascimento: date, peso: float, cliente_id: int) -> None:
        self.__id = id_animal
        self.__nome = nome
        self.__especie = especie
        self.__raca = raca
        self.__data_nascimento = data_nascimento
        self.__peso = peso
        self.__cliente_id = cliente_id

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def especie(self) -> str:
        return self.__especie

    @property
    def raca(self) -> str:
        return self.__raca

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def peso(self) -> float:
        return self.__peso

    @property
    def cliente_id(self) -> int:
        return self.__cliente_id

    def calcular_idade(self) -> int:
        hoje = date.today()
        return hoje.year - self.__data_nascimento.year - ((hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day))

    def atualizar_peso(self, novo_peso: float) -> None:
        if novo_peso > 0:
            self.__peso = novo_peso

    def __str__(self) -> str:
        return f"Animal ID: {self.__id} | Nome: {self.__nome} | Espécie: {self.__especie} | Idade: {self.calcular_idade()} anos | Peso: {self.__peso}kg"
