while True:
    X = int(input())
    if X == 0:
        break
    for c in range(1, X+1):
        if c == X:
            print(c)
        else:
            print(c, end=" ")
