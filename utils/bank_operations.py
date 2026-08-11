
# =========================== DEPÓSITO ===========================
def depositar_valor(valor,/):
    try:
        valor = float(valor)
    except ValueError:
        return 1
    if(valor > 0):
        return [f"Depósito:   R$ {valor:.2f}",valor]
    else:
        return 1

# ============================ SAQUE =============================
def sacar_valor(*,valor:float,numeros_saques:int,limiteDeSaques:int,limitePorSaque:float,saldo:float):
    try:
        valor = float(valor)
    except ValueError:
        return 1
    if(numeros_saques == limiteDeSaques):
        return 2
    elif(valor < 0):
        return 1
    elif(valor > saldo):
        return 3
    elif(valor > limitePorSaque):
        return 4
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
