# 18. Cuadrícula de la multiplicación
'''Lee un número n, se imprime una cuadrícula n * n, un nuúmero que contendrá una
y una columna'''

n = int(input("Ingresa un número: "))
for r in range(1, n+1):
    l = ""
    for c in range(1, n+1):
        l = l + str(r*c) + "\t"
    print(l)