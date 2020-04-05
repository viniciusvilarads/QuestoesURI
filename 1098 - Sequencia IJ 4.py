I = 0
J = 1
for c in range(1,12):
    if c == 1 or c == 6 or c ==11:
        I = int(I)
        J = int(J)
    print("I={} J={}".format(I, J))
    print("I={} J={}".format(I, J+1))
    print("I={} J={}".format(I, J+2))
    I += 0.2
    J += 0.2
    I = round(I, 1)
    J = round(J, 1)
