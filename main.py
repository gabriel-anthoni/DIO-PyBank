from utils.bank_operations import *
from utils.utils import *
from utils.bank_models import *
from datetime import date

def main():
    clientes = []
    contas = []

    menu = """
    ╔═══════════════[MENU]════════════════╗
    ╟─[D] Depositar                       ║
    ╟─[S] Sacar                           ║
    ╟─[E] Extrato                         ║
    ╟─[U] Criar Usuário                   ║
    ╟─[C] Criar Conta Corrente            ║
    ╟─[L] Listar Contas                   ║
    ╟─[Q] Sair                            ║
    ╠═════════════════════════════════════╝\n"""

    while True:
        print(menu, end="")
        opcao = input("    ╙─ Escolha uma opção: ").lower().strip()

        match opcao:
            case "d":
                cpf = input("Informe o CPF do cliente: ")
                cliente = filtrar_cliente(cpf, clientes)

                if not cliente:
                    print("\n[Cliente não encontrado!]")
                    continue

                try:
                    valor = float(input("Depositar: R$ "))
                except ValueError:
                    print("\n[Valor inválido.]")
                    continue

                transacao = Deposito(valor)
                conta = recuperar_conta_cliente(cliente)
                if not conta:
                    continue

                cliente.realizar_transacao(conta, transacao)

            case "s":
                cpf = input("Informe o CPF do cliente: ")
                cliente = filtrar_cliente(cpf, clientes)

                if not cliente:
                    print("\n[Cliente não encontrado!]")
                    continue

                try:
                    valor = float(input("Sacar: R$ "))
                except ValueError:
                    print("\n[Valor inválido.]")
                    continue

                transacao = Saque(valor)
                conta = recuperar_conta_cliente(cliente)
                if not conta:
                    continue

                cliente.realizar_transacao(conta, transacao)

            case "e":
                cpf = input("Informe o CPF do cliente: ")
                cliente = filtrar_cliente(cpf, clientes)

                if not cliente:
                    print("\n[Cliente não encontrado!]")
                    continue

                conta = recuperar_conta_cliente(cliente)
                if not conta:
                    continue

                print("\n================ EXTRATO ================")
                transacoes = conta.historico.transacoes

                if not transacoes:
                    print("Não foram realizadas movimentações.")
                else:
                    for t in transacoes:
                        print(f"{t.__class__.__name__}:\t\tR$ {t.valor:.2f}")

                print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
                print("==========================================")

            case "u":
                nova_conta(clientes)

            case "c":
                criar_conta_corrente(clientes,contas)

            case "l":
                if not contas:
                    print("\n[Nenhuma conta cadastrada.]")
                    continue

                for conta in contas:
                    print("=" * 40)
                    print(f"Agência:\t{conta.agencia}")
                    print(f"C/C:\t\t{conta.numero}")
                    print(f"Titular:\t{conta.cliente.nome}")

            case "q":
                print("\nAté logo!")
                break

            case _:
                print("\n[Opção inválida! Tente novamente.]")

if __name__ == "__main__":
    main()