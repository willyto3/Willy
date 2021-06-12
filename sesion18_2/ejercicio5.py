"""
Sesion 18 - Ejercicio 5
Leer un archivo llamado
data.csv, convertirlo a
matriz contar cosas.
"""
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