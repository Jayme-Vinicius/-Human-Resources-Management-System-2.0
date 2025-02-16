class Funcionários():
    def __init__(self):
        self.informações = Informação()
        self.avaliação = Avaliação()
        self.pagamento = Pagamento()

class Informação():
    def __init__(self):
        self.nome = "N/D"
        self.idade = "N/D"
        self.função = "N/D"
        self.salario = "0"
        self.salario_total = "N/D"
        self.horarios = "N/D"
        self.status = "N/D"

class Avaliação():
    def __init__(self):
        self.nota = "0"
        self.descrição = "N/D"
        self.faltas = "0"

class Pagamento():
    def __init__(self):
        self.beneficios_totais = "0"
        self.beneficios = []
        self.descontos_totais = "0" 
        self.descontos = []

class Beneficio():
    def __init__(self):
     self.nome = "N/D"
     self.tipo_de_aumento = "N/D"
     self.quantia = "0"

class Desconto():
    def __init__(self):
        self.nome = "N/D"
        self.tipo_de_aumento = "N/D"
        self.quantia = "0"

def Adicionar_funcionário(lista_de_funcionários, número_de_funcionários):
    while True:
        novo_funcionário = Funcionários()
        Adicionar_Informação(novo_funcionário)
        lista_de_funcionários.append(novo_funcionário)
        número_de_funcionários = número_de_funcionários + 1 
        while True:
            choice = (input("Deseja continuar Contratando funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários, número_de_funcionários
                case '1':  
                    break
                case _:
                    print("Opção invalida\n")  
                    continue        

def Remover_Funcionário(lista_de_funcionários, número_de_funcionários):
        if lista_de_funcionários == []:
            print("Não tem funcionários cadastrados até o momento\n")
            return
        while True:
            busca = input("Deseja Demitir Todos os Funcionários ou apenas um funcionários especifico\n\n").strip().lower() 
            funcionário_demitido = 0
            if busca == "todos":
                for indice in range(0 , número_de_funcionários):
                    lista_de_funcionários.pop(indice)
                    número_de_funcionários = número_de_funcionários - 1
            else:
                for indice in range(0 , número_de_funcionários):
                    if lista_de_funcionários[indice].informações.nome == busca:
                        print(f"O Funcionário {lista_de_funcionários[indice].informações.nome} foi Demitido\n")
                        lista_de_funcionários.pop(indice)
                        número_de_funcionários = número_de_funcionários - 1
                        funcionário_demitido = 1
                        break
            if funcionário_demitido == 0:
                print(f"O Funcionário {busca} não foi encontrado, tente outra vez\n")
            while True:
                choice = (input("Deseja continuar Demitindo Funcionarios(1)\nDeseja sair(-1)\n\n"))
                match choice:
                    case '-1':
                        return lista_de_funcionários, número_de_funcionários
                    case '1':
                        break
                    case _:
                        print("Opção invalida")
                        continue         
                        
            
def Adicionar_Informação(informações_funcionário):
    informações_funcionário.informações.nome = input("Nome completo do funcionário: ")
    informações_funcionário.informações.idade = input("idade do funcionário: ")
    informações_funcionário.informações.função = input("função do funcionário: ")
    informações_funcionário.informações.salario = input("salario do funcionário: ")
    informações_funcionário.informações.horarios = input("carga horaria do funcionário: ")
    informações_funcionário.informações.status  = "Ativo"

def Atualizar_Informações(lista_de_funcionários, número_de_funcionários):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    while True:
        busca = input("Deseja atualizas as informações todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        funcinário_atualizado = 0
        if busca == "todos":
            for indice in range (0, número_de_funcionários):
                Adicionar_Informação(lista_de_funcionários[indice])         
        else:
            for indice in range (0, número_de_funcionários):
                if lista_de_funcionários[indice].informações.nome == busca:
                    Adicionar_Informação(lista_de_funcionários[indice])
                    print(f"O Funcionário {lista_de_funcionários[indice].informações.nome} teve suas informações atualizadas\n")
                    funcinário_atualizado = 1
                    break
            if funcinário_atualizado == 0:
                print(f"O Funcionário {busca} nã ofoi encontrado\n")
        while True:
            choice = (input("Deseja continuar atualizando informações dos funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':  
                    break   
                case _:
                    print("Opção invalida")
                    continue
            
def Realizar_Avaliação_Funcionário(lista_de_funcionários, número_de_funcionários):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    while True:
        busca = input("Deseja avaliar todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        funcionário_avaliado = 0
        if busca == "todos":
            for indice in range(0, número_de_funcionários):
                Avaliação_funcionário(lista_de_funcionários[indice])      
        else:
            for indice in range(0, número_de_funcionários):
                if lista_de_funcionários[indice].informações.nome == busca:
                    Avaliação_funcionário(lista_de_funcionários[indice])
                    print(f"O Funcionário {lista_de_funcionários[indice].informações.nome} foi avaliado\n")
                    funcionário_avaliado = 1
            if funcionário_avaliado == 0:
                print(f"O Funcionário {busca} não foi encontrado\n")
        while True:
            choice = (input("Deseja continuar avaliando funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue        

def Avaliação_funcionário(funcionário_avaliado):
    funcionário_avaliado.avaliação.nota = input(f"Em uma escala de zero a dez como você avaliaria o funcionário {funcionário_avaliado.informações.nome}:")
    funcionário_avaliado.avaliação.descrição = input(f"como você descreveria o funcionário {funcionário_avaliado.informações.nome}:")
    funcionário_avaliado.avaliação.faltas = input(f"quantas faltas o funcionário {funcionário_avaliado.informações.nome} teve nesse mês:")               

def Adicionar_Beneficios(lista_de_funcionários, lista_de_beneficios, número_de_funcionários, número_de_beneficios):
    while True:
        novo_beneficio = Beneficio()
        Adicionar_Beneficio(novo_beneficio)
        lista_de_beneficios.append(novo_beneficio)
        número_de_beneficios = número_de_beneficios + 1
        for indice in range(0 , número_de_funcionários):
            lista_de_funcionários[indice].pagamento.beneficios.append(0)
        while True:
            choice = (input("Deseja continuar Adicionando Beneficios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_beneficios, número_de_beneficios
                case '1':  
                    break
                case _:
                    print("Opção invalida\n\n")  
                    continue  

def Adicionar_Beneficio(beneficio):
    beneficio.nome = input("Nome Do Beneficio: ")
    while True:    
        beneficio.tipo_de_aumento = input("""Tipo de Aumento do Beneficio Será:
        "Percentual(%)"
        "Multiplicatio(*)"
        "Somativo(+)":""")
        if beneficio.tipo_de_aumento == "%" or "*" or "+":
                break
        else:
            print("Opção invalida")
    beneficio.quantia = input("Quantia desse Aumento: ")

def Remover_Beneficios(lista_de_funcionários, lista_de_beneficios, número_de_funcionários, número_de_beneficios):
    if lista_de_beneficios == []:
        print("Nenhum Beneficio foi Adicionado até o momento\n\n")
        return
    while True:
        busca = input("Deseja Remover todos os Beneficios ou apenas um Beneficio especifico\n\n").strip().lower() 
        beneficio_deletado = 0
        if busca == "todos":
            for indice_1 in range(0 , número_de_beneficios):
                lista_de_beneficios.pop(indice_1)
                número_de_beneficios = número_de_beneficios - 1
                for indice_2 in range(0 , número_de_funcionários):
                    lista_de_funcionários[indice_2].pagamento.beneficios.pop(indice_1)
        else:
            for indice_1 in range(0 , número_de_beneficios):
                if lista_de_beneficios[indice_1].informações.nome == busca:
                    print(f"O Beneficio {lista_de_beneficios[indice_1].nome} foi Deletado\n")
                    lista_de_beneficios.pop(indice_1)
                    número_de_beneficios = número_de_beneficios - 1
                    beneficio_deletado = 1
                    for indice_2 in range(0 , número_de_funcionários):
                        lista_de_funcionários[indice_2].pagamento.beneficios.pop(indice_1)
                    break
        if beneficio_deletado == 0:
            print(f"O Beneficio {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar Removendo Beneficios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_beneficios, número_de_beneficios
                case '1':
                    break
                case _:
                    print("Opção invalida")
                    continue 
        
def Print_Lista_de_Beneficios(lista_de_beneficios, número_de_beneficios):
    if lista_de_beneficios == []:
        print("Nenhum Beneficio foi Adicionado até o momento\n\n")
        return
    while True:
        busca = input("Deseja ver todos os beneficios ou apenas um beneficio especifico\n\n").strip().lower()
        beneficio_encontrado = 0
        if busca == "todos":
            for indice in range (0 , número_de_beneficios):
                Print_Beneficio(lista_de_beneficios[indice])
        else:
            for indice in range(0, número_de_beneficios):
                if lista_de_beneficios[indice].informações.nome == busca:
                    beneficio_encontrado = 1
                    Print_Beneficio(lista_de_beneficios[indice])
                    break
        if beneficio_encontrado == 0 and busca != "todos":
            print(f"O Beneficio {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar buscando beneficios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_beneficios
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue

def Print_Beneficio(beneficio):
    print(f"""
    Nome: {beneficio.nome}
    Tipo de Aumento: {beneficio.tipo_de_aumento}
    Quantia: {beneficio.quantia}\n""")

def Registrar_Beneficio_de_funcionários(lista_de_funcionários, lista_de_beneficios, número_de_funcionários, número_de_beneficios):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    if lista_de_beneficios == []:
        print("Nenhum Beneficio foi Adicionado até o momento\n\n")
        return
    while True:
        busca = input("Deseja Registrar os Beneficios de Todos os Funcionários ou apenas os Beneficios de um Funcionário especifico\n\n").strip().lower()
        funcionário_beneficiado = 0
        if busca == "todos":
            for indice_1 in range (0 , número_de_funcionários):
                for indice_2 in range (0 , número_de_beneficios):
                    while True:
                        beneficio = input(f"""
O Funcionário {lista_de_funcionários[indice_1].informações.nome} Tem {lista_de_beneficios[indice_2].nome}?\n Sim ou Não: """).strip().lower()
                        if beneficio == "sim":
                            lista_de_funcionários[indice_1].pagamento.beneficios[indice_2] == 1
                            break
                        elif beneficio == "não":
                            break
                        else:
                            print("Opção invalida, por favor, digite novamente")
                            continue
        else:
            for indice_1 in range(0, número_de_funcionários):
                if lista_de_funcionários[indice_1].informações.nome == busca:
                    funcionário_beneficiado = 1
                    for indice_2 in range(0, número_de_beneficios):
                        while True:
                            beneficio = input(f"""
O Funcionário {lista_de_funcionários[indice_1].informações.nome} Tem {lista_de_beneficios[indice_2].nome}?\n Sim ou Não: """).strip().lower()
                            if beneficio == "sim":
                                lista_de_funcionários[indice_1].pagamento.beneficios[indice_2] == 1
                                break
                            elif beneficio == "não":
                                break
                            else:
                                print("Opção invalida, por favor, digite novamente")
                                continue
        if funcionário_beneficiado == 0 and busca != "todos":
            print(f"O Beneficio {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar Registrar os Beneficios dos Funcionários(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue
    
def Adicionar_Descontos(lista_de_funcionários, lista_de_descontos, número_de_funcionários, número_de_descontos):
    while True:
        novo_desconto = Desconto()
        Adicionar_Beneficio(novo_desconto)
        lista_de_descontos.append(novo_desconto)
        número_de_descontos = número_de_descontos + 1
        for indice in range(0 , número_de_funcionários):
            lista_de_funcionários[indice].pagamento.descontos.append(0)
        while True:
            choice = (input("Deseja continuar Adicionando Descontos(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_descontos, número_de_descontos
                case '1':  
                    break
                case _:
                    print("Opção invalida\n\n")  
                    continue  

def Adicionar_Desconto(desconto):
    desconto.nome = input("Nome Do Desconto: ")
    while True:
        desconto.tipo_de_aumento = input("""Tipo de Diminuição do Desconto Será:
        "Percentual(%)"
        "Multiplicatio(*)"
        "Somativo(+)":""")
        if desconto.tipo_de_aumento == "%" or "*" or "+":
            break
        else:
            print("Opção invalida")
    desconto.quantia = input("Quantia desse Diminuição: ")

def Remover_Descontos(lista_de_funcionários, lista_de_descontos, número_de_funcionários, número_de_descontos):
    if lista_de_descontos == []:
        print("Nenhum Desconto foi Adicionado até o momento\n")
        return
    while True:
        busca = input("Deseja Remover todos os Descontos ou apenas um Desconto especifico\n\n").strip().lower() 
        desconto_deletado = 0
        if busca == "todos":
            for indice_1 in range(0 , número_de_descontos):
                lista_de_descontos.pop(indice_1)
                número_de_descontos = número_de_descontos - 1
                for indice_2 in range(0 , número_de_funcionários):
                    lista_de_funcionários[indice_2].pagamento.descontos.pop(indice_1)
        else:
            for indice_1 in range(0 , número_de_descontos):
                if lista_de_descontos[indice_1].informações.nome == busca:
                    print(f"O Beneficio {lista_de_descontos[indice_1].informações.nome} foi Deletado\n")
                    lista_de_descontos.pop(indice_1)
                    número_de_descontos = número_de_descontos - 1
                    for indice_2 in range(0 , número_de_funcionários):
                        lista_de_funcionários[indice_2].pagamento.descontos.pop(indice_1)
                    desconto_deletado = 1
                    break
        if desconto_deletado == 0:
            print(f"O Beneficio {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar Removendo Descontos(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_descontos, lista_de_descontos
                case '1':
                    break
                case _:
                    print("Opção invalida")
                    continue 

def Print_Lista_de_Descontos(lista_de_descontos, número_de_descontos):
    if lista_de_descontos == []:
        print("Nenhum Desconto foi Adicionado até o momento\n\n")
        return
    while True:
        busca = input("Deseja ver todos os Descontos ou apenas um Desconto especifico\n\n").strip().lower()
        desconto_encontrado = 0
        if busca == "todos":
            for indice in range (0 , número_de_descontos):
                Print_Desconto(lista_de_descontos[indice])
        else:
            for indice in range(0, número_de_descontos):
                if lista_de_descontos[indice].informações.nome == busca:
                    desconto_encontrado = 1
                    Print_Desconto(lista_de_descontos[indice])
                    break
        if desconto_encontrado == 0 and busca != "todos":
            print(f"O Desconto {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar buscando Descontos(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_descontos
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue

def Print_Desconto(desconto):
    print(f"""
    Nome: {desconto.nome}
    Tipo de Aumento: {desconto.tipo_de_aumento}
    Quantia: {desconto.quantia}\n""")

def Registrar_Desconto_de_Funcionários(lista_de_funcionários, lista_de_descontos, número_de_funcionários, número_de_descontos):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    if lista_de_descontos == []:
        print("Nenhum Desconto foi Adicionado até o momento\n\n")
        return
    while True:
        busca = input("Deseja Registrar os Descontos de Todos os Funcionários ou apenas os Descontos de um Funcionário especifico\n\n").strip().lower()
        funcionário_descontado = 0
        if busca == "todos":
            for indice_1 in range (0 , número_de_funcionários):
                for indice_2 in range (0 , número_de_descontos):
                    while True:
                        beneficio = input(f"""
O Funcionário {lista_de_funcionários[indice_1].informações.nome} Tem {lista_de_descontos[indice_2].nome}?\n Sim ou Não: """).strip().lower()
                        if beneficio == "sim":
                            lista_de_funcionários[indice_1].pagamento.descontos[indice_2] == 1
                            break
                        elif beneficio == "não":
                            break
                        else:
                            print("Opção invalida, por favor, digite novamente")
                            continue
        else:
            for indice_1 in range(0, número_de_funcionários):
                if lista_de_funcionários[indice_1].informações.nome == busca:
                    funcionário_descontado = 1
                    for indice_2 in range(0, número_de_descontos):
                        while True:
                            desconto = input(f"""
O Funcionário {lista_de_funcionários[indice_1].informações.nome} Tem {lista_de_descontos[indice_2].nome}?\n Sim ou Não: """).strip().lower()
                            if desconto == "sim":
                                lista_de_funcionários[indice_1].pagamento.descontos[indice_2] == 1
                                break
                            elif desconto == "não":
                                break
                            else:
                                print("Opção invalida, por favor, digite novamente")
                                continue
        if funcionário_descontado == 0 and busca != "todos":
            print(f"O Desconto {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar Registrar os Descontos dos Funcionários(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue

def Calcular_Salario_Total_Funcionários(lista_de_funcionários, número_de_funcionários, lista_de_beneficios, lista_de_descontos, número_de_beneficios, número_de_descontos):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    while True:
        busca = input("Deseja Calcular o Salario Total de Todos os Funcionários ou apenas o Salario total de um Funcionário especifico\n\n").strip().lower()
        funcionário_descontado = 0
        beneficio_total = 0
        desconto_total = 0
        if busca == "todos":
            for indice in range (0 , número_de_funcionários):
                salario_base = int(lista_de_funcionários[indice].informações.salario)
                beneficio_total = Calcular_Beneficios_totais(lista_de_beneficios, salario_base, número_de_beneficios)
                desconto_total = Calcular_Descontos_totais(lista_de_descontos, salario_base, número_de_descontos)
                lista_de_funcionários[indice].informações.salario_total = salario_base + beneficio_total - desconto_total
        else:
            for indice in range(0, número_de_funcionários):
                if lista_de_funcionários[indice].informações.nome == busca:
                    funcionário_descontado = 1
                    salario_base = int(lista_de_funcionários[indice].informações.salario)
                    beneficio_total = Calcular_Beneficios_totais(lista_de_beneficios, salario_base,número_de_beneficios)
                    desconto_total = Calcular_Descontos_totais(lista_de_descontos, salario_base, número_de_descontos)
                    lista_de_funcionários[indice].informações.salario_total = salario_base + beneficio_total - desconto_total
        if funcionário_descontado == 0 and busca != "todos":
            print(f"O Desconto {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar Calculando o Salario Total dos Funcionários(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue

def Calcular_Beneficios_totais(lista_de_beneficios, salario_base, número_de_beneficios):
    beneficio_total = 0
    for indice in range (0 , número_de_beneficios):
        tipo_de_beneficio = lista_de_beneficios[indice].tipo_de_aumento
        quantia = int(lista_de_beneficios[indice].quantia)
        if tipo_de_beneficio == "%":
            beneficio_total = beneficio_total + (salario_base / 100 * quantia)
        elif tipo_de_beneficio == "*":
            beneficio_total = beneficio_total + (salario_base * quantia)
        elif tipo_de_beneficio == "+":
            beneficio_total = beneficio_total + (salario_base + quantia)
    return beneficio_total

def Calcular_Descontos_totais(lista_de_descontos, salario_base, número_de_descontos):
    desconto_total = 0
    for indice_2 in range (0 , número_de_descontos):
        tipo_de_desconto = lista_de_descontos[indice_2].tipo_de_aumento
        quantia = int(lista_de_descontos[indice_2].quantia)
        if tipo_de_desconto == "%":
            desconto_total = desconto_total + (salario_base / 100 * quantia)
        elif tipo_de_desconto == "*":
            desconto_total = desconto_total + (salario_base * quantia)
        elif tipo_de_desconto == "+":
            desconto_total = desconto_total + (salario_base + quantia)
    return desconto_total

def Print_Informação_Funcionários(lista_de_funcionários, número_de_funcionários):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    while True:
        busca = input("Deseja ver todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        funcinário_encontrado = 0
        if busca == "todos":
            for indice in range (0 , número_de_funcionários):
                Print_Informação_Funcionário(lista_de_funcionários[indice])
        else:
            for indice in range(0, número_de_funcionários):
                if lista_de_funcionários[indice].informações.nome == busca:
                    funcinário_encontrado = 1
                    Print_Informação_Funcionário(lista_de_funcionários[indice])
                    break
        if funcinário_encontrado == 0 and busca != "todos":
            print(f"O Funcionário {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue

def Print_Informação_Funcionário(funcinário_atual):
    print(f"""
    Nome: {funcinário_atual.informações.nome}
    Idade: {funcinário_atual.informações.idade}
    Cargo: {funcinário_atual.informações.função}
    Salário Base: {funcinário_atual.informações.salario}
    Salário Total: {funcinário_atual.informações.salario_total}
    BeneficiosTotais: {funcinário_atual.pagamento.beneficios_totais}
    Descontos Totais: {funcinário_atual.pagamento.descontos_totais}
    Horários: {funcinário_atual.informações.horarios}
    Status: {funcinário_atual.informações.status}\n""")


def Print_Avaliação_Funcionários(lista_de_funcionários, número_de_funcionários):
    if lista_de_funcionários == []:
        print("Não tem funcionários cadastrados até o momento\n\n")
        return
    while True:  
        busca = input("Deseja Ver todos os funcionários ou apenas um funcionários especifico\n\n").strip().lower()
        funcinário_encontrado = 0
        if busca == "todos":
            for indice in range(0, número_de_funcionários):
                Print_Avaliação_Funcionário(lista_de_funcionários[indice])
        else:
            for indice in range(0, número_de_funcionários):
                if lista_de_funcionários[indice].informações.nome == busca:
                    Print_Avaliação_Funcionário(lista_de_funcionários[indice])
                    funcinário_encontrado = 1
                    break
        if funcinário_encontrado == 0 and busca != "todos":
            print(f"O Funcionário {busca} não foi encontrado, tente outra vez\n")
        while True:
            choice = (input("Deseja continuar buscando funcionarios(1)\nDeseja sair(-1)\n\n"))
            match choice:
                case '-1':
                    return lista_de_funcionários
                case '1':
                    break
                case _:
                    print("Opção invalida\n\n")
                    continue

def Print_Avaliação_Funcionário(funcinário_atual):
    print(f"""
    Nome: {funcinário_atual.informações.nome}
    Nota: {funcinário_atual.avaliação.nota}
    Descrição: {funcinário_atual.avaliação.descrição}
    Faltas: {funcinário_atual.avaliação.faltas}\n""")
