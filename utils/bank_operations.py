from datetime import datetime

# =========================== DEPÓSITO ===========================
def depositar_valor(valor,/):
    try:
        valor = float(valor)
    except ValueError:
        return 1
    if(valor > 0):
        data_deposito = datetime.now()
        horario       = data_deposito.time().strftime("%H:%M:%S")
        data          = data_deposito.strftime("%d/%m/%Y")
        return {"Texto":f"[{horario}] Depósito: R$ {valor:.2f}","Valor":valor,"Data":data}
    else:
        return 1

# ============================ SAQUE =============================
def sacar_valor(*,valor:float,numeros_saques:list,limiteDeSaques:int,limitePorSaque:float,saldo:float):
    try:
        valor = float(valor)
    except ValueError:
        return 1
    if(numeros_saques[0] == limiteDeSaques):
        return 2
    elif(valor < 0):
        return 1
    elif(valor > saldo):
        return 3
    elif(valor > limitePorSaque):
        return 4
    else:
        data_saque = datetime.now()
        horario       = data_saque.time().strftime("%H:%M:%S")
        data          = data_saque.strftime("%d/%m/%Y")
        return {"Texto":f"[{horario}] Saque:    R$ {valor:.2f}","Valor":valor,"Data":data}

# =========================== EXTRATO ============================
def exibir_extrato(saldo_atual: float, /, *, lista_extrato: list):
    print("=========== EXTRATO ===========")
    
    if lista_extrato == []:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        for _ in lista_extrato:
            data = list(_.keys())
            print(data[0])
            for i in _[data[0]]:
                print(i)

    print("-------------------------------")
    print(f"Saldo: R$ {saldo_atual:.2f}")
    print("===============================")