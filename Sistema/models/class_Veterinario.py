from models.classe_Pessoa import Pessoa

class Veterinario(Pessoa):
    def __init__(self, id_pessoa: int, nome: str, cpf: str, telefone: str, email: str, crmv: str, especialidade: str) -> None:
        super().__init__(id_pessoa, nome, cpf, telefone, email)
        self.__crmv = crmv
        self.__especialidade = especialidade

    @property
    def crmv(self) -> str:
        return self.__crmv

    @property
    def especialidade(self) -> str:
        return self.__especialidade

    def emitir_laudo(self, descricao: str) -> str:
        return f"LAUDO CLÍNICO EMITIDO PELO DR(A) {self._nome} [CRMV: {self.__crmv}]\nPARECER: {descricao}"

    def __str__(self) -> str:
        return f"Vet: {self._nome} | CRMV: {self.__crmv} | Especialidade: {self.__especialidade}"
