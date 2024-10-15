# 18 de Septiembre de 2024
"""Desarrollar un sistema caja de cambio en el cual se inserta un bilete
o se le indica una cantidad a cambiar, el sistema devuelve la cantidad en monedas
de 10, 5 y un peso.

REGLA GENERAL: NO SE PUEDE DEVOLVER TODO DE UNA SOLA MONEDA. 
Al menos una de cada denominación.
Ejemplo: Le damos 100 pesos, devuelve nueve de $10, una de $5, y cinco de $1
"""
#* Entrada: Cantidad a cambiar

class Moneda:
    
    def __init__(self):
        self.billete = 0
        self.uno = 0
        self.cinco = 0
        self.diez = 0

class PedirDatos(Moneda):
    def pedir_datos(self):
        cantidad = int(input("Ingresa la cantidad de dinero que desea cambiar: "))
        self.billete = cantidad

class Conversion(PedirDatos):
    def conversion(self):
        while self.billete > 0:
            if self.billete > 10:
                self.billete -= 10
                self.diez += 1
            elif self.billete > 5:
                self.billete -= 5
                self.cinco += 1
            else:
                self.billete -= 1
                self.uno += 1

class Imprimir(Conversion):
    def imprimir(self):
        print(f"""Se entregan:
                {self.diez} monedas de 10 pesos
                {self.cinco} monedas de 5 pesos
                {self.uno} monedas de 1 peso""")


cambio = Imprimir()
cambio.pedir_datos()
cambio.conversion()
cambio.imprimir()   