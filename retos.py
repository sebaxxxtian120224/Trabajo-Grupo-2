def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int) -> str:
    total_segundos_salida = hora_salida * 3600 + minuto_salida * 60 + segundo_salida
    total_segundos_duracion = duracion_horas * 3600 + duracion_minutos * 60 + duracion_segundos
    total_segundos_llegada = total_segundos_salida + total_segundos_duracion
    horas_llegada = (total_segundos_llegada // 3600) % 24
    minutos_llegada = (total_segundos_llegada % 3600) // 60
    segundos_llegada = total_segundos_llegada % 60
    return f"{horas_llegada}:{minutos_llegada}:{segundos_llegada}"

#Aqui van las funciones
def calcular_BMI (peso_lb, altura_inch):
        peso_lb = peso_lb * 0.45
        altura_metros = altura_inch * 0.025
        BMI = peso_lb / (altura_metros ** 2)
        return round (BMI, 2)
def calcular_cambio (cambio: int):
    moneda500 = cambio // 500
    cambio %=500
    moneda200 = cambio // 200
    cambio %=200
    moneda100 = cambio // 100
    cambio %=100
    moneda50 = cambio // 50
    cambio %=50
    return str(moneda500) + "," + str(moneda200) + "," + str(moneda100) + "," + str(moneda50)
