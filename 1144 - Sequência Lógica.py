N = int(input())
X = 1
for c in range(N):
    print(X, X**2, X**3)
    print(X, (X**2)+1, (X**3)+1)
    X += 1
