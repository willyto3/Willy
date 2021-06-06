# RETO NUMERO 2 CURSO MINTIC

# IMPORTACIONES
# Importacion modulo Matematicas
import math

# Declaramos Variables de antenas, porcentajes y antenas totales iguales a Cero
antenas_a = 0
antenas_b = 0
antenas_c = 0
antenas_d = 0
antenas_e = 0
porcentaje_a = 0
porcentaje_b = 0
porcentaje_c = 0
porcentaje_d = 0
porcentaje_e = 0
antenas_totales = 0
numero_de_antenas = 0
acumulado_a = 0
acumulado_b = 0
acumulado_c = 0
acumulado_d = 0
acumulado_e = 0

# Funciones

# Funcion para calcular el numero de antenas recibe 3 variables
# (Zona Inicial, Antenas Iniciales y Alcance de antena nueva) y retorna el numero de antenas


def nantenas(zona_inicial, antenas_iniciales, alcance_antena_nueva):
    numero_de_antenas = (
        zona_inicial-(int(antenas_iniciales)*8_400))/alcance_antena_nueva
    numero_de_antenas = math.ceil(numero_de_antenas)
    return numero_de_antenas


# ENTRADAS

# Numero de Zonas que se van a Analizar (Numero entero mayor o igual a cero)

numero_de_zonas = int(input("Numero de Zonas a Analizar: "))

# Verificamos que valor tiene el numero de zonas

if numero_de_zonas == 0:  # Verificacion si es Cero
    numero_de_antenas = 0

else:  # Verificacion de un valor mayor que Cero

    # Asignamos un contador
    i = 0

    # Realizamos un bucle para solicitar el area inicial, el numero de antenas previamente instaladas y el tipo de antenas nuevas a instalar

    while i < numero_de_zonas:
        # Area de la zona donde se desea instalar las antenas
        zona_inicial = float(
            input("Cual es la zona inicial en m2 del area " + str(i+1) + ":"))

        # Cantidad de Antenas previamente instaladas
        antenas_iniciales = input(
            "Cuantas Antenas estan instaladas en el area " + str(i+1) + " :")

        # Tipo de antenas nuevas a Instalar (a, b, c, d, e)
        tipo_antenas_nuevas = str(
            input("Que tipo de Antenas quieres Instalar en el area " + str(i+1)+" : "))

        # Verificacion de tipo de antena a Instalar
        if tipo_antenas_nuevas == "a" and int(antenas_iniciales) >= 0:
            alcance_antena_nueva = 33_600
            # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
            antenas_a = nantenas(
                zona_inicial, antenas_iniciales, alcance_antena_nueva)
            acumulado_a = acumulado_a + antenas_a

        elif tipo_antenas_nuevas == "b" and int(antenas_iniciales) >= 0:
            alcance_antena_nueva = 48_900
            # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
            antenas_b = nantenas(
                zona_inicial, antenas_iniciales, alcance_antena_nueva)
            acumulado_b = acumulado_b + antenas_b

        elif tipo_antenas_nuevas == "c" and int(antenas_iniciales) >= 0:
            alcance_antena_nueva = 17_000
            # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
            antenas_c = nantenas(
                zona_inicial, antenas_iniciales, alcance_antena_nueva)
            acumulado_c = acumulado_c + antenas_c

        elif tipo_antenas_nuevas == "d" and int(antenas_iniciales) >= 0:
            alcance_antena_nueva = 21_000
            # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
            antenas_d = nantenas(
                zona_inicial, antenas_iniciales, alcance_antena_nueva)
            acumulado_d = acumulado_d + antenas_d

        elif tipo_antenas_nuevas == "e" and int(antenas_iniciales) >= 0:
            alcance_antena_nueva = 42_600
            # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
            antenas_e = nantenas(
                zona_inicial, antenas_iniciales, alcance_antena_nueva)
            acumulado_e = acumulado_e + antenas_e

        # Se aumenta el contador
        i += 1  # i = i+1

    # Se calculan las antenas totales requeridas
    antenas_totales = acumulado_a + acumulado_b + \
        acumulado_c + acumulado_d + acumulado_e

    # Condicional para que no se presente division entre Cero
    if antenas_totales != 0:
        porcentaje_a = (acumulado_a / antenas_totales)*100
        porcentaje_b = (acumulado_b / antenas_totales)*100
        porcentaje_c = (acumulado_c / antenas_totales)*100
        porcentaje_d = (acumulado_d / antenas_totales)*100
        porcentaje_e = (acumulado_e / antenas_totales)*100

# Impresion de Resultados, se utiliza %.2f para imprimir los decimales
print(antenas_totales)
print("a " + "%.2f" % porcentaje_a + "%")
print("b " + "%.2f" % porcentaje_b + "%")
print("c " + "%.2f" % porcentaje_c + "%")
print("d " + "%.2f" % porcentaje_d + "%")
print("e " + "%.2f" % porcentaje_e + "%")
