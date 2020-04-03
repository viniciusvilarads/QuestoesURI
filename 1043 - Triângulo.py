l1, l2, l3 = input().split()
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)

if ((l1 + l2) > l3) and ((l1 + l3) > l2) and ((l2 + l3) > l1):
    perimetro = l1 + l2 + l3
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((l1+l2)*l3)/2
    print("Area = {:.1f}".format(area))
