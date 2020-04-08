X = float(input())
N = list()
for c in range(100):
    N.append(X)
    X = X / 2

for c in range(len(N)):
    print("N[{}] = {:.4f}".format(c, N[c]))
