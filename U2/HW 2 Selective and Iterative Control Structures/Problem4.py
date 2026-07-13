'''
Problem 4 — Season Classifier The user enters month numbers one by one. 
The program displays the corresponding season for each entry. 
The loop continues until the user types "exit". If a number is outside 1-12, 
display an error message and continue the loop.


Seasons: Winter (12, 1, 2) · Spring (3, 4, 5) · Summer (6, 7, 8) · Fall (9, 10, 11)
3	Spring
7	Summer
13	Invalid month. Please enter a number between 1 and 12.
'''
month_numbers = []
while True:
    month_entry = input("Enter a month number: ")
    if month_entry.lower() == "exit":
        break
    month_number = int(month_entry)
    if month_number<1 or month_number > 12:
        print("Invalid month. Please enter a month between 1 and 12")
        continue
    month_numbers.append(month_entry)
for month in month_numbers:
    if month in (12, 1, 2):
        season = "winter"
    elif month in (3, 4, 5):
        season = "spring"
    elif month in (6, 7, 8):
        season = "summer"
    else:
        season = "fall"
    print(f"{month} {season}")