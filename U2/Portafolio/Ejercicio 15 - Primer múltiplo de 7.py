# 15 Primer múltiplo de 7 entre 1 rango /break y continue/

# Ingresa 2 números, A y B, A < B. %7, break para parar el código

a = int(input("Ingresa un número A: "))
b = int(input("Ingresa un número B mayor que A: "))
for i in range(a, b+1):
    if i % 7 == 0:
        print(f"Primer múltiplo de 7: {i}")
        break
