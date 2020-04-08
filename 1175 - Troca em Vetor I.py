M = list()
for c in range(20):
    cobaia = int(input())
    M.append(cobaia)
N = M[::-1]

for c in range(len(N)):
    print("N[{}] = {}".format(c, N[c]))
