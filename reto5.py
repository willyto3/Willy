# RETO 5

# Elegimos la Ruta del archivo CSV
ruta = "data.csv"
# Abrimos el archivo data.csv
archivo = open(ruta)

# Leer el lineas
lineas = archivo.readlines()
# Definir un arreglo
matriz = []
# Ciclo para recorrer las lineas
for linea in lineas:
    matriz.append(linea.split(","))

print(matriz)

"""
# Funcion para impresion
# de arreglo bidimensional
def imprimir(a):
    for item in a:
        print(item)
    print()

# Leer el lineas
lineas = archivo.readlines()
# Definir un arreglo
matriz = []
# Ciclo para recorrer las lineas
for linea in lineas:
    matriz.append(linea.split(","))
# Variable de conteo
cont = 0
sum = 0
tipo1 = 'c'
tipo2 = 'a'
# Ciclo de conteo
for fila in matriz:
    fila[3] = fila[3].replace("\n", "")
    if fila[3] == tipo1:
        cont += 1
    elif fila[3] == tipo2:
        sum += int(fila[2])
# Imprimir matriz
imprimir(matriz)
# Imprimir resultados
print("Del tipo", tipo1, "se encontraron", cont, "registros")
print("Del tipo", tipo2, "tiene", sum, "antenas viejas")


Sesion 18 - Ejercicio 5
Leer un archivo llamado
data.csv, convertirlo a
matriz contar cosas.

# Ruta del archivo
ruta = "data.csv"
# Abrir el archivo
archivo = open(ruta)
# Leer el lineas
lineas = archivo.readlines()
# Definir un arreglo
matriz = []
# Ciclo para recorrer las lineas
for i in range(1, len(lineas)):
    matriz.append(lineas[i].split(","))
# Variable de conteo
cont = 0
sum = 0
depto = '1'
nombre = ''
# Definicion de arreglo
tipo = [0, 0, 0, 0, 0]
print(len(matriz))
# Ciclo de conteo
for fila in matriz:
    if fila[0] == depto:
        nombre = fila[1]
        cont += 1
        sum += int(fila[2])
        fila[4] = fila[4].replace("\n", "")
        if fila[4] == 'a':
            tipo[0] += 1
        elif fila[4] == 'b':
            tipo[1] += 1
        elif fila[4] == 'c':
            tipo[2] += 1
        elif fila[4] == 'd':
            tipo[3] += 1
        elif fila[4] == 'e':
            tipo[4] += 1
# Imprimir matriz
f = "{:.2f}"
print(depto, nombre)
print("terrain area")
print("mean", f.format(sum / cont))
print(tipo)

"""