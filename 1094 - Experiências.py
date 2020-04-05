N = int(input())
qtdRato = qtdSapo = qtdCoelho = 0
total = 0
percRato = percSapo = percCoelho = 0
for c in range(N):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)
    if Tipo == "R":
        qtdRato += Quantia
    elif Tipo == "S":
        qtdSapo += Quantia
    elif Tipo == "C":
        qtdCoelho += Quantia

total = qtdRato + qtdSapo + qtdCoelho
percRato = (qtdRato * 100) / total
percSapo = (qtdSapo * 100) / total
percCoelho = (qtdCoelho * 100) / total

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(qtdCoelho))
print("Total de ratos: {}".format(qtdRato))
print("Total de sapos: {}".format(qtdSapo))
print("Percentual de coelhos: {:.2f} %".format(percCoelho))
print("Percentual de ratos: {:.2f} %".format(percRato))
print("Percentual de sapos: {:.2f} %".format(percSapo))
