X, Y = input().split()
X = int(X)
Y = int(Y)
seq = 1
for c in range(1, int(Y/X)+1):
    for d in range(X):
        if d == X-1:
            print(seq)
        else:
            print(seq, end=" ")
            
        seq += 1
