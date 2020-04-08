T = int(input())
for d in range(T):
    N = int(input())
    N1 = 0
    N2 = 1
    fibonacci = list()
    fibonacci.append(N1)
    fibonacci.append(N2)
    for c in range(1, N):
        N3 = N1 + N2
        fibonacci.append(N3)
        N1 = N2
        N2 = N3
    print("Fib({}) = {}".format(N, fibonacci[N]))
