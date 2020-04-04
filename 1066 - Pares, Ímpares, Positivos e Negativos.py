somaPares = somaImpares = somaPositivos = somaNegativos = 0
for c in range(5):
    num = int(input())
    if num % 2 == 0:
        somaPares += 1
    else:
        somaImpares += 1
    if num > 0:
        somaPositivos += 1
    elif num < 0:
        somaNegativos += 1
print("{} valor(es) par(es)".format(somaPares))
print("{} valor(es) impar(es)".format(somaImpares))
print("{} valor(es) positivo(s)".format(somaPositivos))
print("{} valor(es) negativo(s)".format(somaNegativos))
