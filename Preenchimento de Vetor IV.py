par = list()
impar = list()
for c in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        for d in range(len(par)):
            print("par[{}] = {}".format(d, par(d)))
        par.clear()
    if len(impar) == 5:
        for d in range(len(impar)):
            print("impar[{}] = {}".format(d, impar[d]))
        impar.clear()


if len(impar) > 0:
    for d in range(len(impar)):
        print("impar[{}] = {}".format(d, impar[d]))
if len(par) > 0:
    for d in range(len(par)):
        print("par[{}] = {}".format(d, par(d)))
