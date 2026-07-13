'''
Problem 5 — Shipping Cost Calculator The user enters the weight (kg) and distance (km)
for multiple packages. The program calculates the shipping cost for each package. 
The loop continues until the user types "exit". 
At the end, display the total accumulated shipping cost.

Distance <= 100 km	$50.00 MXN	$80.00 MXN
Distance > 100 km	$120.00 MXN	$200.00 MXN
weight = 3, distance = 80	Shipping cost: $50.00 MXN
weight = 7, distance = 50	Shipping cost: $80.00 MXN
weight = 4, distance = 250, exit	Shipping cost: $120.00 MXN — Total: $250.00 MXN
'''

total = 0
packages = []

while True:
    weight_entry = input("Enter weight (kg): ")
    if weight_entry.lower() == "exit":
        break
    
    weight = float(weight_entry)
    distance = float(input("Enter distance (km): "))
    
    if distance <= 100:
        if weight <= 5:
            cost = 50
        else:
            cost = 80
    else:
        if weight <= 5:
            cost = 120
        else:
            cost = 200
            
    packages.append((weight, distance, cost))

for weight, distance, cost in packages:
    print(f"weight = {weight}, distance = {distance}  Shipping cost: ${cost} MXN")
    total += cost

print(f"Total: ${total} MXN")