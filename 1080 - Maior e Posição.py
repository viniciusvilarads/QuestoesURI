valores = list()
for c in range(100):
    num = int(input())
    valores.append(num)
print(max(valores))
print(valores.index(max(valores))+1)
