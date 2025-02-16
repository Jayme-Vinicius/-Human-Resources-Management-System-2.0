# Sistema de Gerenciamento de RH

## Classes

### Funcionários
Classe principal que representa um funcionário, contendo três subclasses:
- informações (dados pessoais e profissionais)
- avaliação (métricas de desempenho)
- pagamento (benefícios e descontos)

### Informação
Armazena dados básicos do funcionário:
- nome, idade, função, salário base, salário total, horários e status
- usa "N/D" (Não Disponível) como valor padrão para campos de texto
- usa "0" como valor padrão para campos numéricos

### Avaliação
Guarda dados de performance do funcionário:
- nota de avaliação
- descrição do desempenho
- número de faltas

### Pagamento
Gerencia informações financeiras:
- total de benefícios e lista de benefícios
- total de descontos e lista de descontos

### Beneficio e Desconto
Classes similares que controlam alterações no salário:
- nome do benefício/desconto
- tipo de alteração (percentual, multiplicativo ou somativo)
- valor da alteração

## Funções

### Gestão de Funcionários

#### Adicionar_funcionário
- Cadastra novos funcionários no sistema
- Permite entrada contínua de dados até o usuário optar por sair

#### Remover_Funcionário
- Remove funcionários do sistema
- Permite remoção individual ou em massa

#### Adicionar_Informação
- Coleta dados básicos do funcionário
- Registra informações como nome, idade, função, etc.

#### Atualizar_Informações
- Permite modificar dados existentes
- Pode atualizar um funcionário específico ou todos

#### Print_Informação_Funcionários
- Exibe dados dos funcionários
- Pode mostrar um funcionário específico ou listar todos

### Sistema de Avaliação

#### Realizar_Avaliação_Funcionário
- Registra nova avaliação
- Permite avaliar um funcionário específico ou todos

#### Avaliação_funcionário
- Coleta dados da avaliação
- Registra nota, descrição e faltas

#### Print_Avaliação_Funcionários
- Mostra avaliações registradas
- Pode exibir uma avaliação específica ou todas

### Gestão de Benefícios

#### Adicionar_Beneficios
- Cria novos tipos de benefícios
- Registra nome, tipo e valor do benefício

#### Remover_Beneficios
- Remove benefícios existentes
- Permite remoção individual ou em massa

#### Print_Lista_de_Beneficios
- Lista benefícios disponíveis
- Pode mostrar um benefício específico ou todos

#### Registrar_Beneficio_de_funcionários
- Associa benefícios a funcionários
- Pode registrar para um funcionário específico ou todos

### Gestão de Descontos

#### Adicionar_Descontos
- Cria novos tipos de descontos
- Registra nome, tipo e valor do desconto

#### Remover_Descontos
- Remove descontos existentes
- Permite remoção individual ou em massa

#### Print_Lista_de_Descontos
- Lista descontos disponíveis
- Pode mostrar um desconto específico ou todos

#### Registrar_Desconto_de_Funcionários
- Associa descontos a funcionários
- Pode registrar para um funcionário específico ou todos

### Cálculos Salariais

#### Calcular_Salario_Total_Funcionários
- Calcula salário final considerando benefícios e descontos
- Pode calcular para um funcionário específico ou todos

#### Calcular_Beneficios_totais
- Soma todos os benefícios aplicáveis
- Considera diferentes tipos de cálculo (percentual, multiplicativo, somativo)

#### Calcular_Descontos_totais
- Soma todos os descontos aplicáveis
- Considera diferentes tipos de cálculo (percentual, multiplicativo, somativo)

## Visão Geral do Sistema

O sistema funciona como um gerenciador completo de recursos humanos, oferecendo:
- Cadastro e gerenciamento de funcionários
- Sistema de avaliação de desempenho
- Gestão de benefícios e descontos
- Cálculo automatizado de salários
- Geração de relatórios e visualização de dados

Todas as operações podem ser realizadas tanto individualmente quanto em massa, permitindo uma gestão eficiente de equipes de qualquer tamanho.
