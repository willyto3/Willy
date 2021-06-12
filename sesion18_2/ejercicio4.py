"""
Sesion 18 - Ejercicio 4
Leer un archivo llamado
reto.txt, convertirlo a
matriz e imprimirlo en
pantalla
"""
# Funcion para impresion
# de arreglo bidimensional
def imprimir(a):
    for item in a:
        print(item)
    print()

# Ruta del archivo
#ruta = "C:/python/sesion18_2/reto.txt"
ruta = "reto.csv"
# Abrir el archivo
archivo = open(ruta)
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
