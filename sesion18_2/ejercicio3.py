"""
Sesion 18 - Ejercicio 3
Leer un archivo llamado
archivo.txt linea por
linea e imprimir un arreglo
con todas sus lineas
"""
# Ruta del archivo
#ruta = "C:/python/sesion18_2/archivo.txt"
ruta = "archivo.txt"
# Abrir el archivo
archivo = open(ruta)
# Leer el lineas
contenido = archivo.readlines()
# Imprimir lineas
print(contenido)