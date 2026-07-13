# Password game
characters = "A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 ! @ # $ % ^ & * ( ) - _ = + ~ ` { } [ ] : ; ' < , > . / ?"
special_characters = "!@#$%^&*()-_=+<>?/"

# month = july
month = "july"

unlocked = 1
ask_password = True

while True:
    if ask_password == True:
        password = input("Ingresa tu contraseña: ")
    ask_password = True
    errors = ""
    # Rule1
    if unlocked >= 1:
        # Message 8 characters
        if len(password) < 8:
            #ToDO
            errors += "Fallaste, te faltan caracteres"
        valid_chars = characters.split()
        for letra in password:
            if letra not in valid_chars:
                errors += f"El caracter {letra} no es un caracter válido"
                break
    if unlocked >= 2:
        tiene_mayus = False
        for letra in password:
            if letra in "QWERTYUIOPASDFGHJKLZXCVBNM":
                tiene_mayus = True
                break
        if tiene_mayus == False:
            errors += "La contraseña no contiene Mayúsculas"
    if unlocked >=3:
        tiene_minus = False
        for letra in password:
            if letra in "qwertyuiopasdfghjklzxcvbnm":
                tiene_minus = True
                break
        if tiene_minus == False:
            errors += "La contraseña no contiene minúsculas"
    if unlocked >=4:
        tiene_digito = False
        for digito in password:
            if digito in "1234567890":
                tiene_digito = True
                break
        if tiene_digito == False:
            errors += "La contraseña necesita al mneos un dígito"
    if unlocked >= 5:
        tiene_esp = False
        for character in password:
            if character in special_characters:
                tiene_esp = True
                break
        if tiene_esp == False:
            errors += "La contraseña necesita un caracter especial!"
    if unlocked >= 6:
        suma = 0
        for caracter in password:
            if caracter.isdigit():
                suma += int(caracter)
        if suma != 25:
            errors += "Los digitos en la contraseña deben sumar 25"
    if unlocked >= 7:
        divisores = 0
        for i in range(1, len(password)+1):
            if len(password) % i == 0:
                divisores += 1
        if divisores != 2:
            errors += "La longitud de la contraseña debe ser un primo"
    if unlocked >=8:
        if month not in password.lower():
            errors += "La contraseña debe inculir el mes actual"
    
    if errors == "":
        if unlocked < 8:
            unlocked = unlocked + 1
            ask_password= False
            print("Rule passed, new instruction available")    
        else:
            print("congrats")
            break
    else:
        print("To fix: ")
        print(errors)