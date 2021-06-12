"""
Sesion 18 - Ejercicio 1
Leer un archivo llamado
archivo.txt e imprima
todo su contenido
"""
# Ruta del archivo
#ruta = "C:/python/sesion18_2/archivo.txt"
ruta = "archivo.txt"
# Abrir el archivo
archivo = open(ruta)
# Leer el contenido
contenido = archivo.read()
# Imprimir el contenido
print(contenido)