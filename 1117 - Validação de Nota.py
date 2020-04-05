validade = 0
soma = 0
while True:
    nota = float(input())
    if 0 <= nota <= 10:
        soma += nota
        validade += 1
    else:
        print("nota invalida")
    if validade == 2:
        break

print("media = {:.2f}".format(soma / 2))
