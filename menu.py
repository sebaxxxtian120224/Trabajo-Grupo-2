from retos import * 

print ("1. Area De Triangulo")
print ("2. BMI")
print ("3. Cambio")
print ("4. Horario De LLegada")
opcion = int(input("Seleccione Opcion: "))
if opcion == 1:
    s1 = float(input("Ingrese Lado 1: "))
    s2 = float(input("Ingrese Lado 2: "))
    s3 = float(input("Ingrese Lado 3: "))
    print("Area:" , area_triangulo(s1,s2,s3))
elif opcion == 2:
    peso = float(input("Peso En Lb: "))
    altura = float(input("Altura: "))
    print("BMI:" , calcular_BMI(peso, altura))
elif opcion == 3:
    cambio = int(input("Valor: "))
    print("Monedas:" , calcular_cambio(cambio))

elif opcion == 4:
    h = int(input("Hora salida: "))
    m = int(input("Minuto salida: "))
    s = int(input("Segundo salida: "))
    dh = int(input("Horas duración: "))
    dm = int(input("Minutos duración: "))
    ds = int(input("Segundos duración: "))
    print("Llegada:", calcular_horario_llegada(h, m, s, dh, dm, ds))
elif opcion == 5:
        print("Saliendo del programa...")
else:
        print("Opción no válida")