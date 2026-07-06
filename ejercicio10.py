'''
  Lee un numero. Si es positivo, indica si es "Positivo par" o
  "Positivo impar". Si no es positivo, imprime "No es positivo".
  '''

number = int(input("Ingrese un número: "))

if number > 0 and number % 2 ==0:
    print("Positivo par")
elif number > 0 and number % 2 != 0:
    print("Positivo impar")
else:
    print("No es positivo")