coluna = input()
tipo = input()
comida = input()

if comida == "carnivoro":
    print("aguia")
elif tipo == "ave" and comida == "onivoro":
    print("pomba")
elif tipo == "mamifero" and comida == "onivoro":
    print("homem")
elif tipo == "anelideo" and comida == "onivoro":
    print("minhoca")
elif tipo == "mamifero" and comida == "herbivoro":
    print("vaca")
elif tipo == "inseto" and comida == "herbivoro":
    print("lagarta")
elif tipo == "inseto" and comida == "hematofago":
    print("pulga")
elif tipo == "anelideo" and comida == "hematofago":
    print("sanguessuga")
