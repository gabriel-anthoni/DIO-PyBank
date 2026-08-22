from utils.bank_operations import *
from utils.models import *
from utils.utils import *

menu = """
╔═══════════════[MENU]════════════════╗
╟─[D] Depositar                       ║
╟─[S] Sacar                           ║
╟─[E] Extrato                         ║
╟─[U] Criar Usuário                   ║
╟─[C] Criar Conta Corrente            ║
╟─[L] Listar Contas                   ║
╟─[Q] Sair                            ║
╠═════════════════════════════════════╝\n║"""

contas   = [1,[]]
usuarios = []

while True:
    print(menu)
    opcao = input("╙─ Escolha uma opção: ").lower()
    match opcao:
        # ==== DEPÓSITO ====
        case 'd':
            limpar_terminal()

            if contas[1] == []:
                print("Nenhuma conta cadastrada no momento.")
                continue

            numero_conta = int(input("Número da conta:"))
            if procurar_numero_conta(numero_conta,contas[1]):
                valor = input("R$ ")
                print(processar_transacao(valor,contas[1],numero_conta,"Deposito"))
            else:
                print("Não existe")

        # ==== SAQUE ====
        case 's':
            limpar_terminal()

            if contas[1] == []:
                print("Nenhuma conta cadastrada no momento.")
                continue

            numero_conta = int(input("Número da conta:"))
            if procurar_numero_conta(numero_conta,contas[1]):
                valor = input("R$ ")
                print(processar_transacao(valor,contas[1],numero_conta,"Saque"))
            else:
                print("Conta não encontrada.")

        # ==== EXTRATO ====
        case 'e':
            limpar_terminal()

            if contas[1] == []:
                print("Nenhuma conta cadastrada no momento.")
                continue

            numero_conta = int(input("Número da conta:"))
            for _ in contas[1]:
                if _.numero_conta == numero_conta:
                    exibir_extrato(_.saldo,_.retornar_extrato())

        # ==== CADASTRAR USUÁRIO ====
        case 'u':
            limpar_terminal()
            usuario = cadastrar_usuario(usuarios)
            usuario = PessoaFisica(
                usuario['nome'],
                usuario['dataDeNascimento'],
                usuario['cpf'],
                usuario['endereço'])
            usuarios.append(usuario)

        # ==== CADASTRAR CONTA ====
        case 'c':
            limpar_terminal()

            if usuarios == []:
                print("Nenhum usuário cadastrado")
                continue
            
            cpf = input("CPF:")
            for _ in usuarios:
                if _.cpf == cpf:
                    conta = Conta(contas[0],_)
                    contas[0] += 1
                    contas[1].append(conta)
        
        # ==== LISTAR CONTAS ====
        case 'l':
            limpar_terminal()
            if contas[1] == []: 
                print("Nenhuma conta cadastrada no momento.")
                continue
            exibir_contas(contas[1])
            
        # ==== SAIR =====
        case 'q':
            limpar_terminal()
            break
        
        # ==== ERROR ====
        case _:
            limpar_terminal()
            print("Opção inválida! Por favor, escolha uma das opções do menu.")