A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    A = 24 - A
    hora = A + B
elif A < B:
    hora = B - A
else:
    hora = 24

print("O JOGO DUROU {} HORA(S)".format(hora))
