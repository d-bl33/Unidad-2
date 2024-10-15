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
class Tienda:
    def __init__(self):
        self.clave = [235, 789, 320, 439, 462]
        self.nombre =["Cereal", "Huevo", "Arroz", "Leche", "Chocolate"]
        self.costo = [56, 75, 23, 40, 15]
        self.existencia = [90, 60, 129, 32, 5]
        self.venta = [0,0,0,0,0]
        self.ganancia =[0,0,0,0,0]
    def mas_producto(self): #~producto que tengo más
        mayor_cantidad = max(self.existencia)
        indice = self.existencia.index(mayor_cantidad)
        print(f""""El producto con mayor existencia en stock es: 
                Producto: {self.nombre[indice]}
                Clave: {self.clave[indice]}
                Cantidad: {mayor_cantidad}""")
    def menor_producto(self): #~producto que tengo menos
        menor_cantidad = min(self.existencia) #CTRL+D (con el número de veces que quieras cambiarlo)
        indice = self.existencia.index(menor_cantidad)
        print(f""""El producto con menor existencia en stock es: 
                Producto: {self.nombre[indice]}
                Clave: {self.clave[indice]}
                Cantidad: {menor_cantidad}""")
    def mas_vendido(self):
        mayor_vendido= max(self.venta) #CTRL+D (con el número de veces que quieras cambiarlo)
        indice = self.venta.index(mayor_vendido)
        print(f""""El producto más vendido es: 
                Producto: {self.nombre[indice]}
                Clave: {self.clave[indice]}
                Cantidad: {mayor_vendido}""")
    def mas_vendido(self):
        menor_vendido= min(self.venta) 
        indice = self.venta.index(menor_vendido)
        print(f""""El producto menos vendido es: 
                Producto: {self.nombre[indice]}
                Clave: {self.clave[indice]}
                Cantidad: {menor_vendido}""")
    def vender(self):
        for i in range(len(self.clave)):
            print(f""""
{i + 1}.-{self.nombre[i]}:
--Clave: {self.clave[i]}---${self.costo[i]} 
    Existencia: {self.existencia[i]}\n""")
        numero = int(input("Ingrese la clave del producto que desea comprar: "))
        if numero not in self.clave:
            print("\nLa clave no es válida\nSaliendo...")
        else:
            ind = self.clave.index(numero)
            if self.existencia[ind] == 0:
                print("No hay productos en stock\nSaliendo...")
            else:
                cantidad = int(input(f"¿Cuántas unidades de {self.nombre[ind]} desea comprar? "))
                if cantidad <= self.existencia[ind]:
                    self.existencia[ind] -= cantidad
                    self.venta[ind] += cantidad
                    self.ganancia[ind] += (self.costo[ind] * 0.10) * cantidad
                    print(f"Venta realizada: {cantidad} unidades de {self.nombre[ind]}")
                else:
                    print(f"No hay suficiente stock. Solo quedan {self.existencia[ind]} unidades.")
    def menu(self):
        while True:  
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
                    self.menos_vendido()
                case 4:
                    self.mas_producto()
                case 5:
                    self.menos_producto()
                case 6:
                    print("\n\tSaliendo...")
                    break
                case _:
                    print("Opción no válida")
            input()
x = Tienda()
x.vender()
x.mas_vendido()
x.menu()




