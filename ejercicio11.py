'''
Lee un entero positivo N e imprime la suma 1 + 2 + ... + N usando un
  ciclo while (inicializa, condicion, actualiza).
'''
n = int(input("Ingrese un número: "))
contador = 1
nn = 0
while contador <= n:
    nn += contador
    contador +=1
print(f"La suma de Gauss del 1 al {n} es {nn}")
