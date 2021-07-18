# Importaciones

# Importar modulo para realizar conexiones a MYSQL wILLY Colso
import mysql.connector


def conexion_datos():
    global miconexion
    miconexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="admin",
        database="Personal"
    )

    # Crear un cursor y inicializarlo
    micursor = miconexion.cursor()

    # Crear la Base de Datos
    #micursor.execute("CREATE DATABASE PERSONAL")

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
    # print(micursor.description)

    resultados = micursor.fetchall()
    for resultado in resultados:
        print(resultado)

def generarusuario(comandoSQL, valores):
    
    # Crear un cursor y inicializarlo
    micursor = miconexion.cursor()

    
    micursor.execute(comandoSQL, valores)
    print("Entre")

    # Guardar los datos en la base de Datos MYSQL
    miconexion.commit()