"""
Sesion 18 - Ejercicio 2
Leer un archivo llamado
archivo.txt e imprima
la linea 1 y la linea 2
"""
# Ruta del archivo
#ruta = "C:/python/sesion18_2/archivo.txt"
ruta = "archivo.txt"
# Abrir el archivo
archivo = open(ruta)
# Leer el linea 1
contenido = archivo.readline()
# Imprimir linea 1
print(contenido)
# Leer el linea 2
contenido = archivo.readline()
# Imprimir linea 2
print(contenido)