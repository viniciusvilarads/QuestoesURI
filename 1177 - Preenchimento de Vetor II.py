T = int(input())
N = list()
for d in range(999):
    for c in range(T):
        N.append(c)
for c in range(0, 1000):
    print("N[{}] = {}".format(c, N[c]))
