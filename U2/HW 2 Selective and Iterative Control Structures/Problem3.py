'''
Problem 3 — Water Bill Calculator The user enters the m³ consumed for multiple months.
The program calculates the charge for each month using tiered rates.
The loop continues until the user types "exit".
At the end, display the total accumulated charge.

0 - 10 m³	$8.00
11 - 20 m³	$12.00
21 m³ and above	$18.00
8	Month charge: $64.00 MXN
15	Month charge: $180.00 MXN
25, exit	Month charge: $450.00 MXN — Total: $694.00 MXN'''

Total = 0
month_list = []
while True:
    spent = input("Enter your water consumed (mˆ3): ")
    if spent == "exit":
        break
    consume = float(spent)
    if consume <= 10:
        price = consume * 8
    elif consume <= 20:
        price = consume * 12
    else:
        price = consume * 18

    month_list.append((consume, price))
for month in month_list:
    print(f"{month[0]} Month charge: ${month[1]} mxm")
    Total += month[1]
print(f"Total: {Total} mxm")