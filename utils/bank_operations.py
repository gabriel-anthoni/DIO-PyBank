
# =========================== DEPÓSITO ===========================
def depositar_valor(valor,/):
    try:
        valor = float(valor)
    except ValueError:
        return [False,"Operação falhou! O valor informado é inválido."]
    if(valor > 0):
        return [f"Depósito:   R$ {valor:.2f}",valor]
    else:
        return [False,"Operação falhou! O valor informado é inválido."]

# ============================ SAQUE =============================
def sacar_valor(*,valor:float,numeros_saques:int,limiteDeSaques:int,limitePorSaque:float,saldo:float):
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
def exibir_extrato(saldo_atual: float, /, *, lista_extrato: list):
    print("====== EXTRATO ======")
    
    if lista_extrato == []:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        for e in lista_extrato:
            print(e)

    print("---------------------")
    print(f"Saldo: R$ {saldo_atual:.2f}")
    print("=====================")
