<div align="center">

# Sistema de Clínica Veterinária


![Static Badge](https://img.shields.io/badge/Python-POO-blue?style=flat&logo=python&logoColor=white&labelColor=yellow&color=blue)


</div>

## Informações

Projeto: Trabalho final apresentado à disciplina de Programação Orientada a Objetos.

**Integrantes:**
- Davi Vitor Santos Mota - 22552367
- Isabely Cristina Barbosa Beça - 22551984
- Vicktor Eduardo Almeida Pinheiro - 22552978

## Resumo do Projeto

O Sistema de Gestão Veterinária é o projeto final desenvolvido para a disciplina de Programação Orientada a Objetos (POO), com o objetivo de aplicar os principais conceitos estudados ao longo da matéria, como encapsulamento, herança, polimorfismo, abstração e organização em classes. O projeto simula o funcionamento de uma clínica veterinária por meio de uma aplicação simples e integrada a um banco de dados.

O sistema permite gerenciar clientes, cadastrar médicos veterinários e animais, realizar agendamentos de consultas, controlar atendimentos e prontuários, além de gerar informações financeiras e executar outras funcionalidades essenciais para a administração da clínica. Dessa forma, o projeto demonstra a aplicação prática dos conceitos de POO no desenvolvimento de um sistema organizado, funcional e de fácil manutenção.

## Como Rodar
### Ferramentas Necessárias
Antes de executar o projeto, é necessário ter os seguintes recursos instalados:

---

**Python 3.x** (versão utilizada no desenvolvimento do projeto);

**Uma IDE** de sua preferência, como Visual Studio Code, PyCharm ou outra compatível com Python;

**PostgreSQL**, utilizado como banco de dados da aplicação.

---

O projeto está configurado para se conectar ao banco de dados utilizando os seguintes parâmetros padrão:

Parâmetro	Valor
Host	localhost
Banco de Dados	vetsys_db
Usuário	postgres
Senha	172236
Porta	5432

Caso sua configuração seja diferente, basta alterar os valores da classe DBConnection ou definir as variáveis de ambiente correspondentes (DB_HOST, DB_NAME, DB_USER, DB_PASS e DB_PORT).

### Executando o Sistema
O projeto pode ser executado de duas maneiras diferentes, conforme a preferência do usuário.

## Opção 1 — Utilizando uma IDE

1. Clone o repositório utilizando o Git:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

   Ou utilize o **GitHub Desktop** para clonar o projeto.

2. Abra a pasta do projeto em uma IDE de sua preferência (Visual Studio Code, PyCharm, entre outras).

3. Navegue até a pasta `ui` e execute o arquivo `menu.py`.

A organização do projeto está estruturada da seguinte forma:

<img width="216" height="726" alt="image" src="https://github.com/user-attachments/assets/20bb89d3-2c17-4284-93c1-fc3663cfd62c" />

As principais pastas são:

- **database/** — Responsável pela conexão com o banco de dados e criação das tabelas.
- **models/** — Contém as classes que representam as entidades do sistema.
- **repositories/** — Responsável pelas operações de acesso ao banco de dados (CRUD).
- **service/** — Implementa as regras de negócio da aplicação.
- **ui/** — Interface do sistema, contendo o arquivo `menu.py`, responsável por iniciar a aplicação.

---

## Opção 2 — Executando pelo Terminal (CMD)

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd Sistema
   ```

3. Entre na pasta da interface:

   ```bash
   cd ui
   ```

4. Execute o sistema:

   ```bash
   python menu.py
   ```

> **Observação:** Antes de iniciar o sistema, certifique-se de que o PostgreSQL esteja em execução e configurado corretamente, conforme descrito na seção **Ferramentas Necessárias**.

