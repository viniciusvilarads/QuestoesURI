A = list()
for c in range(100):
    M = float(input())
    A.append(M)
for c in range(len(A)):
    if A[c] <= 10:
        print("A[{}] = {}".format(c, A[c]))
