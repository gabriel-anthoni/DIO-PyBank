menu = """
================ MENU ================
  [D] Depositar
  [S] Sacar
  [E] Extrato
  [Q] Sair
======================================
"""

LIMITE_SAQUES_DIARIOS        = 3
limite_por_saque             = 500.00
saldo_atual                  = 0.00
extrato_historico            = []
quantidade_saques_realizados = 0

# =========================== DEPÓSITO ===========================
def depositar_valor(valor):
    try:
        valor = float(valor)
    except ValueError:
        return [False,"Operação falhou! O valor informado é inválido."]
    if(valor > 0):
        return [f"Depósito:   R$ {valor:.2f}",valor]
    else:
        return [False,"Operação falhou! O valor informado é inválido."]

# ============================ SAQUE =============================
def sacar_valor(valor:float,numeros_saques:int,limiteDeSaques:int,limitePorSaque:float,saldo:float):
    try:
        valor = float(valor)
    except ValueError:
        return [False,"Operação falhou! O valor informado é inválido."]
    if(numeros_saques == limiteDeSaques):
        return [False,"Operação falhou! Você atingiu o limite máximo de saques diários."]
    elif(valor < 0):
        return [False,"Operação falhou! O valor informado é inválido."]
    elif(valor > saldo):
        return [False,"Operação falhou! Você não tem saldo suficiente para realizar esse saque."]
    elif(valor > limitePorSaque):
        return [False,f"Operação falhou! O valor solicitado excede o limite de R$ {limite_por_saque:.2f} por saque."]
    else:
        return [f"Saque:      R$ {valor:.2f}",valor]

# =========================== EXTRATO ============================
def exibir_extrato(saldo_atual: float, lista_extrato: list):
    print("====== EXTRATO ======")
    
    if lista_extrato == []:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        for e in lista_extrato:
            print(e)

    print("---------------------")
    print(f"Saldo: R$ {saldo_atual:.2f}")
    print("=====================")

# ============================ MENU ==============================
while True:
    print(menu)
    opcao = input("Escolha uma opção: ").lower()
    match opcao:
        case "d":
            depositar = depositar_valor(input("Depositar: R$ "))
            if(depositar[0] == False):
                print(depositar[1])
                continue
            saldo_atual += depositar[1]
            extrato_historico.append(depositar[0])
        case "s":
            saque = sacar_valor(input("Sacar: R$ "),quantidade_saques_realizados,LIMITE_SAQUES_DIARIOS,limite_por_saque,saldo_atual)
            if(depositar[0] == False):
                print(saque[1])
                continue
            saldo_atual                  -= saque[1]
            quantidade_saques_realizados += 1
            extrato_historico.append(saque[0])
        case "e":
            exibir_extrato(saldo_atual,extrato_historico)
        case "q":
            break
        case _:
            print("Opção inválida! Por favor, escolha uma das opções do menu.")