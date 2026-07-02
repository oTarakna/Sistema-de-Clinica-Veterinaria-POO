from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id_pessoa: int, nome: str, cpf: str, telefone: str, email: str) -> None:
        self._id = id_pessoa
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email

    @property
    def id(self) -> int:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def telefone(self) -> str:
        return self._telefone

    @property
    def email(self) -> str:
        return self._email

    def validar_cpf(self) -> bool:
        cpf_limpo = "".join(filter(str.isdigit, self._cpf))
        return len(cpf_limpo) == 11

    def atualizar_contato(self, novo_telefone: str, info_email: str) -> None:
        if novo_telefone:
            self._telefone = novo_telefone
        if info_email:
            self._email = info_email
