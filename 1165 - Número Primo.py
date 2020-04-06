N = int(input())
for c in range(N):
    X = int(input())
    primo = 0
    for d in range(1, X+1):
        if X % d == 0:
            primo += 1
    if primo == 2:
        print(X, "eh primo")
    else:
        print(X, "nao eh primo")
