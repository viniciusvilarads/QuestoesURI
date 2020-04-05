validade = 0
soma = 0
X = 0
while True:
    nota = float(input())
    if 0 <= nota <= 10:
        soma += nota
        validade += 1
    else:
        print("nota invalida")
    if validade == 2:
        print("media = {:.2f}".format(soma / 2))
        while True:
            print("novo calculo (1-sim 2-nao)")
            X = int(input())
            if X == 1:
                validade = 0
                soma = 0
                break
            elif X == 2:
                break
    if X == 2:
        break
