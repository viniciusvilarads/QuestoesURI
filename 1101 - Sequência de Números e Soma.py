while True:
    soma = 0
    M, N = input().split()
    M = int(M)
    N = int(N)
    if M <= 0  or N <= 0:
        break
    else:
        for c in range(min(M,N), max(M,N)+1):
            print(c, end=" ")
            soma += c
        print("Sum={}".format(soma))
