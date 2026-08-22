from datetime import datetime
from .utils import validar_cpf,formatar_numero

# =========================== EXTRATO ===========================
def exibir_extrato(saldo_atual: float, dict_extrato: list):
    print("╔═════════════════════════════════════╗")
    
    if dict_extrato == {}:
        print("║ Nenhuma movimentação realizada      ║\n║ até o momento.                      ║")
    else:
        for data in dict_extrato.keys():
            print(f"╟─{data}──────────────────────────╢")
            for i in dict_extrato[data]:
                print(f"╟─{i}{" "*(7-(len(i)-28))} ║")

    print("╟─────────────────────────────────────╢")
    print(f"║ Saldo: R$ {formatar_numero(saldo_atual)}{" "*(25-len(f"{formatar_numero(saldo_atual)}"))} ║")
    print("╚═════════════════════════════════════╝")

# ====================== CADASTRAR USUÁRIO ======================
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
                if usuario.cpf == cpf:
                    cpf_existe = True
                    break
            if cpf_existe:
                continue
        
        if (validar_cpf(cpf)):
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
        "nome": nome,
        "dataDeNascimento": data_de_nascimento,
        "cpf": cpf,
        "endereço": f"{rua}, {nrm}, {bairro}, {cidade}/{sigla_estado}"
    }

    return novo_usuario

# ===================== REGISTRAR TRANSAÇÃO =====================
def registrar_transacao(hora,valor,tipo:str = "Deposito"):
    novo_valor = formatar_numero(valor)
    if tipo == "Deposito":
        return f"[{hora}] {tipo}: R$ {novo_valor}"
    elif tipo == "Saque":
        return f"[{hora}] {tipo}:    R$ {novo_valor}"

# ======================= VERIFICAR SAQUE =======================
def verificar_saque(valor,conta:Conta):
    if valor > conta.limite:
        return [False,"limite por saque excedido"]

    if valor > conta.saldo:
        return [False,"saldo insuficiente"] 
    
    data = datetime.today().date()
    if conta.data_ultimo_saque != data:
        conta.alterar_data_ultimo_saque()
    
    if (conta.data_ultimo_saque == data) and (conta.limite_saques == conta.saques_realizados):
        return [False,"limite diário atingido"]
    
    conta.aumentar_saques_realizados()
    return [True]

# ===================== PROCESSAR TRANSAÇÃO =====================
def processar_transacao(valor,contas:list,numero_conta:int,operacao: str = "Deposito"):
    try:
        valor = float(valor)
        for _ in contas:

            if _.numero_conta == numero_conta:
                if operacao == "Deposito":
                    _.depositar(valor)

                elif operacao == "Saque":
                    saque_valido = verificar_saque(valor,_)
                    if saque_valido[0]:
                        _.sacar(valor)
                    else:
                        return saque_valido[1]

                return f"{operacao} de R$ {formatar_numero(valor)} realizada com sucesso para a conta {_.numero_conta}."
    except ValueError:
        return "VALOR ERRADO"

# ======================== LISTAR CONTAS ========================
def exibir_contas(lista_de_contas: list):

    print("┌───────────────────┬───────────────────┬─────────────────┐")
    print("| Numero da conta:  | Dono:             | CPF:            |")
    print("├───────────────────┼───────────────────┼─────────────────┤")

    ultima_linha = len(lista_de_contas)
    linha        = 0
    for conta in lista_de_contas:
        linha += 1

        print(f"| {conta.numero_conta}{" "*(7-(len(str(conta.numero_conta))-10))} | {conta.cliente.nome}{" "*(7-(len(str(conta.cliente.nome))-10))} | {conta.cliente.cpf}{" "*(7-(len(str(conta.cliente.cpf))-8))} |")
        if(ultima_linha == linha):
            print("└───────────────────┴───────────────────┴─────────────────┘")
        else:
            print("├───────────────────┼───────────────────┼─────────────────┤")

# =================== BUSCAR DATA DA TRANSAÇÃO ==================
def buscar_data_transacao(conta:Conta):
    dataEhora = datetime.now()
    data = dataEhora.strftime("%d/%m/%Y")
    hora = dataEhora.strftime("%H:%M:%S")
    for _ in conta.extrato.ver_chaves():
        if _ == data:
            return [True,data,hora]
    return [False,data,hora]
