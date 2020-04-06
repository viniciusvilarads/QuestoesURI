while True:
    X = int(input())
    if X == 0:
        break
    soma = 0
    for c in range(10):
        if X % 2 == 0:
            soma += X
        X += 1
    print(soma)
