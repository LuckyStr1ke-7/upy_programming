# 
'''
Problem 2 — BMI Calculator The user enters weight (kg) and height (m) for 
multiple people.
The program calculates the BMI and classifies it for each person.
The loop continues until the user types "exit" when prompted for weight.

BMI formula: BMI = weight / height²

Categories: Underweight (< 18.5) / Normal (18.5 - 24.9) / Overweight (25 - 29.9) / Obese (>= 30)



weight = 70, height = 1.75	BMI: 22.86 — Normal
weight = 90, height = 1.60	BMI: 35.16 — Obese
weight = 55, height = 1.68	BMI: 19.49 — Normal
'''

data=[]
while True:
    weight_entry = input("Enter a weight (Kg): ")
    if weight_entry == "exit":
        break
    weight = float(weight_entry)
    height = float(input("Enter a height (m): "))
    data.append((weight, height))

for tupla in data:
    bmi = tupla[0] / (tupla[1] ** 2)
    if bmi < 18.5:
        state = "Underweight"
    elif bmi < 25:
        state = "Normal"
    elif bmi < 30:
        state = "Overweight"
    else:
        state = "Obese"
    print(f"Weight = {tupla[0]}, Height = {tupla[1]}. BMI: {bmi} - {state}")