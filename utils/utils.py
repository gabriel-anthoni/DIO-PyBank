
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

# ========================== TRANSAÇÃO ===========================
def registrar_transacao( *,transacao, extrato_historico):
    transacao_registrada_hoje = False

    for registro in extrato_historico:
        if transacao["Data"] in registro.keys():
            transacao_registrada_hoje = True
            registro[str(transacao["Data"])].append(transacao["Texto"])
            break
    
    if not transacao_registrada_hoje:
        extrato_historico.append({f"{transacao["Data"]}": [transacao["Texto"]]})