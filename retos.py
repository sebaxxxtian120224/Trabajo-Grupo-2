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