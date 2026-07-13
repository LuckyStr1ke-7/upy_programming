'''
El sistema guarda el usuario "admin" y la contrasena "1234". Lee un
  usuario y una contrasena. Primero verifica el usuario; solo si es
  correcto, verifica la contrasena. Imprime "Bienvenido",
  "Contrasena incorrecta" o "Usuario desconocido".
  '''

usuario = "admin"
contraseña = "1234"
login = input("Ingrese el nombre de usuario: ")
if login == usuario:
    password = input("Ingrese la contraseña: ")
    if password == contraseña:
        print("Bienvenido!")
    else:
        print("Contraseña Incorrecta")
else:
    print("Usuario desconocido")