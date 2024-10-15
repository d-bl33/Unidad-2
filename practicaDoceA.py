""" 
*Ejercicio 1 
Crea un array o arreglo unidimensional donde le indiques el tamaño
por teclado  y crear una función que rellene el array o arreglo con
los múltiplos de un  número pedido por teclado. Por ejemplo, 
si defino un array de tamaño 5 y elijo un 3 en la función, 
el array contendrá 3, 6, 9, 12, 15. Muestralos por pantalla 
usando otra función distinta."""

class Multiplo:
    def __init__(self):
        self.lista = []
        self.tam = int(input("Ingrese el tamaño del arreglo: "))
        self.num = int(input("ingrese el multiplo: "))

    def crear_lista(self):
        for i in range(self.tam):
            self.lista.append((i + 1) * self.num)

    def imprimir_lista(self):
        print(self.lista)
ejercicio_1 = Multiplo()
ejercicio_1.crear_lista()
ejercicio_1.imprimir_lista()

"""
*Ejercicio 2 
Crea dos arrays o arreglos unidimensional es que tengan el mismo
tamaño (lo  pedirá por teclado), en uno de ellos almacenarás nombres
de personas como  cadenas, en el otro array o arreglo ira almacenando 
la longitud de los nombres. """
print()
class Nombres:
    def __init__(self):
        self.tamaño = int(input("Ingresa el tamaño de los arreglos: "))
        self.nombres = []
        self.longitud = []
    def longitud_de_nombre(self):
        for i in range(self.tamaño):
            nombre = input(f"Ingresa el nombre de la persona {i+1}: ")
            self.nombres.append(nombre)
            self.longitud.append(len(nombre))
    def imprimir(self):
        print("\nNOMBRES Y LONGITUDES")
        for i in range(self.tamaño):
            print(f"Nombre: {self.nombres[i]}, Longitud: {self.longitud[i]}")
ejercicio_2= Nombres()
ejercicio_2.longitud_de_nombre()
ejercicio_2.imprimir()

"""
*Ejercicio 3 
Dado el siguiente arreglo de números: [1, 5, 8, 3, 30, 9, 13] 
Imprimir en pantalla programáticamente los números impares mayores a 3."""
print()
class Impar():
    def __init__(self):
        self.lista = [1, 5, 8, 3, 30, 9, 13]
    def comparacion(self):
        for i in self.lista:
            if (i > 3) and (i % 2 == 1):
                print(f"--> {i}")
ejercicio_3= Impar()
ejercicio_3.comparacion()

"""
*Ejercicio 4 
Dada las siguientes notas almacenadas en un arreglo: [20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la función 
(min) y escriba  en pantalla. Luego programáticamente 
calcule el promedio de  notas descontando la nota eliminada. """
print()

class Notas():
    def __init__(self):
        self.notas = [20, 15, 12, 11, 8, 4, 1]
        self.nota_baja = 0
        self.promedio = 0
    def comparar(self):
        self.nota_baja = self.notas[0]
        for nota in self.notas:
            if nota < self.nota_baja:
                self.nota_baja = nota
        self.notas.remove(self.nota_baja)
    def imprimir_nota_baja(self):
        print(f"La nota más baja eliminada es: {self.nota_baja}")
    def promedio_(self):
        self.promedio = sum(self.notas) / len(self.notas)
        self.promedio = round(self.promedio,2)
    def imprimir(self):
        print(f"El promedio de las notas (sin la más baja) es: {self.promedio}")
ejercicio_4 = Notas()
ejercicio_4.comparar()
ejercicio_4.imprimir_nota_baja
ejercicio_4.promedio_()
ejercicio_4.imprimir()

"""
*Ejercicio 5 
Dada las siguientes notas almacenadas en un arreglo: 
[20, 15, 12, 11, 8, 4, 1] solicitar al usuario en número a buscar,
indicar si el numero existe y e que  posición se encuentra
"""
class Buscar:
    def __init__(self):
        print()
        self.lista = [20, 15, 12, 11, 8, 4, 1]
        self.numero = int(input("Introduzca el número a buscar: "))
    def comprobar(self): #con if
        if self.numero in self.lista:
            indice = self.lista.index(self.numero)
            print(f"El número {self.numero} está en la posición: {indice + 1} de la lista")
        else:
            print(f"El número {self.numero} no se encuentra en la lista")
ejercicio_5 = Buscar()
ejercicio_5.comprobar()


"""try:
    indice = lista_cinco.index(numero)
    print(f"El número {numero} está en la posición: {indice + 1} de la lista")
except:
    print(f"El número {numero} no se encuentra en la lista")
"""
