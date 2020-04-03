di = input().split()
hIni = input().split(":")
df = input().split()
hFin = input().split(":")

di = int(di[1])
hi = int(hIni[0])
mi = int(hIni[1])
si = int(hIni[2])
df = int(df[1])
hf = int(hFin[0])
mf = int(hFin[1])
sf = int(hFin[2])

dia = df - di
hora = hf - hi    
minuto = mf - mi   
segundo = sf - si


if hora < 0:
    hora += 24
    dia -= 1
if minuto < 0:
    minuto += 60
    hora -= 1
if segundo < 0:
    segundo += 60
    minuto -=1
if dia <= 0:
    dia = 0

print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(minuto))
print("{} segundo(s)".format(segundo))
