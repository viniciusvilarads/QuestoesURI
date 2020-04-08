N = int(input())
N1 = 0
N2 = 1
print(N1, N2, end=" ")
for c in range(1, N-1):
    N3 = N1 + N2
    if c+1 == N-1:
        print(N3)
    else:
        print(N3, end=" ")
    N1 = N2
    N2 = N3
