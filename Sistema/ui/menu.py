import sys
from datetime import datetime, date
from services.clinica_service import ClinicaService

class TerminalUI:
    def __init__(self) -> None:
        self.service = ClinicaService()

    def exibir_menu_principal(self) -> None:
        while True:
            print("\n" + "="*45)
            print("   SISTEMA DE GESTÃO VETERINÁRIA   ")
            print("="*45)
            print("1. Gerenciamento de Clientes")
            print("2. Paciente - Cadastro de Animais")
            print("3. Cadastro de Médicos Veterinários")
            print("4. Agendamentos de Consultas/Horários")
            print("5. Atendimento Clínico (Consultas/Exames)")
            print("6. Prontuário Médico Eletrônico")
            print("7. Painel de Caixa / Faturamento Geral")
            print("0. Encerrar Software")
            print("="*45)
            opcao = input("Selecione uma operação: ").strip()

            try:
                if opcao == "1":
                    self._menu_clientes()
                elif opcao == "2":
                    self._cadastrar_animal()
                elif opcao == "3":
                    self._cadastrar_veterinario()
                elif opcao == "4":
                    self._submenu_agendamentos()
                elif opcao == "5":
                    self._submenu_atendimentos()
                elif opcao == "6":
                    self._exibir_prontuario()
                elif opcao == "7":
                    self._exibir_financeiro()
                elif opcao == "0":
                    print("\nDesligando módulos operacionais com segurança!")
                    sys.exit(0)
                else:
                    print("Opção inválida, por favor tente novamente.")
            except Exception as error:
                print(f"\n[ERRO OPERACIONAL]: {error}")

    def _menu_clientes(self) -> None:
        print("\n--- SUBMENU CLIENTES ---")
        print("1. Cadastrar Novo Cliente")
        print("2. Listar Todos os Clientes")
        print("3. Procurar Cliente por ID")
        print("4. Modificar Cadastro Existente")
        print("5. Excluir Cliente do Sistema")
        op = input("Ação: ").strip()

        if op == "1":
            nome = input("Nome Completo: ")
            cpf = input("CPF (apenas números ou formal): ")
            tel = input("Telefone de contato: ")
            email = input("E-mail: ")
            end = input("Endereço Comercial/Residencial: ")
            c = self.service.cadastrar_cliente(nome, cpf, tel, email, end)
            print(f"\nSucesso: {c}")
        elif op == "2":
            for c in self.service.listar_clientes():
                print(c)
        elif op == "3":
            idx = int(input("Informe o ID único do cliente: "))
            print(self.service.obter_cliente(idx))
        elif op == "4":
            idx = int(input("ID do Cliente a alterar: "))
            nome = input("Novo Nome Completo: ")
            cpf = input("Novo CPF: ")
            tel = input("Novo Telefone: ")
            email = input("Novo E-mail: ")
            end = input("Novo Endereço: ")
            self.service.atualizar_cliente(idx, nome, cpf, tel, email, end)
            print("\nCadastro sincronizado e atualizado com sucesso no PostgreSQL.")
        elif op == "5":
            idx = int(input("ID do Cliente a deletar permanentemente: "))
            self.service.excluir_cliente(idx)
            print("\nRegistro removido com sucesso de nossa base física.")

    def _cadastrar_animal(self) -> None:
        print("\n--- CADASTRO DE ANIMAL ---")
        tutor_id = int(input("ID do Cliente (Tutor): "))
        nome = input("Nome do Animal: ")
        especie = input("Espécie (ex: Cão, Gato): ")
        raca = input("Raça: ")
        data_string = input("Data Nascimento (DD/MM/AAAA): ")
        dt_nasc = datetime.strptime(data_string, "%d/%m/%Y").date()
        peso = float(input("Peso Atual (kg): "))
        
        ani = self.service.cadastrar_animal(nome, especie, raca, dt_nasc, peso, tutor_id)
        print(f"\nPaciente registrado com sucesso: {ani}")

    def _cadastrar_veterinario(self) -> None:
        print("\n--- CADASTRO DE VETERINÁRIO ---")
        nome = input("Nome Completo: ")
        cpf = input("CPF: ")
        tel = input("Telefone: ")
        email = input("E-mail: ")
        crmv = input("Número de Registro CRMV: ")
        espec = input("Especialidade Médica: ")
        
        v = self.service.cadastrar_veterinario(nome, cpf, tel, email, crmv, espec)
        print(f"\nProfissional Habilitado com Sucesso: {v}")

    def _submenu_agendamentos(self) -> None:
        print("\n--- PAINEL DE AGENDAMENTOS ---")
        print("1. Marcar Novo Horário na Agenda")
        print("2. Visualizar Grade de Horários")
        op = input("Ação: ").strip()

        if op == "1":
            id_c = int(input("ID do Cliente: "))
            id_a = int(input("ID do Animal: "))
            id_v = int(input("ID do Veterinário: "))
            dt_str = input("Data e Hora (DD/MM/AAAA HH:MM): ")
            dt_h = datetime.strptime(dt_str, "%d/%m/%Y %H:%M")
            ag = self.service.agendar_horario(dt_h, id_c, id_a, id_v)
            print(f"\nAlocação Efetuada com sucesso: {ag}")
        elif op == "2":
            for a in self.service.listar_agenda():
                print(a)

    def _submenu_atendimentos(self) -> None:
        print("\n--- ATENDIMENTO CLÍNICO OPERACIONAL ---")
        print("1. Registrar Execução de Consulta Geral")
        print("2. Registrar Ordem de Exame Laboratorial")
        op = input("Procedimento: ").strip()

        id_a = int(input("ID do Animal Paciente: "))
        val_b = float(input("Valor Base do Procedimento: R$ "))

        if op == "1":
            id_v = int(input("ID do Veterinário Responsável: "))
            queixa = input("Sintomas/Queixa Principal: ")
            diag = input("Diagnóstico Clínico: ")
            presc = input("Prescrição Médica Medicamentosa: ")
            tot = self.service.registrar_consulta(id_a, id_v, val_b, queixa, diag, presc)
            print(f"\nConsulta finalizada. Valor faturado total com acréscimo de 15%: R$ {tot}")
        elif op == "2":
            tipo = input("Tipo/Nome do Exame (ex: Hemograma): ")
            lab = input("Laboratório Parceiro Terceirizado: ")
            tot = self.service.registrar_exame(id_a, val_b, tipo, lab)
            print(f"\nOrdem de exame integrada. Valor total com taxa laboratorial inclusa: R$ {tot}")

    def _exibir_prontuario(self) -> None:
        print("\n--- PRONTUÁRIO ELETRÔNICO DO PACIENTE ---")
        id_a = int(input("ID do Animal para busca de histórico: "))
        historico = self.service.emitir_prontuario(id_a)
        print("\n" + historico)

    def _exibir_financeiro(self) -> None:
        print("\n--- EXTRATO CONTÁBIL DE CAIXA ---")
        faturas = self.service.listar_faturamento()
        if not faturas:
            print("Nenhuma transação financeira efetuada no período.")
            return
        total_caixa = 0.0
        for f in faturas:
            print(f)
            total_caixa += f.valor_total
        print(f"-"*40)
        print(f"Balanço bruto arrecadado em caixa: R$ {round(total_caixa, 2)}")
