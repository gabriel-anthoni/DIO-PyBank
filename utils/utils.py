import os

# ========================= VALIDAR CPF =========================
def validar_cpf(cpf:str):
    cpf_valido = ( len(cpf) == 14 and
            cpf[0:3].isdigit()  and
            cpf[3] == "."       and
            cpf[4:7].isdigit()  and
            cpf[7] == "."       and
            cpf[8:11].isdigit() and
            cpf[11] == "-"      and
            cpf[12:14].isdigit() )
    return cpf_valido

# ======================= FORMATAR NÚMERO =======================
def formatar_numero(valor):
    valor = f"{float(valor):.2f}"
    centavos = valor[-1:-3:-1]
    valor = valor[-4::-1]

    valor_formatado = ""
    num = 0
    for _ in valor:
        if num != 3:
            valor_formatado += _
            num += 1
        else:
            valor_formatado += f".{_}"
            num = 0
    
    return f"{valor_formatado[::-1]},{centavos[::-1]}"

# ================== PROCURAR NÚMERO DA CONTA ===================
def procurar_numero_conta(num:str,lista_de_contas:list):
    for _ in lista_de_contas:
        if _.numero_conta == num:
            return True
    return False

# ======================= LIMPAR TERMINAL =======================
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")