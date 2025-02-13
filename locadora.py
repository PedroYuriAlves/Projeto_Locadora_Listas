import os

veic_disp = [
    {"modelo":"Creta", "valor_dia":150},
    {"modelo":"Tracker", "valor_dia":90},
    {"modelo":"HB20", "valor_dia":50},
    {"modelo":"Tucson", "valor_dia":110},
    {"modelo":"Fusca", "valor_dia":10},
    {"modelo":"Creta", "valor_dia":150},
]

veic_alugados = []

def imprimir_disp():
    if(len(veic_disp) > 0):
        for v in range(len(veic_disp)):
            print("[{}] {} - {} /dia".format(v, veic_disp[v]["modelo"],veic_disp[v]["valor_dia"]))
    else:
        print("Nenhum veículo disponivel")
        
def imprimir_alugados():
    if(len(veic_alugados) > 0):
        for v in range(len(veic_alugados)):
            print("[{}] {} - {} /dia".format(v, veic_alugados[v]["modelo"],veic_alugados[v]["valor_dia"]))
    else:
        print("Nenhum veículo sendo utilizado")

def alugarVeiculo(cod, dias):
    veic_alugado = veic_disp.pop(cod)

    print("Veículo {} Alugado - Valor do Alguel R$ {}".format(veic_alugado["modelo"],veic_alugado["valor_dia"]*dias))
    veic_alugados.append(veic_alugado)

def devolverVeiculo(cod):
    veic_devolvido = veic_alugados.pop(cod)
    print("Veículo {} Devolvido".format(veic_devolvido["modelo"]))
    veic_disp.append(veic_devolvido)
    
 


condicao = 1
os.system("cls")
while condicao == 1:
    
    print("Bem vindo a Locadora de Carros do Yuri")
    print("Digite a Opção de Serviço:")
    print("0 - Ver portifolio de Veículos | 1 - Alugar um Carro | 2 - Devolver um carro | 3 - para Sair do sistema")
    menu_usu = int(input())
    if(menu_usu == 0):
        imprimir_disp()
        print("")
    elif(menu_usu == 1):
        imprimir_disp()    
        print("Digite quantos dias você quer alugar o veículo?:")
        dias_aluguel = int(input())
        print("Digite a o código do veículo que você quer alugar:")
        cod_veic = int(input())
        while (0 > cod_veic or cod_veic >= len(veic_disp)):            
            print("Código de veículo inválido\n digite um código correto:")
            cod_veic = int(input())
        alugarVeiculo(cod_veic,dias_aluguel)
    elif(menu_usu == 2):        
        if(len(veic_alugados) > 0):
            imprimir_alugados()   
            print("Digite a o código do veículo que você quer alugar:")
            cod_veic = int(input())
            devolverVeiculo(cod_veic)
    elif(menu_usu == 3):
        condicao = 0        
        print("Encerrando o sistema.....")
    else:
        print("Comando invalido.")
        
    print("===================================")
    print("")



