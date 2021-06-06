# Importaciones
# Importar modulo para poder hacer la parte grafica
from tkinter import *
# Importar modulo para manejar imagenes
#from PIL import ImageTK, Image
# Importar modulo para realizar conexiones a MYSQL
import mysql.connector

ventanainicial = Tk()
ventanainicial.geometry("600x600")

miconexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="LaurenAndrea2012",
    database="Personal"
)

# Crear un cursor y inicializarlo
micursor = miconexion.cursor()

# Crear la Base de Datos
# micursor.execute("CREATE DATABASE PERSONAL")

# Crear la Tabla Personas
micursor.execute("CREATE TABLE IF NOT EXISTS Personas (cedula INT (15), \
    primer_nombre VARCHAR(255), \
    segundo_nombre VARCHAR(255), \
    primer_apellido VARCHAR(255), \
    segundo_apellido VARCHAR (255), \
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

# micursor.execute("SHOW DATABASES")
# for db in micursor:
#     print(db)

# Mostrar la tabla Personas
micursor.execute("SELECT * FROM Personas")
#print(micursor.description)

for algo in micursor.description:
    print(algo)

# CREAR PARTE GRAFICA

# Crear parte grafica

#
titulo =Label(ventanainicial, text="SANTANDER Base de Datos del Personal", font=("helvetica", 40))
titulo.pack()


mainloop()

