# Problem 1 — Grade Averaging System

'''Problem 1 — Grade Averaging System The user enters student grades one by one.
The program keeps reading grades until the user types "done".
Then it calculates the average and displays whether the student passed (>= 7.0) or failed.
If no grades were entered, display an error message.
8, 9, 7, done	Average: 8.00 — Passed
5, 4, 6, done	Average: 5.00 — Failed
done	No grades entered. Please enter at least one grade.
'''

n = 0
cum_sum = 0
calificaciones = []
while True:
    grades_input = input("Enter a grade: ")
    if grades_input.lower() == "done":
        break
    grade = float(grades_input)
    cum_sum += grade
    n += 1
    calificaciones.append(grade)

if n == 0:
    print("No grades entered. Please enter at least one grade")
else:
    avg = cum_sum / n
    if avg >= 7:
        print(f"{calificaciones} Average: {avg} - Passed")
    else:
        print(f"{calificaciones} Average: {avg} - Failed")