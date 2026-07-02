
# Possíveis Classes

- **Pessoa (Abstrata):** Centraliza os dados cadastrais básicos comuns a qualquer ser humano que interaja com o sistema. É uma classe pois encapsula o estado de identificação e contato básico do ecossistema.

- **Cliente:** Representa o tutor dos animais, responsável legal pelos pagamentos e autorizações. Deve ser uma classe porque possui comportamentos próprios (como gerenciar seus animais cadastrados) e regras de negócio associadas à sua adimplência financeira.

- **Veterinário:** O profissional técnico que realiza os atendimentos, consultas e solicitações de exames. É mapeado como classe para rastrear sua habilitação legal (CRMV), especialidades e vincular a responsabilidade técnica pelas ações clínicas.

- **Animal:** O paciente da clínica. É uma classe essencial que armazena o histórico biológico, raça, espécie e idade do animal, funcionando como o núcleo ao qual os cuidados médicos são direcionados.

- **Serviço**: Generalização de qualquer procedimento cobrável e executável na clínica. Torna-se classe para permitir a extensão unificada de faturamento e registro histórico.

- **Consulta:** Tipo específico de serviço focado na avaliação do paciente. É uma classe pois possui atributos clínicos particulares, como relato de sintomas e anamnese.

- **Exame:** Procedimento diagnóstico complementar. É uma classe porque possui um fluxo próprio de coleta, processamento de resultados, valores laboratoriais de referência e emissão de laudos.

- **Pagamento:** Entidade financeira responsável por processar a liquidação dos valores dos serviços prestados. É uma classe para isolar a lógica fiscal e contábil do restante dos fluxos clínicos (SRP).

--------------------------------------------------------------------------
# Hierarquias e Abstração

#### Hierarquia de Atores (Pessoas)

- **Superclasse:** `Pessoa` (Classe Abstrata)
- **Subclasses:** `Cliente` e `Veterinario`
- **Análise:** `Cliente` **é uma** Pessoa; `Veterinario` **é uma** Pessoa. Ambos herdam o mecanismo de identificação (Nome, CPF, Telefone), mas o `Cliente` estende a classe com dados de cobrança, enquanto o `Veterinario` estende com o registro profissional (CRMV).

#### Hierarquia de Procedimentos (Serviços)

- **Superclasse:** `Servico` (Classe Abstrata)
- **Subclasses:** `Consulta` e `Exame`
- **Análise:** `Consulta` **é um** Serviço; `Exame` **é um** Serviço. Ambos compartilham data, hora e valor base, mas a `Consulta` se especializa em diagnóstico clínico direto, e o `Exame` se especializa em resultados laboratoriais e laudos técnicos.

--------------------------------------------------------------------------
# Especificação de cada Classe

### Classe: Pessoa (Abstrata)

**Descrição:** Superclasse abstrata que serve de base para o cadastro de todas as pessoas do sistema.

**Atributos:**
- `id`: int (protegido) — Identificador único da pessoa.
- `nome`: String (protegido) — Nome completo.
- `cpf`: String (protegido) — Cadastro de Pessoa Física para validação e contratos.
- `telefone`: String (protegido) — Número de contato principal.
- `email`: String (protegido) — Endereço eletrônico para notificações.

**Métodos:**
- `validarCpf()`: boolean (protegido) — Executa o algoritmo de validação do CPF.
- `atualizarContato(novoTelefone: String, novoEmail: String)`: void (público) — Modifica os dados de contato do indivíduo.

### Classe: Cliente

**Descrição:** Especialização de Pessoa, representando o tutor dos animais cadastrados na clínica.

**Atributos:**
- `endereco`: String (privado) — Endereço residencial para fins de cobrança/entrega.
- `animais`: List< Animal > (privado) — Lista de animais vinculados a este tutor.

**Métodos:**
- `vincularAnimal(animal: Animal)`: void (público) — Associa um novo animal ao cadastro do cliente.
- `removerAnimal(animal: Animal)`: void (público) — Desvincula um animal do cliente (mantendo a integridade histórica).

### Classe: Veterinario

**Descrição:** Especialização de Pessoa, representando o médico veterinário responsável pelos atendimentos.

**Atributos:**
- `crmv`: String (privado) — Registro no Conselho Regional de Medicina Veterinária.
- `especialidade`: String (privado) — Área de especialização médica (ex: Dermatologia, Oncologia).

**Métodos:**
- `emitirLaudo(descricao: String)`: String (público) — Gera um texto formal assinado digitalmente com o CRMV do profissional.

### Classe: Animal

