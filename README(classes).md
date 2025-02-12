# -Human-Resources-Management-System-2.0

Classes: 

- Funcionário: a classe funcionário armazena as subclasses informações, avaliação e pagamento, é por sua vez será armazenada em uma lista de funcionários
- Informações: a classe informações é uma subclasse que armazena informações sobre o funcionário a qual ela pertence, como nome, idade, cargo, salario total, salario base, beneficios totais, descontos totais, horarios e etc..
- Avaliação: a classe avaliação é uma subclasse que armazena a avaliação sobre o funcionario a qual pertence, como sua nota como usuario, descrição de seu desempenho e número de faltas
- Pagamentos: a classe pagamentos é uma subclasse que armazena informações uma lista dos beneficios e descontos que o funcionário poderá receber (tais beneficios e descontos automaticamente irá modificar o salário total do funcionário)
- beneficios e descontos: a classe beneficios e descontos armazena uma lista de beneficios e uma lista de descontos e o número total de cada um deles
- beneficio: a classe beneficios é uma classe que armazena o nome e a forma de aumento salarial (percentual, multiplicativo ou fixo)
- descontos: a classe descontos é uma classe que armazena o nome e a forma de diminuição salarial (percentual, multiplicativo ou fixo) 

Funções que fazem uso do class: 
- Adicionar_Informação(novo_funcionário.informações): preenche os dados na subclasse funcionário
- Realizar_Avaliação_Funcionário(novo_funcionário): preenche os dados na subclasse avaliação
- Registrar_Beneficios(novo_funcionário): preenche os dados na subclasse beneficios 
