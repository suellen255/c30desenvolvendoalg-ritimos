
def rank_jogador(pontos, derrotas):
    pontos = pontos - (derrotas * 10)

    if pontos < 0:
        return "Banido"
    elif pontos < 100:
        return "Bronze"
    elif pontos < 300:
        return "Prata"
    elif pontos < 600:
        return "Ouro"
    else:
        return "Diamante"


def saque(saldo, valor):
    taxa = 2
    return saldo - valor - taxa


def deposito(saldo, valor):
    return saldo + valor