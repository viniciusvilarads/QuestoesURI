A, B = input().split()
A = int(A)
B = int(B)
if max(A,B) % min(A,B) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
