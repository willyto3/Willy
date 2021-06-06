# RETO NUMERO 1 CURSO MINTIC

#IMPORTACIONES
#Importacion modulo Matematicas
import math

# ENTRADAS

# Area de la zona donde se desea instalar las antenas
zona_inicial = float(input("Cual es la zona inicial en m2: "))
# Cantidad de Antenas previamente instaladas
antenas_iniciales = input("Cuantas Antenas estan instaladas: ")
# Tipo de antenas nuevas a Instalar (a, b, c, d, e)
tipo_antenas_nuevas = str(input("Que tipo de Antenas quieres Instalar: "))

# VERIFICACION DE ENTRADAS

# Verificacion de cantidad de antenas previamente instaladas (Debe ser ENTERO y mayor o igual a CERO)

#Verificacion que se igual a cero
if float(antenas_iniciales) == 0:
   pass
# Verificacion que sea un numero entero o menor a cero
elif float(antenas_iniciales)/round(float(antenas_iniciales)) != 1 or float(antenas_iniciales)<0:
    antenas_iniciales=False

   
# Verificacion de tipo de antena a Instalar
if tipo_antenas_nuevas == "a":
    alcance_antena_nueva=33_600
elif tipo_antenas_nuevas == "b":
    alcance_antena_nueva=48_90045

elif tipo_antenas_nuevas == "c":
    alcance_antena_nueva=17_000
elif tipo_antenas_nuevas == "d":
    alcance_antena_nueva=21_000
elif tipo_antenas_nuevas == "e":
    alcance_antena_nueva=42_600
else:
    alcance_antena_nueva=False

# Comprobamos los datos, si estan mal imprimimos error, si estan bien la cantidad de antenas necesarias
if antenas_iniciales == False or alcance_antena_nueva == False:
    print ("Error En Los Datos")
else:
    numero_de_antenas = (zona_inicial-(int(antenas_iniciales)*8_400))/alcance_antena_nueva
    numero_de_antenas = math.ceil(numero_de_antenas)
    print(numero_de_antenas)
