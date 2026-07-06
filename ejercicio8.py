'''Lee una temperatura en Celsius e imprime el estado fisico del agua:
     temp <= 0           -> "Solido (hielo)"
     0 < temp < 100      -> "Liquido (agua)"
     temp >= 100         -> "Gaseoso (vapor)"'''

t= float(input("Ingrese una temperatura (C): "))

if t<=0:
    print(f"Estado sólido (hielo): {t}C")
elif t<100:
    print(f"Estado líquido (agua): {t}C")
else:
    print(f"Estado gaseoso (Vapor): {t}C")