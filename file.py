# Año bisiesto
'''
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print(f"lap year {year}")
else:
    print("Nain")'''

# Validar un número dentro de un rango
'''
n = int(input("Ingresa un numero cualquiera: "))

rango = 10 <= n <= 15 # True or False
print (rango)'''

# Vocal o consonante
'''
letra = input("Ingresa una letra: ")
vocal = letra.lower() in "aeiou"
print(vocal)'''


# Tickets
'''
price = 150
age = int(input("Ingrese su edad: "))
card = input("Tiene tarjeta? (Si/No): ").lower()

if age < 12:
    disc = 0.3
elif age <= 25 and card == "si":
    disc = 0.20
elif age < 65:
    disc = 0
else:
    disc = 0.4

new_price = price * (1-disc)
print(f"Price $: {new_price}")'''

# Par o impar
'''
n = int(input("Ingresa un número: "))
if n % 2 == 0:
    print("Es par")
else:
    print("Impar")
'''

# Traffic light
'''
color = input("Ingresa un color: ").lower()
if color == "green":
    print("Go")
elif color == "yellow":
    print("Warning!!!")
elif color == "red":
    print("STOP")
else:
    print("Invalid color")
'''

# IMC
'''
weight = float(input("Ingrese su peso (Kg): "))
height = float(input("Ingresa su estatura (M): "))
imc = weight / (height**2)

if imc < 18.5:
    print("Estás desnutrido")
elif imc < 25:
    print("Estás normal")
elif imc < 30:
    print("Estás Gordito")
else:
    print("Eres Majim boo")
'''

