from models.classe_Pessoa import Pessoa
from typing import List, Any

class Cliente(Pessoa):
    def __init__(self, id_pessoa: int, nome: str, cpf: str, telefone: str, email: str, endereco: str) -> None:
        super().__init__(id_pessoa, nome, cpf, telefone, email)
        self.__endereco = endereco
        self.__animais: List[Any] = []

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, valor: str) -> None:
        self.__endereco = valor

    @property
    def animais(self) -> List[Any]:
        return self.__animais

    def vincular_animal(self, animal: Any) -> None:
        if animal not in self.__animais:
            self.__animais.append(animal)

    def remover_animal(self, animal: Any) -> None:
        if animal in self.__animais:
            self.__animais.remove(animal)

    def __str__(self) -> str:
        return f"Cliente ID: {self._id} | Nome: {self._nome} | CPF: {self._cpf} | Cidade: {self.__endereco}"
