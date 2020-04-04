X = int(input())
Y = int(input())
soma = 0 
for c in range(min(X,Y)+1, max(X,Y)):
    if c % 2 != 0:
        soma += c

print(soma)