**Descrição:** Entidade que armazena os dados biológicos e cadastrais do paciente animal.

**Atributos:**
- `id`: int (privado) — Identificador único do paciente.
- `nome`: String (privado) — Nome do animal.
- `especie`: String (privado) — Espécie do animal (ex: Cão, Gato).
- `raca`: String (privado) — Raça do animal.
- `dataNascimento`: Date (privado) — Data de nascimento do animal para cálculo dinâmico da idade.
- `peso`: double (privado) — Peso atual em quilogramas.

**Métodos:**
- `calcularIdade()`: int (público) — Retorna a idade do animal calculada a partir da data atual e da data de nascimento.
- `atualizarPeso(novoPeso: double)`: void (público) — Atualiza o peso do paciente durante os atendimentos.

### Classe: Agendamento

**Descrição:** Entidade responsável por gerenciar a reserva de horários para a realização de serviços.

**Atributos:**
- `id`: int (privado) — Identificador do agendamento.
- `dataHora`: Date (privado) — Data e horário marcados.
- `status`: String (privado) — Estado atual (Pendente, Confirmado, Cancelado, Concluído).
- `cliente`: Cliente (privado) — Referência ao tutor do animal.
- `animal`: Animal (privado) — Referência ao paciente.
- `veterinario`: Veterinario (privado) — Referência ao profissional escolhido.

**Métodos:**
- `confirmarAgendamento()`: void (público) — Altera o status para "Confirmado".
- `cancelarAgendamento(motivo: String)`: void (público) — Cancela o agendamento e libera o horário do veterinário na agenda.

### Classe: Prontuario

**Descrição:** Registro central imutável que agrega todo o histórico clínico do animal.

**Atributos:**
- `id`: int (privado) — Identificador do prontuário.
- `animal`: Animal (privado) — O paciente dono deste histórico.
- `historicoServicos`: List< Servico > (privado) — Lista cronológica de todas as consultas e exames realizados.

**Métodos:**
- `adicionarRegistro(servico: Servico)`: void (público) — Insere uma nova consulta ou exame finalizado ao prontuário do animal.
- `gerarHistoricoCompleto()`: String (público) — Compila textualmente todas as ocorrências clínicas em ordem cronológica reversa.

### Classe: Servico (Abstrata)

**Descrição:** Superclasse abstrata que unifica os atributos e comportamentos financeiros/temporais de qualquer intervenção clínica.

**Atributos:**
- `id`: int (protegido) — Identificador do serviço.
- `dataHora`: Date (protegido) — Data e hora da realização do serviço.
- `valorBase`: double (protegido) — Preço base do procedimento.
- `status`: String (protegido) — Estado do serviço (Em Andamento, Finalizado, Cancelado).

**Métodos:**
- `calcularValorTotal()`: double (público, abstrato) — Método polimórfico que deve ser sobrescrito para calcular o preço final com taxas adicionais ou insumos.
- `finalizarServico()`: void (público) — Altera o status para "Finalizado".

### Classe: Consulta

**Descrição:** Especialização de Serviço destinada ao atendimento inicial e diagnóstico.

**Atributos:**
- `queixaPrincipal`: String (privado) — Sintomas relatados pelo tutor.
- `diagnostico`: String (privado) — Conclusão médica dada pelo veterinário.
- `prescricao`: String (privado) — Medicamentos e dosagens indicadas.
- `veterinario`: Veterinario (privado) — O profissional que executou a consulta.

**Métodos:**
- `calcularValorTotal()`: double (público) — Sobrescrita do método. Retorna o `valorBase` somado a possíveis taxas de plantão ou emergência.
- `registrarAnamnese(queixa: String, diagnostico: String)`: void (público) — Alimenta as informações técnicas da consulta.

### Classe: Exame

**Descrição:** Especialização de Serviço focada em exames laboratoriais ou de imagem.

**Atributos:**
- `tipoExame`: String (privado) — Nome do exame (ex: Hemograma, Raio-X).
- `resultado`: String (privado) — Laudo ou dados brutos do resultado.
- `laboratorioParceiro`: String (privado) — Nome do laboratório externo, caso aplicável.

**Métodos:**
- `calcularValorTotal()`: double (público) — Sobrescrita do método. Adiciona o custo do insumo laboratorial ao `valorBase`.
- `atualizarResultado(laudo: String)`: void (público) — Insere o resultado final do exame e encerra o fluxo do procedimento.

### Classe: Pagamento

**Descrição:** Classe responsável pelo processamento financeiro e faturamento dos serviços concluídos.

**Atributos:**

