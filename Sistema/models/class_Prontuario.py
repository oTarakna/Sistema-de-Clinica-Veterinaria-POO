from models.classe_Animal import Animal
from models.classe_Servico import Servico
from typing import List

class Prontuario:
    def __init__(self, id_prontuario: int, animal: Animal) -> None:
        self.__id = id_prontuario
        self.__animal = animal
        self.__historico_servicos: List[Servico] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def animal(self) -> Animal:
        return self.__animal

    def adicionar_registro(self, servico: Servico) -> None:
        self.__historico_servicos.append(servico)

    def gerar_historico_completo(self) -> str:
        if not self.__historico_servicos:
            return f"Sem ocorrências registradas para o paciente {self.__animal.nome}."
        
        saida = f"=== PRONTUÁRIO INTEGRAL: {self.__animal.nome.upper()} ===\n"
        for serv in reversed(self.__historico_servicos):
            saida += f"-> {serv}\n"
        return saida
