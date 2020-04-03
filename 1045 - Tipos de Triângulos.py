N1, N2, N3 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)

valores = list()
valores.append(N1)
valores.append(N2)
valores.append(N3)

A = max(valores)
valores.remove(max(valores))
B = max(valores)
valores.remove(max(valores))
C = max(valores)
valores.remove(max(valores))

if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B==C):
        print("TRIANGULO ISOSCELES")
