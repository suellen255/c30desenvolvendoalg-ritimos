consumos = []

dias = int(input("Quantos dias você anotou? "))

for i in range(dias):
    valor = float(input("Digite o consumo do dia: "))
    consumos.append(valor)

total = sum(consumos)

print("Total consumido:", total, "GB")

if total > 30:
    print("Você ultrapassou o limite de 30GB")
else:
    print("Você ainda tem internet disponível")