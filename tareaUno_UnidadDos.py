class Alumnos:
    def __init__(self):
        self.nombres = ["Juan", "Paco", "Pancho", "María", "Lucero"]
        self.calif_1 = [89, 67, 100, 95, 76]
        self.calif_2 = [100, 89, 90, 63, 80]
        self.calif_3 = [78, 34, 90, 83, 100]
        self.promedio = []
        self.reprobados = []

    def prom(self):
        for i in range(len(self.calif_1)):
            promedio = (self.calif_1[i] + self.calif_2[i] + self.calif_3[i]) / 3
            self.promedio.append(round(promedio, 2))

    def verificar_reprobados(self):
        for i in range(len(self.nombres)):
            reprobado_unidades = []
            if self.calif_1[i] < 70:
                reprobado_unidades.append(1)
            if self.calif_2[i] < 70:
                reprobado_unidades.append(2)
            if self.calif_3[i] < 70:
                reprobado_unidades.append(3)
            if reprobado_unidades:
                self.reprobados.append((self.nombres[i], reprobado_unidades))
            else:
                self.reprobados.append((self.nombres[i], "Aprobado"))

    def resultados(self):
        print("\n****** RESULTADOS FINALES ******")
        for nombre, resultado in self.reprobados:
            if resultado == "Aprobado":
                print(f"{nombre} aprobó la materia")
            else:
                print(f"{nombre} reprobó en la unidad o unidades: {resultado}")

class Menu(Alumnos):
    def __init__(self):
        super().__init__()
        self.prom() 
        self.verificar_reprobados()

    def prom_mas_bajo(self):
        mas_bajo = min(self.promedio)
        indice = self.promedio.index(mas_bajo)
        nombre = self.nombres[indice]
        print(f"\nEl alumno {nombre} obtuvo el promedio más bajo: {mas_bajo}")

    def prom_mas_alto(self):
        mas_alto = max(self.promedio)
        indice = self.promedio.index(mas_alto)
        nombre = self.nombres[indice]
        print(f"\nEl alumno {nombre} obtuvo el promedio más alto: {mas_alto}")

    def buscar(self):
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in self.nombres:
            indice = self.nombres.index(nombre)
            promedio = self.promedio[indice]
            print(f"\nAlumno: {nombre} -- Promedio: {promedio}")
        else:
            print(f"\n\t{nombre} no es alumno del grupo")

    def calif_mas_baja(self):
        calificaciones = self.calif_1 + self.calif_2 + self.calif_3
        mas_baja = min(calificaciones)

        if mas_baja in self.calif_1:
            unidad = 1
            indice = self.calif_1.index(mas_baja)
        elif mas_baja in self.calif_2:
            unidad = 2
            indice = self.calif_2.index(mas_baja)
        else:
            unidad = 3
            indice = self.calif_3.index(mas_baja)

        nombre = self.nombres[indice]
        print(f"El alumno {nombre} obtuvo la calificación más baja {mas_baja} en la unidad: {unidad}")

    def calif_mas_alta(self):
        calificaciones = self.calif_1 + self.calif_2 + self.calif_3
        mas_alta = max(calificaciones)

        if mas_alta in self.calif_1:
            unidad = 1
            indice = self.calif_1.index(mas_alta)
        elif mas_alta in self.calif_2:
            unidad = 2
            indice = self.calif_2.index(mas_alta)
        else:
            unidad = 3
            indice = self.calif_3.index(mas_alta)

        nombre = self.nombres[indice]
        print(f"El alumno {nombre} obtuvo la calificación más alta {mas_alta} en la unidad: {unidad}")

    def prom_califs(self):
        promedio_1 = sum(self.calif_1) / len(self.calif_1)
        promedio_2 = sum(self.calif_2) / len(self.calif_2)
        promedio_3 = sum(self.calif_3) / len(self.calif_3)

        print(f"Promedio de la unidad 1: {round(promedio_1, 2)}")
        print(f"Promedio de la unidad 2: {round(promedio_2, 2)}")
        print(f"Promedio de la unidad 3: {round(promedio_3, 2)}")

    def menu(self):
        while True:  
            print("\n******MENÚ******")
            print("1) El promedio más bajo")
            print("2) El promedio más alto")
            print("3) Buscar alumno")
            print("4) Calificación más baja")
            print("5) Calificación más alta")
            print("6) Promedio de cada Unidad")
            print("7) Mostrar resultados finales")
            opc = int(input("Seleccione una opción: "))
            match opc:
                case 1:
                    self.prom_mas_bajo()
                case 2:
                    self.prom_mas_alto()
                case 3:
                    self.buscar()
                case 4:
                    self.calif_mas_baja()
                case 5:
                    self.calif_mas_alta()
                case 6:
                    self.prom_califs()
                case 7:
                    self.resultados()
                case _:
                    print("Opción no válida")
            input()

practica = Menu()
practica.menu()
