from repositories.cliente_repository import ClienteRepository
from repositories.animal_repository import AnimalRepository
from repositories.veterinario_repository import VeterinarioRepository
from repositories.servico_repository import ServicoRepository
from repositories.agendamento_repository import AgendamentoRepository
from repositories.pagamento_repository import PagamentoRepository
from repositories.prontuario_repository import ProntuarioRepository

from models.classe_Cliente import Cliente
from models.classe_Animal import Animal
from models.classe_Veterinario import Veterinario
from models.classe_Consulta import Consulta
from models.classe_Exame import Exame
from models.classe_Pagamento import Pagamento
from models.classe_Agendamento import Agendamento
from models.classe_Prontuario import Prontuario

from datetime import datetime, date
from typing import List

class ClinicaService:
    def __init__(self) -> None:
        self.cliente_repo = ClienteRepository()
        self.animal_repo = AnimalRepository()
        self.vet_repo = VeterinarioRepository()
        self.servico_repo = ServicoRepository()
        self.agenda_repo = AgendamentoRepository()
        self.pago_repo = PagamentoRepository()
        self.prontuario_repo = ProntuarioRepository()

    def cadastrar_cliente(self, nome: str, cpf: str, tel: str, email: str, end: str) -> Cliente:
        temp_c = Cliente(0, nome, cpf, tel, email, end)
        if not temp_c.validar_cpf():
            raise ValueError("Documento CPF inválido estruturalmente.")
        if self.cliente_repo.buscar_por_cpf(cpf):
            raise ValueError("CPF informado já se encontra cadastrado.")
        novo_id = self.cliente_repo.criar(temp_c)
        return self.cliente_repo.buscar_por_id(novo_id)

    def obter_cliente(self, id_cliente: int) -> Cliente:
        cli = self.cliente_repo.buscar_por_id(id_cliente)
        if not cli:
            raise KeyError("Cliente não localizado.")
        return cli

    def listar_clientes(self) -> List[Cliente]:
        return self.cliente_repo.listar_todos()

    def atualizar_cliente(self, id_cliente: int, nome: str, cpf: str, tel: str, email: str, end: str) -> None:
        self.obter_cliente(id_cliente)
        cli_mod = Cliente(id_cliente, nome, cpf, tel, email, end)
        if not cli_mod.validar_cpf():
            raise ValueError("Novo CPF informado está incorreto.")
        self.cliente_repo.atualizar(cli_mod)

    def excluir_cliente(self, id_cliente: int) -> None:
        self.obter_cliente(id_cliente)
        self.cliente_repo.deletar(id_cliente)

    def cadastrar_animal(self, nome: str, especie: str, raca: str, data_nasc: date, peso: float, id_tutor: int) -> Animal:
        self.obter_cliente(id_tutor)
        if peso <= 0:
            raise ValueError("O peso inicial deve ser maior que zero.")
        novo_ani = Animal(0, nome, especie, raca, data_nasc, peso, id_tutor)
        id_animal = self.animal_repo.criar(novo_ani)
        
        self.prontuario_repo.criar(id_animal)
        
        return self.animal_repo.buscar_por_id(id_animal)

    def listar_animais_por_tutor(self, id_tutor: int) -> List[Animal]:
        return self.animal_repo.listar_por_tutor(id_tutor)

    def cadastrar_veterinario(self, nome: str, cpf: str, tel: str, email: str, crmv: str, espec: str) -> Veterinario:
        vet = Veterinario(0, nome, cpf, tel, email, crmv, espec)
        if not vet.validar_cpf():
            raise ValueError("CPF do Veterinário inválido.")
        id_gerado = self.vet_repo.criar(vet)
        return self.vet_repo.buscar_por_id(id_gerado)

    def listar_veterinarios(self) -> List[Veterinario]:
        return self.vet_repo.listar_todos()

    def registrar_consulta(self, id_animal: int, id_vet: int, valor_b: float, queixa: str, diag: str, presc: str) -> float:
        vet = self.vet_repo.buscar_por_id(id_vet)
        ani = self.animal_repo.buscar_por_id(id_animal)
        if not vet or not ani:
            raise KeyError("Veterinário ou Animal não encontrado.")
        
        pid = self.prontuario_repo.buscar_por_animal(id_animal)
        if not pid:
            raise KeyError("Prontuário correspondente não localizado.")

        consulta = Consulta(0, datetime.now(), valor_b, "Finalizado", ani.id, queixa, diag, presc, vet)
        total = consulta.calcular_valor_total()
        
        id_serv = self.servico_repo.criar_consulta(consulta, pid)
        
        fatura = Pagamento(0, total, "Pendente", False, id_serv)
        self.pago_repo.criar(fatura)
        return total

    def registrar_exame(self, id_animal: int, valor_b: float, tipo: str, lab: str) -> float:
        ani = self.animal_repo.buscar_por_id(id_animal)
        if not ani:
            raise KeyError("Animal inválido para a realização de exames.")
        
        pid = self.prontuario_repo.buscar_por_animal(id_animal)
        if not pid:
            raise KeyError("Prontuário correspondente não localizado.")

        exame = Exame(0, datetime.now(), valor_b, "Finalizado", ani.id, tipo, "Aguardando Laudo", lab)
        total = exame.calcular_valor_total()
        
        id_serv = self.servico_repo.criar_exame(exame, pid)
        
        fatura = Pagamento(0, total, "Pendente", False, id_serv)
        self.pago_repo.criar(fatura)
        return total

    def emitir_prontuario(self, id_animal: int) -> str:
        ani = self.animal_repo.buscar_por_id(id_animal)
        if not ani:
            raise KeyError("Animal inexistente.")
        
        pid = self.prontuario_repo.buscar_por_animal(id_animal)
        if not pid:
            return f"Nenhum prontuário físico inicializado para {ani.nome}."

        prontuario = Prontuario(pid, ani)
        servicos = self.servico_repo.listar_por_prontuario(pid, id_animal)
        for s in servicos:
            prontuario.adicionar_registro(s)
            
        return prontuario.gerar_historico_completo()

    def agendar_horario(self, dt_hora: datetime, id_cli: int, id_ani: int, id_vet: int) -> Agendamento:
        cli = self.obter_cliente(id_cli)
        ani = self.animal_repo.buscar_por_id(id_ani)
        vet = self.vet_repo.buscar_por_id(id_vet)
        if not ani or not vet:
            raise KeyError("Entidades inválidas para o agendamento.")
        
        agenda = Agendamento(0, dt_hora, "Confirmado", cli, ani, vet)
        self.agenda_repo.criar(agenda)
        return agenda

    def listar_agenda(self) -> List[Agendamento]:
        return self.agenda_repo.listar_todos()

    def listar_faturamento(self) -> List[Pagamento]:
        return self.pago_repo.listar_todos()
