def imc(peso, altura):
    return peso / (altura * altura)

try:
    peso = float(input())
    altura = float(input())

    valor = imc(peso, altura)

    if valor < 18.5:
        print("Magro")
    elif valor <= 24.9:
        print("Normal")
    else:
        print("Acima do peso")

except:
    print("Entrada inválida")