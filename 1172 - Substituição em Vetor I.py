X = list()
for c in range(10):
    cobaia = int(input())
    if cobaia <= 0:
        cobaia = 1
    X.append(cobaia)
for c in range(len(X)):
    print("X[{}] = {}".format(c, X[c]))
