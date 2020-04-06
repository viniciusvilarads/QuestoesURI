N = int(input())
soma = 0
for c in range(N):
    soma = 0
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    for d in range(Y*2):
        if X % 2 != 0:
            soma += X
        X += 1
    print(soma)
