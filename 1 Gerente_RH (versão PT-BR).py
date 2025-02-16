import Funções

print("Olá seja bem vindo ao gerenciador de RH\n")
lista_de_funcionários = []
número_de_funcionários = 0
lista_de_beneficios = []
número_de_beneficios = 0
lista_de_descontos = []
número_de_descontos = 0
while (1):
    choice_1 = (input("""
Selecione a opção que desejar:
Visualizar opções(0)\n\n"""))
    match choice_1:
        case '0':
            print("""
Visualizar sobre Funcionários(1)
Visualizar Sobre Pagamentos, Beneficios e Descontos(2)
Sair(-1)\n""")
        case '1':
            choice_2 = (input("""
Visualizar Lista de Funcionários (1)
Contratar Funcionários (2)
Demitir Funcionários (3)
Atualizar o Perfil dos Funcionários(4)
Ver Avaliação Funcionários(5)                              
Avaliar os Funcionários(6)
Voltar(-1)\n\n"""))
            match choice_2:
                case '1':
                    lista_de_funcionários = Funções.Print_Informação_Funcionários(lista_de_funcionários, número_de_funcionários)
                case '2':
                    lista_de_funcionários, número_de_funcionários = Funções.Adicionar_funcionário(lista_de_funcionários, número_de_funcionários)
                case '3':
                    lista_de_funcionários, número_de_funcionários = Funções.Remover_Funcionário(lista_de_funcionários, número_de_funcionários)
                case '4':
                    lista_de_funcionários = Funções.Atualizar_Informações(lista_de_funcionários, número_de_funcionários)
                case '5':
                    lista_de_funcionários = Funções.Print_Avaliação_Funcionários(lista_de_funcionários, número_de_funcionários)
                case '6':
                    lista_de_funcionários = Funções.Realizar_Avaliação_Funcionário(lista_de_funcionários, número_de_funcionários)
                case '-1':
                    continue
                case _:
                    print("Opção invalida\n\n")
        case '2':
            choice_2 = (input("""
Calcular Salario Total(1)
Registrar Beneficio dos Funcionários (2)
Ver Lista de Beneficios (3)                             
Adicionar Beneficios (4)
Remover Beneficios (5)
Registrar Desconto dos Funcionários (6)
Ver Lista de Beneficios (7)                              
Adicionar Descontos (8)
Remover Descontos (9)
Voltar(-1)\n\n"""))
            match choice_2:
                case '1':
                    lista_de_funcionários = Funções.Calcular_Salario_Total_Funcionários(lista_de_funcionários, número_de_funcionários, lista_de_beneficios, lista_de_descontos, número_de_beneficios, número_de_descontos)
                case '2':
                    lista_de_funcionários = Funções.Registrar_Beneficio_de_funcionários(lista_de_funcionários, lista_de_beneficios, número_de_funcionários, número_de_beneficios)
                case '3':
                    lista_de_beneficios = Funções.Print_Lista_de_Beneficios(lista_de_beneficios, número_de_beneficios)
                case '4':
                    lista_de_beneficios, número_de_beneficios = Funções.Adicionar_Beneficios(lista_de_funcionários, lista_de_beneficios, número_de_funcionários, número_de_beneficios)
                case '5':
                    lista_de_beneficios, número_de_beneficios = Funções.Remover_Beneficios(lista_de_funcionários, lista_de_beneficios, número_de_funcionários, número_de_beneficios)
                case '6':
                    lista_de_funcionários = Funções.Registrar_Desconto_de_Funcionários(lista_de_funcionários, lista_de_descontos, número_de_funcionários, número_de_descontos)
                case '7':
                    lista_de_descontos = Funções.Print_Lista_de_Descontos(lista_de_descontos, número_de_descontos)
                case '8':
                    lista_de_descontos, número_de_descontos = Funções.Adicionar_Descontos(lista_de_funcionários, lista_de_descontos, número_de_funcionários, número_de_descontos)
                case '9':
                    lista_de_descontos, número_de_descontos = Funções.Remover_Descontos(lista_de_funcionários, lista_de_descontos, lista_de_funcionários, lista_de_descontos)
        case '-1':
            print("Obrigado pela preferencia :)")
            break
        case '_':
            print("Opção invalida")
