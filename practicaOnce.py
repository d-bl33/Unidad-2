#& ARRAYS. Arreglos. VECTORES

alumnos = ["Juan", "Pedro", "Luis"]
print(alumnos[0])
print(alumnos[2])
print()
print(alumnos[-1])
print(alumnos[-2])
print(alumnos[-3])
#print(alumnos[-4]) marca error, porque está fuera del rango

print()
#* Arreglo Combinado
alumnos = ["Juan", "Pedro", "Luis", 13] #Arreglo de 4 valores
print(alumnos)

print("\nRECORRIENDO ELEMENTOS")
for alumno in alumnos: #recorriendo elementos
    print(alumno)

print("\nRECORRIENDO ÍNDICES")
for i in range(len(alumnos)):
    print(alumnos[i])#recorriendo los índices (i)

print("\nRECORRIENCO CON WHILE Y LOS ÍNDICES")
indice = 0
while indice < len(alumnos):
    print(alumnos[indice])
    indice += 1

print("\nAGREGAR VALORES AL ARREGLO")
numeros = []
numeros.append(45)
numeros.append(98)
numeros.append(72)
print(numeros)

print("\nQUITAR VALORES")
numeros.pop()# sin argumento se elimina el último elemento de la lista (72)
alumnos.remove("Juan")
print(numeros)
print(alumnos)

print("\nBUSCAR LA POSICIÓN (ÍNDICE) DE UN ELEMENTO")
n = "Luis"
alumnos.index(n)
print(alumnos)

#* Buscar con for
print()
for i in range (len(alumnos)):
    if alumnos [i] == "Luis": #alumnos posición i
        print(f"{alumnos [i]} si existe en la lista en {i+1}")

#* Buscar con una función
print()
if "Luis" in alumnos:
    print("Si existe Luis en la lista")
else:
    print("No existe en la lista")

#* Obtener el índice del elemento
indice = alumnos.index("Luis")
print(f"\nLa posición de Luis es {indice}")

#* Buscar la posición con Try
try:
    indice = alumnos.index("Lola")
    print(f"\nLa posición de Luis es {indice}")
except ValueError:
    print("\nNo existe Lola en la lista")
