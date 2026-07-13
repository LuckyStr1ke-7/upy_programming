# 13 suma de numeros de pares
n = int(input("Ingresa un número: "))
res = 0
for i in range(2, n+1, 2):
    res = res + i
print(f"suma de pares hasta {n}: {res}")