
""" ~ Martes y Viernes de 1 a 3 TUTORÍAS
El sistema para cosecha de manzanas a cada trabajador se le paga por caja de manzanas cosechadas,
las primeras 10 cajas, se le pagan a $50 cada caja, mas de 50 y menos de 80 cajas
se le pagan 50% más, más de 80 se le pagan el doble de su total de pago, se le
descuenta el 5% para caja de ahorro:
Generar un sistema que pida el nombre del trabajador y la cantidad de cajas cosechadas ese
día, así como el pago que obtiene indicando la cantidad pagada de acuerdo a la cantidad de 
cosechadas así como el descuento que se hace por pago

* Primeras 10 = $50 / caja
* + 50 pero - de 80 = 50% más
* + 80 se paga el doble de subtotal de pago
"""
class Empleado:
    def __init__(self, nombre, caja):
        self.nombre = nombre
        self.caja = caja
        self.pago_por_caja = 50
        self.total = 0
        self.descuento = 0.05 

    def calcular_pago(self):
        if self.caja <= 10:
            self.total = self.caja * self.pago_por_caja
        elif 50 < self.caja <= 80:
            self.total = 10 * self.pago_por_caja + (self.caja - 50) * self.pago_por_caja * 1.5
        elif self.caja > 80:
            self.total = (self.caja * self.pago_por_caja) * 2
        else:
            self.total = self.caja * self.pago_por_caja

    def calcular_descuento(self):
        return self.total * self.descuento

    def info(self):
        self.calcular_pago()
        descuento = self.calcular_descuento()
        pago_descuento = self.total - descuento
        print(f"\nTrabajador: {self.nombre}")
        print(f"    Cajas cosechadas: {self.caja}")
        print(f"    Pago total (antes de descuento): ${self.total}")
        print(f"    Descuento (5% para caja de ahorro): ${descuento}")
        print(f"    Pago después de descuento ${pago_descuento}")

nombre = input("Ingresa el nombre del trabajador: ")
cajas_cosechadas = int(input("Ingresa la cantidad de cajas cosechadas: "))

empleado = Empleado(nombre, cajas_cosechadas)
empleado.info()
