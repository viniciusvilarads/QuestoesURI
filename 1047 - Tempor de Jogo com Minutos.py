hInicial, mInicial, hFinal, mFinal = input().split()
hInicial = int(hInicial)
mInicial = int(mInicial)
hFinal = int(hFinal)
mFinal = int(mFinal)


if hFinal > hInicial:
    hora = hFinal - hInicial
    if mFinal > mInicial:
        minuto = mFinal - mInicial
    elif mInicial > mFinal:
        hora = hora - 1
        minuto = (60 - mInicial) + mFinal
    elif mInicial == mFinal:
        minuto = 0
elif hInicial > hFinal:
    hora = (24 - hInicial) + hFinal
    if mFinal > mInicial:
        minuto = mFinal - mInicial
    elif mInicial > mFinal:
        hora = hora - 1
        minuto = (60 - mInicial) + mFinal
    elif mInicial == mFinal:
        minuto = 0
elif hInicial == hFinal:
    if mFinal > mInicial:
        minuto = mFinal - mInicial
        hora = 0
    elif mInicial > mFinal:
        minuto = (60 - mInicial) + mFinal
        hora = 23
    elif mInicial == mFinal:
        hora = 24
        minuto = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