- `id`: int (privado) — Identificador da transação.
- `valorTotal`: double (privado) — Valor final a ser pago.
- `formaPagamento`: String (privado) — Método utilizado (Dinheiro, Cartão, Pix).
- `pago`: boolean (privado) — Indicador de status do pagamento (True/False).
- `servico`: Servico (privado) — O serviço associado que originou a cobrança.

**Métodos:**
- `processarPagamento()`: boolean (público) — Conecta-se à regra de faturamento e altera o atributo `pago` para verdadeiro se bem-sucedido.

--------------------------------------------------------------------------
# Relacionamentos entre Classes

A tabela a seguir consolida a malha de interações estruturais do sistema de acordo com as regras de negócio clínicas.

| **Classe Origem** | **Classe Destino** | **Tipo de Relacionamento** | **Multiplicidade** | **Descrição do Motivo**                                                                                                                         |
| ----------------- | ------------------ | -------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `Pessoa`          | `Cliente`          | Herança                    | N/A                | `Cliente` herda a estrutura básica de dados pessoais.                                                                                           |
| `Pessoa`          | `Veterinario`      | Herança                    | N/A                | `Veterinario` herda a estrutura básica de dados pessoais.                                                                                       |
| `Servico`         | `Consulta`         | Herança                    | N/A                | `Consulta` é uma especialização de `Servico`.                                                                                                   |
| `Servico`         | `Exame`            | Herança                    | N/A                | `Exame` é uma especialização de `Servico`.                                                                                                      |
| `Cliente`         | `Animal`           | Associação                 | 1 : 1..*           | Um cliente possui um ou vários animais. O animal precisa de um tutor vinculado.                                                                 |
| `Animal`          | `Prontuario`       | Composição                 | 1 : 1              | O prontuário pertence exclusivamente a um animal. Se o animal for excluído, seu prontuário deixa de fazer sentido existencial no sistema ativo. |
| `Prontuario`      | `Servico`          | Agregação                  | 1 : 0..*           | O prontuário agrupa múltiplos serviços (`Consulta`/`Exame`). Os serviços existem independentemente do prontuário, mas são nele referenciados.   |
| `Agendamento`     | `Cliente`          | Associação                 | * : 1              | Vários agendamentos podem ser criados por um único cliente.                                                                                     |
| `Agendamento`     | `Animal`           | Associação                 | * : 1              | Vários agendamentos podem referenciar um mesmo animal ao longo do tempo.                                                                        |
| `Agendamento`     | `Veterinario`      | Associação                 | * : 1              | Um veterinário atende múltiplos agendamentos ao longo de sua escala de trabalho.                                                                |
| `Servico`         | `Pagamento`        | Composição                 | 1 : 1              | Cada serviço gera exatamente uma transação de pagamento associada diretamente ao seu fechamento.                                                |

--------------------------------------------------------------------------
## Aplicação dos Princípios da Programação Orientada a Objetos

**Encapsulamento:** Todos os atributos críticos das classes foram definidos com visibilidade privada (`privado`) ou protegida (`protegido`). O acesso e a alteração desses estados ocorrem estritamente por meio de métodos públicos de negócio (ex: `atualizarPeso`, `confirmarAgendamento`). Isso impede que o estado de um objeto seja corrompido externamente.

**Abstração:** As classes `Pessoa` e `Servico` foram isoladas como estruturas abstratas. Elas representam conceitos genéricos do domínio que não devem ser instanciados diretamente, focando apenas nas assinaturas e comportamentos fundamentais compartilhados por suas especializações.

**Herança:** Utilizada de forma limpa nas árvores de `Pessoa` e `Servico`. Ela evita a duplicação de código. Atributos comuns como `nome`, `cpf` ou `valorBase` são herdados automaticamente pelas subclasses, permitindo reaproveitamento estrutural completo.

**Polimorfismo:** Evidenciado no método abstrato `calcularValorTotal()` da superclasse `Servico`. Tanto `Consulta` quanto `Exame` implementam esse método com suas lógicas específicas de negócio. O sistema de faturamento pode tratar qualquer objeto derivado de `Servico` de forma genérica e disparar o cálculo correto em tempo de execução de forma transparente.

**Princípio da Responsabilidade Única (SRP):** Cada classe cuida apenas do seu contexto. `Prontuario` gerencia o histórico e não se envolve com regras de faturamento, enquanto a classe `Pagamento` isola completamente o fluxo financeiro da clínica, não sabendo como uma consulta é clinicamente diagnosticada.

--------------------------------------------------------------------------
# Representação Visual da Estrutura de Classes
