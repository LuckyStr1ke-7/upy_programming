# 12 Factorial
n = int(input("Ingrese un número: ") )
total = 1
i = 1

while i<=n:
    total = total * i
    i = i + 1
print(f"factorial: {total}")
