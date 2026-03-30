#comando continue
#usado para interromper apenas a repetição


for i in range(5):
    if i == 3:  #ex: não ira imprimir o 3
        continue

    print(i, end=" ")

print('Programa terminado')