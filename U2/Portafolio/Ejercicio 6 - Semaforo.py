# Traffic light

color = input("Ingresa un color: ").lower()
if color == "green":
    print("Go")
elif color == "yellow":
    print("Warning!!!")
elif color == "red":
    print("STOP")
else:
    print("Invalid color")