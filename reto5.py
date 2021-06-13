# RETO NUMERO 5 CURSO MINTIC 2021

# IMPORTACIONES
# Importacion modulo Matematicas
import math
# Importacion modulo terminal 
import os

# borramos el terminal
os.system("cls")

# DECLARAMOS LAS VARIABLES
n = 33
antenas_iniciales = -1    
lista_antenas= []
antenas_totales = 0
numero_de_antenas = 0


# Funciones
# Funcion para calcular el numero de antenas recibe 3 variables
# (Area de Zona, Antenas Iniciales y Alcance de antena nueva) y retorna el numero de antena

def nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva):
    numero_de_antenas = (
        area_de_zona-(int(antenas_iniciales)*8_400))/alcance_antena_nueva
    numero_de_antenas = math.ceil(numero_de_antenas)
    if numero_de_antenas <0:
        numero_de_antenas =0
    return numero_de_antenas

"""
# Funcion para buscar la letra (tipo de antena nueva) en función de la posición de la lista_antenas, recibe una variable.
# (Indice) y retorna letra (tipo de antena)

def buscarletra(indice): 
  if indice == 0:
    letra="a"
  elif indice == 1:
    letra="b"
  elif indice == 2:
    letra="c"
  elif indice == 3:
    letra="d"
  elif indice == 4:
    letra="e"
  return letra

"""

# Solicitamos los departamentos a buscar (n) y los guardamos en una lista

lista_departamentos= input().split(" ")

lista_departamentos= list(map(int,lista_departamentos))
lista_departamentos.sort()
lista_departamentos= list(map(str,lista_departamentos))

# Creamos una matriz de departamentos filas (numero de departamento) por 9 columnas (tipo de antenas)
matriz_departamentos=[]

for fila in range(len(lista_departamentos)):
  matriz_departamentos.append([])
  for columna in range(9):
    matriz_departamentos[fila].append(0)


# Elegimos la Ruta del archivo CSV
ruta = "data.csv"
# Abrimos el archivo data.csv
archivo = open(ruta)

# Leer el lineas
lineas = archivo.readlines()
# Definir un arreglo
matriz = []
# Ciclo para recorrer las lineas sin contar la linea 0
for i in range(1, len(lineas)):
  matriz.append(lineas[i].split(","))

# Variable de conteo
for departamento in lista_departamentos:
  indice=lista_departamentos.index(departamento)
  numero_departamento = departamento
  nombre_departamento = ''
  nombres_departamentos=[]
    

  for fila in matriz:
      if fila[0] == numero_departamento:
        nombre_departamento = fila[1]
        matriz_departamentos[indice][5]=numero_departamento
        matriz_departamentos[indice][6]=nombre_departamento
        area_de_zona = float(fila[2])
        antenas_iniciales = int(fila[3])
        tipo_antenas_nuevas = fila[4].replace("\n", "")
        matriz_departamentos[indice][7]+=area_de_zona
        matriz_departamentos[indice][8]+=1

        # ENTRADAS
        # Se reinicia los contadores de las antenas.
        antenas_a = 0
        antenas_b = 0
        antenas_c = 0
        antenas_d = 0
        antenas_e = 0
      
        if int(numero_departamento) > n:
          numero_departamento = False

        # Verificacion de tipo de antena a Instalar
        if tipo_antenas_nuevas == "a" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 33_600
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_a = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "a" en la posición correspondiente de la lista_antenas
          matriz_departamentos[indice][0] = antenas_a + \
              matriz_departamentos[indice][0]

        elif tipo_antenas_nuevas == "b" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 48_900
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_b= nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "b" en la posición correspondiente de la lista_antenas
          matriz_departamentos[indice][1] = antenas_b + \
              matriz_departamentos[indice][1]
              
        elif tipo_antenas_nuevas == "c" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 17_000
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_c = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "c" en la posición correspondiente de la lista_antenas
          matriz_departamentos[indice][2] = antenas_c + \
              matriz_departamentos[indice][2]
              
        elif tipo_antenas_nuevas == "d" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 21_000
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_d = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "d" en la posición correspondiente de la lista_antenas
          matriz_departamentos[indice][3] = antenas_d + \
              matriz_departamentos[indice][3]
              
        elif tipo_antenas_nuevas == "e" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 42_600
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_e = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "e" en la posición correspondiente de la lista_antenas
          matriz_departamentos[indice][4] = antenas_e + \
              matriz_departamentos[indice][4]
              
        else:
          # Si es un tipo de antena no definido dentro del tipo de antenas (a,b,c,d,e) el tipo de antenas lo coloca como falso
          tipo_antenas_nuevas = False

# SALIDAS
f = "{:.2f}"
for departamento in range(len(lista_departamentos)):
  suma = matriz_departamentos[departamento][7]
  print(lista_departamentos[departamento], matriz_departamentos[departamento][6])
  print("terrain area")
  promedio= matriz_departamentos[departamento][7]/matriz_departamentos[departamento][8]
  print("mean", f.format(promedio)

