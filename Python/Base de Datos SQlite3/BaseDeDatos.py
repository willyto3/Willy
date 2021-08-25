# Importamos la libreria de SQlite 3
import sqlite3

# Creamos la conexion de la base de datos
conexion = sqlite3.connect('personas.db')

print("Base de Datos Creada o Abierta")

"""
# Se ejecuta una conexion y se crea la tabla.
# ID entero llave primaria no puede ser nulo
# NAME texto no puede ser nulo
conexion.execute(
    'CREATE TABLE USUARIOS (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);')

print("La Tabla USUARIOS fue creada satisfactoriamente")

# Se insertan datos en la tabla usuarios
conexion.execute('INSERT INTO USUARIOS (ID, NAME) VALUES (1, "WILLY")')
# Se realizan los cambios
conexion.commit()

print("Usuario añadido exitosamente") """

""" # Se borra una entrada de la tabla USUARIOS
conexion.execute('DELETE FROM USUARIOS WHERE ID=1')
# Se guardan los cambios
conexion.commit() """

# Actualizar una entrada en la tabla USUARIOS
conexion.execute('UPDATE USUARIOS SET NAME ="WILLY LAUREANO" WHERE ID=1')
# Se guardan los cambios
conexion.commit()

#Mostrar datos de la tabla Usuarios
cursor = conexion.execute('SELECT * FROM USUARIOS')
for fila in cursor:
    print(fila)

conexion.close()
