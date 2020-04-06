N = list()
V = int(input())
for c in range(10):
    N.append(V)
    V = V * 2
for c in range(len(N)):
    print("N[{}] = {}".format(c, N[c]))
