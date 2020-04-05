alcool = gasolina = diesel = 0
while True:
    comb = int(input())
    if comb == 4:
        break
    elif comb == 1:
        alcool += 1
    elif comb == 2:
        gasolina += 1
    elif comb == 3:
        diesel += 1

print("MUITO OBRIGADO")
print("Alcool:",alcool)
print("Gasolina:",gasolina)
print("Diesel:",diesel)
