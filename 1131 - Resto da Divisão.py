X = int(input())
Y = int(input())
for c in range(min(X,Y)+1, max(X,Y)):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
