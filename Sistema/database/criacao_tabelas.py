# arquivo: database/create_tables.py
from database.conexao import DBConnection

def inicializar_banco():
    """Executa scripts DDL estruturados em total conformidade com o MER fornecido."""
    ddl_queries = """
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cpf VARCHAR(14) UNIQUE NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        email VARCHAR(100) NOT NULL,
        endereco VARCHAR(200) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS veterinarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cpf VARCHAR(14) UNIQUE NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        email VARCHAR(100) NOT NULL,
        crmv VARCHAR(20) UNIQUE NOT NULL,
        especialidade VARCHAR(50) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS animais (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        especie VARCHAR(50) NOT NULL,
        raca VARCHAR(50) NOT NULL,
        data_nascimento DATE NOT NULL,
        peso NUMERIC(5,2) NOT NULL,
        cliente_id INT NOT NULL,
        CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS prontuarios (
        id SERIAL PRIMARY KEY,
        animal_id INT UNIQUE NOT NULL,
        CONSTRAINT fk_animal_prontuario FOREIGN KEY (animal_id) REFERENCES animais(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS servicos (
        id SERIAL PRIMARY KEY,
        tipo VARCHAR(20) NOT NULL,
        data_hora TIMESTAMP NOT NULL,
        valor_base NUMERIC(10,2) NOT NULL,
        status VARCHAR(20) NOT NULL,
        prontuario_id INT NOT NULL,
        queixa_principal TEXT,
        diagnostico TEXT,
        prescricao TEXT,
        veterinario_id INT,
        tipo_exame VARCHAR(100),
        resultado TEXT,
        laboratorio_parceiro VARCHAR(100),
        CONSTRAINT fk_prontuario_servico FOREIGN KEY (prontuario_id) REFERENCES prontuarios(id) ON DELETE CASCADE,
        CONSTRAINT fk_vet_servico FOREIGN KEY (veterinario_id) REFERENCES veterinarios(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS pagamentos (
        id SERIAL PRIMARY KEY,
        valor_total NUMERIC(10,2) NOT NULL,
        forma_pagamento VARCHAR(30) NOT NULL,
        pago BOOLEAN NOT NULL DEFAULT FALSE,
        servico_id INT NOT NULL UNIQUE,
        CONSTRAINT fk_servico_pagamento FOREIGN KEY (servico_id) REFERENCES servicos(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS agendamentos (
        id SERIAL PRIMARY KEY,
        data_hora TIMESTAMP NOT NULL,
        status VARCHAR(20) NOT NULL,
        cliente_id INT NOT NULL,
        animal_id INT NOT NULL,
        veterinario_id INT NOT NULL,
        CONSTRAINT fk_agendamento_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
        CONSTRAINT fk_agendamento_animal FOREIGN KEY (animal_id) REFERENCES animais(id) ON DELETE CASCADE,
        CONSTRAINT fk_agendamento_vet FOREIGN KEY (veterinario_id) REFERENCES veterinarios(id) ON DELETE CASCADE
    );
    """
    with DBConnection.get_cursor() as cursor:
        cursor.execute(ddl_queries)
