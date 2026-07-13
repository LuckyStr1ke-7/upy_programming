# IMC

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