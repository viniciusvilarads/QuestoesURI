N = int(input())
valIn = valOut = 0
for c in range(N):
    X = int(input())
    if 10 <= X <= 20:
        valIn += 1
    else:
        valOut += 1

print(valIn, "in")
print(valOut, "out")
