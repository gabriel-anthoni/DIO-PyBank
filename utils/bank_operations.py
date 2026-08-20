from datetime import datetime
from .bank_models import *

def filtrar_cliente(cpf: str, clientes: list):
    clientes_filtrados = [c for c in clientes if c.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente: Cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta associada. @@@")
        return None
    return cliente.contas[0]


def validar_cpf(cpf:str):
    cpf_valido = ( len(cpf) == 14   and
                cpf[0:3].isdigit()  and
                cpf[3] == "."       and
                cpf[4:7].isdigit()  and
                cpf[7] == "."       and
                cpf[8:11].isdigit() and
                cpf[11] == "-"      and
                cpf[12:14].isdigit() )
    return cpf_valido


def nova_conta(clientes: list):
    while True:
        cpf = input("Informe o CPF: ").strip()
        
        if not validar_cpf(cpf):
            print("\n[CPF invalido!]")
            continue

        if filtrar_cliente(cpf, clientes):
            print("\n[Já existe um cliente cadastrado com esse CPF!]")
            continue
        break

    nome = input("Informe o nome completo: ")

    while True:
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_nascimento, "%d/%m/%Y")
            idade_days = datetime.now() - data
            idade = idade_days.days // 365

            if idade < 18:
                print("\n[Cadastro permitido apenas para maiores de 18 anos.]")
                continue

            break
        except ValueError:
            print("\n[Formato de data inválido. Tente novamente.]")

    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)
    print("\n[Usuário criado com sucesso!]")


def criar_conta_corrente(clientes, contas):
    while True:
        cpf = input("Informe o CPF do cliente: ").strip()
        
        if not validar_cpf(cpf):
            print("\n[CPF inválido!]")
            continue

        cliente = filtrar_cliente(cpf, clientes)

        if not cliente:
            print("\n[Cliente não encontrado! Cadastre o usuário primeiro.]")
            return
        
        break

    numero_conta = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)

    contas.append(conta)
    cliente.adicionar_conta(conta)
    print(f"\n[{numero_conta}º Conta criada com sucesso!]")