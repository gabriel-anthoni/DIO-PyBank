from utils.bank_operations import *
from utils.utils import *
from datetime import date

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
quantidade_saques_realizados = [0,date.today().strftime("%d/%m/%Y")]
clientes                     = []

# ============================ MENU ==============================
while True:
    print(menu)
    opcao = input("Escolha uma opção: ").lower()
    match opcao:
        # ==== DEPÓSITO ====
        case "d":
            depositar = depositar_valor(input("Depositar: R$ "))
            if(isinstance(depositar, (int))):
                print(formatar_erro(depositar))
                continue
            saldo_atual += depositar["Valor"]
            registrar_transacao(transacao=depositar, extrato_historico=extrato_historico)
                
        # ==== SAQUE ====
        case "s":
            data = date.today().strftime("%d/%m/%Y")

            if data != quantidade_saques_realizados[1]:
                quantidade_saques_realizados = [0,data] 

            saque = sacar_valor(valor=input("Sacar: R$ "),numeros_saques=quantidade_saques_realizados,limiteDeSaques=LIMITE_SAQUES_DIARIOS,limitePorSaque=limite_por_saque,saldo=saldo_atual)
            if(isinstance(saque, (int))):
                print(formatar_erro(saque,limite_por_saque=limite_por_saque))
                continue
            saldo_atual                  -= saque["Valor"]
            quantidade_saques_realizados[0] += 1
            registrar_transacao(transacao=saque, extrato_historico=extrato_historico)
            
        # ==== EXTRATO ====
        case "e":
            exibir_extrato(saldo_atual,lista_extrato=extrato_historico)
        # ==== SAIR =====
        case "q":
            break
        # ==== ERROR ====
        case _:
            print("Opção inválida! Por favor, escolha uma das opções do menu.")