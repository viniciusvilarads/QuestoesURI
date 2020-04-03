N1, N2, N3 = input().split()
N1 = int(N1)
N2 = int(N2)
N3 = int(N3)
valores = list()
valores.append(N1)
valores.append(N2)
valores.append(N3)
valoresCobaia = valores[:]
valoresCobaia.sort()

for c in valoresCobaia:
    print(c)

print()

for c in valores:
    print(c)
