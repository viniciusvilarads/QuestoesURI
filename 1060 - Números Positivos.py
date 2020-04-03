soma = qtd = 0
for c in range(6):
    num = float(input())
    if num > 0:
        qtd += 1
        soma += 1
print(soma, "valores positivos")
print("{:.1f}".format(soma/qtd))
