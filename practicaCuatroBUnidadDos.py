"""Hacemos 6 arreglos. Le ponemos 5 nombres (productos) ya directamente
1. CLAVE
2. NOMBRE
3. COSTO (10% de ganancia)
4. EXISTE
5. VENTA
6. GANANCIA
Si no hay producto(0) no puede existir la venta
Si el producto existe le preguntamos cuanto quiere comprar y de acuerdo a la cantidad le decimos si hay existencia, si hay existencia se lo vamos a vender
Menu de opciones va a venir ventas y opciones(stock), incluir qué producto se vendío más, que producto se vendio menos, que producto tengo mas y cual menos
5 opciones"""
from os import system

class Tienda:

    def __init__(self):
        self.producto = [[253, 789, 320, 439, 462], 
                        ["Cereal", "Huevo", "Arroz", "Leche", "Chocolate"], 
                        [56, 75, 23, 40, 15], 
                        [90, 60, 129, 32, 5], 
                        [0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0]]
        
        """self.clave = [253, 789, 320, 439, 462]
        self.nombre = ["Cereal", "Huevo", "Arroz", "Leche", "Chocolate"]
        self.costo = [56, 75, 23, 40, 15]
        self.existencia = [90, 60, 129, 32, 5]
        self.venta = [0, 0, 0, 0, 0]
        self.ganancia = [0, 0, 0, 0, 0]"""

    def mas_producto(self):
        mayor_cantidad = max(self.producto[3])
        indice = self.producto[3].index(mayor_cantidad)
        print(f"\nEl producto con mayor existencia en stock: {self.producto[1][indice]} -- Clave:  {self.producto[0][indice]}\n\t Cantidad: {mayor_cantidad}")

    def menor_producto(self):
        menor_cantidad = min(self.producto[3])
        indice = self.producto[3].index(menor_cantidad)
        print(f"\nEl producto con menor existencia en stock: {self.producto[1][indice]} -- Clave: {self.producto[0][indice]}\n\t Cantidad: {menor_cantidad}")

    def mas_vendido(self):
        mayor_vendido = max(self.producto[4])
        indice = self.producto[4].index(mayor_vendido)
        print(f"\nEl producto más vendido es: {self.producto[1][indice]} -- Clave: {self.producto[0][indice]}\n\t Cantidad: {mayor_vendido}")
    
    def menor_vendido(self):
        menor_vendido = min(self.producto[4])
        indice = self.producto[4].index(menor_vendido)
        print(f"\nEl producto menos vendido es: {self.producto[1][indice]} -- Clave: {self.producto[0][indice]}\n\t Cantidad: {menor_vendido}")

    def vender(self):
        for i in range(len(self.producto[0])):
            print(f"{i + 1}.- {self.producto[1][i]}\n -- Clave: {self.producto[0][i]} -- ${self.producto[2][i]}\n -- Existencia: {self.producto[3][i]}\n")
        clav = int(input("Ingrese la clave del producto que desea comprar: "))
        if not clav in self.producto[0]:
            print("\nLa clave no es válida\n\tSaliendo...")
        else:
            ind = self.producto[0].index(clav)
            if self.producto[3][ind] == 0:
                print("\nNo existen productos en stock\n\tSaliendo...")
            else:
                cantidad = int(input("Ingrese el número de productos que desea comprar: "))
                if cantidad > self.producto[3][ind]:
                    print("No hay suficiente stock")
                else:
                    self.producto[3][ind] -= cantidad
                    self.producto[4][ind] = cantidad
                    ganancia = (self.producto[2][ind] + (self.producto[2][ind] * 0.1)) * cantidad
                    self.producto[5][ind] = ganancia
                    print(f"\n--> Cuenta:\n{self.producto[1][ind]} --- ${ganancia}")

    def menu(self):
        while True:
            system("cls") 
            print("\n******MENÚ******")
            print("1) Realizar compra")
            print("2) El producto más vendido")
            print("3) El producto menos vendido")
            print("4) Producto con mayor existencia")
            print("5) Producto con menor existencia")
            print("6) Salir")
            opc = int(input("Seleccione una opción: "))
            match opc:
                case 1:
                    self.vender()
                case 2:
                    self.mas_vendido()
                case 3:
                    self.menor_vendido()
                case 4:
                    self.mas_producto()
                case 5:
                    self.menor_producto()
                case 6:
                    print("\n\tSaliendo...")
                    break
                case _:
                    print("Opción no válida")
            input()

x = Tienda()
x.menu()