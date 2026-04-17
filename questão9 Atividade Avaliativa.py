notas = [5, 7.5, 8, 6, 9, 4, 7.2]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Quantidade de notas acima de 7:", contador)