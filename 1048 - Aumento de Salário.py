sal = float(input())
if 0 < sal <= 400.00:
    novoSal = ((sal * 15)/100) + sal
    reajGanho = (sal * 15)/100
    perc = "15"
    print("Novo salario: {:.2f}".format(novoSal))
    print("Reajuste ganho: {:.2f}".format(reajGanho))
    print("Em precentual: {} %".format(perc))
elif 400.00 < sal <= 800.00:
    novoSal = ((sal * 12)/100) + sal
    reajGanho = (sal * 12)/100
    perc = "12"
    print("Novo salario: {:.2f}".format(novoSal))
    print("Reajuste ganho: {:.2f}".format(reajGanho))
    print("Em precentual: {} %".format(perc))
elif 800.00 < sal <= 1200.00:
    novoSal = ((sal * 10)/100) + sal
    reajGanho = (sal * 10)/100
    perc = "10"
    print("Novo salario: {:.2f}".format(novoSal))
    print("Reajuste ganho: {:.2f}".format(reajGanho))
    print("Em precentual: {} %".format(perc))
elif 1200.00 < sal <= 2000.00:
    novoSal = ((sal * 7)/100) + sal
    reajGanho = (sal * 7)/100
    perc = "7"
    print("Novo salario: {:.2f}".format(novoSal))
    print("Reajuste ganho: {:.2f}".format(reajGanho))
    print("Em precentual: {} %".format(perc))
elif sal > 2000.00:
    novoSal = ((sal * 4)/100) + sal
    reajGanho = (sal * 4)/100
    perc = "4"
    print("Novo salario: {:.2f}".format(novoSal))
    print("Reajuste ganho: {:.2f}".format(reajGanho))
    print("Em precentual: {} %".format(perc))
    
