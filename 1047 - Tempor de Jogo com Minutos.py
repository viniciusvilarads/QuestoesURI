hInicial, mInicial, hFinal, mFinal = input().split()
hInicial = int(hInicial)
mInicial = int(mInicial)
hFinal = int(hFinal)
mFinal = int(mFinal)

hora = minuto = 0

if hInicial == hFinal and mInicial == mFinal:
    hora = 24
elif hFinal > hInicial and mFinal > mInicial:
    hora = hFinal - hInicial
    if hora == 1:
        hora = 0
    minuto = mFinal - mInicial
elif hFinal > hInicial and mInicial > mFinal:
    hora = hFinal - hInicial
    if hora == 1:
        hora = 0 
    minuto = (60 - mInicial) + mFinal
elif hInicial > hFinal and mFinal > mInicial:
    hora = (24 - hInicial) + hFinal
    if hora == 1:
        hora = 0
    minuto = mFinal - mInicial
elif hInicial > hFinal and mInicial > mFinal:
    hora = (24 - hInicial) + hFinal
    if hora == 1:
        hora = 0
    minuto = (60 - mInicial) + mFinal
elif hFinal > hInicial and mFinal == mInicial:
    hora = hFinal - hInicial
elif hFinal > hInicial and mInicial == mFinal:
    hora = hFinal - hInicial
elif hInicial == hFinal and mFinal > mInicial:
    minuto = mFinal - mInicial
elif hInicial == hFinal and mInicial > mFinal:
    minuto = (60 - mInicial) + mFinal
    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
