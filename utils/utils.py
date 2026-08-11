
# ============================ ERROS =============================
def formatar_erro(erro:int, *,limite_por_saque=0):
    match erro:
        case 1:
            return "Não foi possível concluir. O valor digitado é inválido."
        case 2:
            return "Ops! Você já atingiu o número máximo de saques permitidos hoje."
        case 3:
            return "Transação não autorizada: saldo insuficiente na conta."
        case 4:
            return f"Limite ultrapassado! Cada saque pode ser de no máximo R$ {limite_por_saque:.2f}."
        case _:
            return "Não foi possível processar a solicitação no momento."
