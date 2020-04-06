S = 3
S2 = 2
soma = 1
while S != 39:
    soma += S/S2
    S += 2
    S2 = S2*2
print("{:.2f}".format(soma))
