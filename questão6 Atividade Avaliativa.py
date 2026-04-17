temps = []

for i in range(7):
    temps.append(float(input()))

soma = 0

for t in temps:
    soma = soma + t

media = soma / 7

print(media)