N = int(input())

for c in range(N):
    X = int(input())
    if X == 0:
        print("NULL")
    else:
        if X % 2 == 0:
            print("EVEN", end=" ")
        else:
            print("ODD", end=" ")
        if X > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")
