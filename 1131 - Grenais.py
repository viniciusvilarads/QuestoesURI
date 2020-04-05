vitGremio = vitInter = empate = contador = 0

while True:
    inter, gremio = input().split()
    gremio = int(gremio)
    inter = int(inter)
    contador += 1
    if gremio > inter:
        vitGremio += 1
    elif inter > gremio:
        vitInter += 1
    else:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    cont = int(input())
    if cont != 1:
        break

if vitGremio > vitInter:
    vencedor = "Gremio venceu mais"
elif vitInter > vitGremio:
    vencedor = "Inter venceu mais"
else:
    vencedor = "Nao houve vencedor"

print(contador, "grenais")
print("Inter:{}".format(vitInter))
print("Gremio:{}".format(vitGremio))
print("Empates:{}".format(empate))
print(vencedor)
