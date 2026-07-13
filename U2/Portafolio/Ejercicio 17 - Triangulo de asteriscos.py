# 17 triangulo de asteriscos
#necesitamos una variable n, todos los asteriscos se van a alinear
# a la izquierda, renglónn 1=*, renglón 2=**

n = int(input("Ingresa un número: "))
for renglon in range(1, n+1):
    print("*" * renglon)
for renglon in range(n, 0, -1):
    print("*"* renglon)
