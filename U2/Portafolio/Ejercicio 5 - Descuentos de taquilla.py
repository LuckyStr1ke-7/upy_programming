# Tickets

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
print(f"Price $: {new_price}")
