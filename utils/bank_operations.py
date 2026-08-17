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
        data_saque    = datetime.now()
        horario       = data_saque.time().strftime("%H:%M:%S")
        data          = data_saque.strftime("%d/%m/%Y")
        return {"Texto":f"[{horario}] Saque:    R$ {valor:.2f}","Valor":valor,"Data":data}

# =========================== EXTRATO ============================
def exibir_extrato(saldo_atual: float, /, *, lista_extrato: list):
    print("╔═════════════════════════════════════╗")
    
    if lista_extrato == []:
        print("Nenhuma movimentação realizada até o momento.")
    else:
        for _ in lista_extrato:
            data = list(_.keys())
            print(f"╟─{data[0]}──────────────────────────╢")
            for i in _[data[0]]:
                print(f"╟─{i}{" "*(7-(len(i)-28))} ║")

    print("╟─────────────────────────────────────╢")
    print(f"║ Saldo: R$ {saldo_atual:.2f}{" "*(25-len(f"{saldo_atual:.2f}"))} ║")
    print("╚═════════════════════════════════════╝")
    

# ====================== CADASTRAR USUÁRIO =======================
def cadastrar_usuario(lista_de_usuarios: list):

    ESTADOS_VALIDOS = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    ]

    nome = input("Nome: ").strip().title()

    while True:
        print("Digite sua data de nascimento no formato: DD/MM/YYYY")
        data_de_nascimento = input("Data de Nascimento: ").strip()
        try:
            data       = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
            idade_days = datetime.now() - data
            idade      = idade_days.days // 365
            
            if idade < 18:
                print("Cadastro permitido apenas para maiores de 18 anos.")
                continue
            break
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    while True:
        print("Digite seu CPF no formato: XXX.XXX.XXX-XX")
        cpf = input("CPF: ").strip()

        cpf_existe = False
        if lista_de_usuarios != []:
            for usuario in lista_de_usuarios:
                if usuario["CPF"] == cpf:
                    cpf_existe = True
                    break
            if cpf_existe:
                continue
        
        if (
            len(cpf) == 14      and
            cpf[0:3].isdigit()  and
            cpf[3] == "."       and
            cpf[4:7].isdigit()  and
            cpf[7] == "."       and
            cpf[8:11].isdigit() and
            cpf[11] == "-"      and
            cpf[12:14].isdigit()
        ):
            break
        else:
            print("Formatagem do CPF inválida!")

    print("\n--- Endereço ---")
    rua = input("Logradouro: ").strip().title()
    
    while True:
        nrm = input("Número (pressione Enter para S/N): ").strip()
        if nrm.isdigit():
            break
        elif not nrm:
            nrm = "S/N" 
            break
        else:
            print("Erro: digite apenas números ou deixe em branco.")
    
    bairro = input("Bairro: ").strip().title()
    cidade = input("Cidade: ").strip().title()

    while True:
        sigla_estado = input("Sigla do Estado (UF): ").strip().upper()
        if sigla_estado in ESTADOS_VALIDOS:
            break
        else:
            print("Sigla de estado inválida.")

    novo_usuario = {
        "CPF": cpf,
        "Nome": nome,
        "DataDeNascimento": data_de_nascimento,
        "Endereço": f"{rua}, {nrm}, {bairro}, {cidade}/{sigla_estado}"
    }

    return novo_usuario

# ======================= CADASTRAR CONTA ========================
def cadastrar_conta(lista_de_usuarios: list, lista_de_contas:list):
    if lista_de_usuarios == []:
        print("Não existem usuarios no Sistema.")
        return None

    while True:
        print("Digite seu CPF no formato: XXX.XXX.XXX-XX")
        cpf = input("CPF: ").strip()

        cpf_existe = False
        for usuario in lista_de_usuarios:
            if usuario["CPF"] == cpf:
                cpf_existe = True
                break
        if not cpf_existe:
            print("não existe usuario no nosso sistema com esse CPF")
            return None
            
        
        if (
            len(cpf) == 14      and
            cpf[0:3].isdigit()  and
            cpf[3] == "."       and
            cpf[4:7].isdigit()  and
            cpf[7] == "."       and
            cpf[8:11].isdigit() and
            cpf[11] == "-"      and
            cpf[12:14].isdigit()
        ):
            break
        else:
            print("Formatagem do CPF inválida!")
    lista_de_contas[0] += 1
    
    conta = {
        "NumeroDaConta":lista_de_contas[0],
        "Agencia":"001",
        "UsuarioCPF": cpf
    }

    return conta

# ======================== LISTAR CONTAS =========================
def exibir_contas(lista_de_usuarios: list, lista_de_contas: list):
    if not lista_de_usuarios or lista_de_contas[0] == 0:
        print("É necessário ter pelo menos um usuário e uma conta cadastrados.")
        return

    print("┌───────────────────┬───────────────────┬─────────────────┐")
    print("| Numero da conta:  | Dono:             | CPF:            |")
    print("├───────────────────┼───────────────────┼─────────────────┤")

    ultima_linha = len(lista_de_contas[1])
    linha        = 0
    for conta in lista_de_contas[1]:
        donodaconta = None
        linha += 1
        
        for usuario in lista_de_usuarios:
            if usuario['CPF'] == conta['UsuarioCPF']:
                donodaconta = usuario
                break

        if donodaconta:
            num_conta = str(conta['NumeroDaConta'])
            nome = donodaconta['Nome']
            cpf = donodaconta['CPF']

            print(f"| {num_conta:<17} | {nome:<17} | {cpf:<15} |")
            if(ultima_linha == linha):
                print("└───────────────────┴───────────────────┴─────────────────┘")
            else:
                print("├───────────────────┼───────────────────┼─────────────────┤")