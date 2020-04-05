N = int(input())
for c in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    soma = 0 
    for c in range(min(X,Y)+1, max(X,Y)):
        if c % 2 != 0:
            soma += c
    print(soma)
    
