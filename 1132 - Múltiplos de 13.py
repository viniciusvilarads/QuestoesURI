X = int(input())
Y = int(input())
soma = 0
for c in range(min(X,Y), max(X,Y)+1):
    if c % 13 != 0:
        soma += c

print(soma)
