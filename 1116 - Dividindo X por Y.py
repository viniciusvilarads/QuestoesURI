N = int(input())
for c in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if Y == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(X/Y))
