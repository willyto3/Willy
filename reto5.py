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

lista_departamentos.sort()

# Creamos una matriz de departamentos filas (numero de departamento) por 5 columnas (tipo de antenas)
matriz_departamentos=[]

for fila in range(len(lista_departamentos)):
  matriz_departamentos.append([])
  for columna in range(5):
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
  

  for fila in matriz:
      if fila[0] == numero_departamento:
        nombre_departamento = fila[1]
        area_de_zona = float(fila[2])
        antenas_iniciales = int(fila[3])
        tipo_antenas_nuevas = fila[4].replace("\n", "")

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

print(matriz_departamentos)

"""  
    # Comprobamos que  tipo de antenas nuevas y numero de departamento correspondan a los tipos establecidos
    if tipo_antenas_nuevas != False and numero_departamento != False:
      # Se calculan las antenas totales requeridas
      antenas_totales = antenas_a + antenas_b + antenas_c + antenas_d + antenas_e
    else:
      # Si el tipo de anteas nuevas y el numero de departamento no estan en el rango, las antenas totales son iguales a cero.
      antenas_totales = 0

    # Se le da un valor de -1 a antenas iniciales para que ingrese nuevamente al ciclo while
    antenas_iniciales = -1

    # Se asigna las antenas totales que tiene el departamento (se acumula en la lista)
    lista_departamentos[numero_departamento-1] = antenas_totales + \
        lista_departamentos[numero_departamento-1]

# SALIDAS
# Se implementa un for para recorrer las columnas.
for columna in range(n):
  # Creamos una lista vacía "lista", para guardar la cantidad de cada tipo de antenas por departamento.
  lista=[]
  # Se imprime la primera salida que pide el ejercicio: el número del departamento.
  print(columna+1)
  # Se imprime la segunda salida que pide el ejercicio: cantidad de antenas totales de dicho departamento.
  print(lista_departamentos[columna])

  # Se utiliza un for anidado para recorrer las filas (tipo de antenas)
  for fila in range(5):
    # Se llena la lista con los datos de cada departamento. 
    lista.append(lista_antenas[fila][columna])
  
  # Se utiliza la función menor, para hallar el valor menor en la lista.
  menor=min(lista)
  # Se imprime la tercera salida que pide el ejercicio: 
  # Halla El tipo de nueva antena con menor cantidad instalada, seguido de su valor correspondiente.
  print(buscarletra(lista.index(menor)), menor)
  
  # Se utiliza la función mayor, para hallar el valor mayor en la lista.
  mayor=max(lista)

  # Se imprime la cuarta salida que pide el ejercicio: 
  # Halla El tipo de nueva antena con mayor cantidad instalada, seguido de su valor correspondiente.
  print(buscarletra(lista.index(mayor)), mayor)


# Se implementa un for para recorrer las filas.
for fila in range(5):
  # Creamos una lista vacía "lista", para guardar la cantidad de antenas nuevas de un tipo por cada departamento.
  lista=[]
  # Se utiliza un for anidado para recorrer las columnas (departamentos)
  for columna in range(n):
    
    # Se llena la lista con los datos de cada tipo de antenas. 
    lista.append(lista_antenas[fila][columna])

  # Se utiliza la función menor, para hallar el valor menor en la lista.
  menor=min(lista)
  
  # Se imprime la quinta salida que pide el ejercicio: 
  # Halla El número del departamento con menor cantidad de antenas instaladas del tipo correspondiente, seguido del tipo de la nueva antena y el valor de las nuevas antenas instaladas de ese tipo.
  print(lista.index(menor)+1, buscarletra(fila), menor)
  
  
  # Se utiliza la función mayor, para hallar el valor mayor en la lista.
  mayor=max(lista)

  # Se imprime la sexta salida que pide el ejercicio: 
  # Halla El número del departamento con mayor cantidad de antenas instaladas del tipo correspondiente, seguido del tipo de la nueva antena y el valor de las nuevas antenas instaladas de ese tipo.
  print(lista.index(mayor)+1, buscarletra(fila), mayor)





# Funcion para impresion
# de arreglo bidimensional
def imprimir(a):
    for item in a:
        print(item)
    print()
  

"""
"""          
  # Imprimir matriz
  f = "{:.2f}"
  print(depto, nombre)
  print("terrain area")
  print("mean", f.format(sum / cont))
  print(tipo)
"""