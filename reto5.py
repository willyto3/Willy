# RETO NUMERO 5 CURSO MINTIC 2021

# IMPORTACIONES
# Importacion modulo Matematicas
import math
# Importacion modulo terminal 
import os
# Importacion modulo de Estadistica 
import statistics

# borramos el terminal
os.system("cls")

def main():
  # DECLARAMOS LAS VARIABLES
  n = 33
  antenas_iniciales = -1
  antenas_totales = 0
  numero_de_antenas = 0
  # iniciamos las listas para guardar los valores de cada area y antenas iniciales    
  lista_area_zonas= []
  lista_antenas_iniciales= []


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

  # Solicitamos los departamentos a buscar (n) y los guardamos en una lista
  lista_departamentos= input().split(" ")
  # Convertimos la lista de los departamentos en enteros
  lista_departamentos= list(map(int,lista_departamentos))
  # Organizamos en orden ascendente la lista de departamentos
  lista_departamentos.sort()
  # Convertimos la lista de los departamentos en string
  lista_departamentos= list(map(str,lista_departamentos))

  # Creamos una matriz de departamentos filas (numero de departamento) por 10 columnas
  # columnas 0 a 4 Antenas (a,b,c,d,e)
  #columna 5 numero del departamento
  # Columna 6 nombre del departamento
  # Columna 7 area de zona total     
  # columna 8 contador de veces que se repite el departamento     
  #columna 9 antenas iniciales totales
  matriz_departamentos=[]

  # Llenamos la matriz departamento con ceros
  for fila in range(len(lista_departamentos)):
    matriz_departamentos.append([])
    for columna in range(10):
      matriz_departamentos[fila].append(0)

  # Elegimos la Ruta del archivo CSV
  ruta = "data.csv"
  # Abrimos el archivo data.csv
  archivo = open(ruta)

  # Leemos las lineas del archivo CSV
  lineas = archivo.readlines()
  # Definir un arreglo matriz para guardar los datos del archivo CSV
  matriz = []
  # Ciclo para recorrer las lineas sin contar la linea 0
  # se utiliza el split con ","" por que el archivo viene separados por ","
  # se coloca desde el rango 1, para no guardar el nombre de la tabla
  for i in range(1, len(lineas)):
    matriz.append(lineas[i].split(","))

  # recorremos la lista departamentos
  for departamento in lista_departamentos:
    # hallamos el indice del departamento
    indice=lista_departamentos.index(departamento)
    # hallamos el numero del departamento
    numero_departamento = departamento
    # Asignamos el nombre del departamento vacio
    nombre_departamento = ''
    # Creamos las listas vacias nombres de departamento
    nombres_departamentos=[]
      
    # recorremos la matriz con que se lleno los archivos del CSV
    for fila in matriz:
      # comparamos la columna cero de cada fila con el numero del departamento
      # si es verdadero guardamos los datos en la matriz departamento  
      if fila[0] == numero_departamento:
        nombre_departamento = fila[1]
        matriz_departamentos[indice][5]=numero_departamento
        matriz_departamentos[indice][6]=nombre_departamento
        area_de_zona = float(fila[2])
        antenas_iniciales = int(fila[3])
        # reemplazamos el dato "/n" por vacio
        tipo_antenas_nuevas = fila[4].replace("\n", "")
        # acumulador de las areas de zona
        matriz_departamentos[indice][7]+=area_de_zona
        # contador de las veces que se repite el departamento
        matriz_departamentos[indice][8]+=1
        # acumulador de las antenas iniciales
        matriz_departamentos[indice][9]+=antenas_iniciales
        # Se llena la lista area zonas con cada valor que encuentra en la matriz
        lista_area_zonas.append(area_de_zona)
        # Se llena la lista antenas iniciales con cada valor que encuentra en la matriz
        lista_antenas_iniciales.append(antenas_iniciales)

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
          # Guardamos el dato de antenas "a" en la posición correspondiente de la matriz departamentos
          matriz_departamentos[indice][0] = antenas_a + \
              matriz_departamentos[indice][0]

        elif tipo_antenas_nuevas == "b" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 48_900
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_b= nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "b" en la posición correspondiente de la matriz departamentos
          matriz_departamentos[indice][1] = antenas_b + \
              matriz_departamentos[indice][1]
              
        elif tipo_antenas_nuevas == "c" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 17_000
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_c = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "c" en la posición correspondiente de la matriz departamentoss
          matriz_departamentos[indice][2] = antenas_c + \
              matriz_departamentos[indice][2]
              
        elif tipo_antenas_nuevas == "d" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 21_000
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_d = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "d" en la posición correspondiente de la matriz departamentoss
          matriz_departamentos[indice][3] = antenas_d + \
              matriz_departamentos[indice][3]
              
        elif tipo_antenas_nuevas == "e" and int(antenas_iniciales) >= 0:
          alcance_antena_nueva = 42_600
          # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
          antenas_e = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
          # Guardamos el dato de antenas "e" en la posición correspondiente de la matriz departamentos
          matriz_departamentos[indice][4] = antenas_e + \
              matriz_departamentos[indice][4]
              
        else:
          # Si es un tipo de antena no definido dentro del tipo de antenas (a,b,c,d,e) el tipo de antenas lo coloca como falso
          tipo_antenas_nuevas = False

        

    # SALIDAS
    # Declaramos el formato de 2 cifras decimales
    f = "{:.2f}"
    # Imprimimos el numero del departamento y el nombre del departamento   
    print(lista_departamentos[indice], matriz_departamentos[indice][6])
    print("terrain area")
    # Calculamos el promedio de las areas de zona del departamento
    promedio= matriz_departamentos[indice][7]/matriz_departamentos[indice][8]
    # Imprimimos el promedio de las areas de zona del departamento
    print("mean", f.format(promedio))
    # Calculamos la desviacion de las areas de zona del departamento
    desviacion = statistics.stdev(lista_area_zonas)
    # Imprimimos la desviacion de las areas de zona del departamento
    print("std", f.format(desviacion))
    # Imprimimos el valor minimo de las areas de zona del departamento
    print("min", f.format(min(lista_area_zonas)))
    # Imprimimos el valor maximo de las areas de zona del departamento
    print("max", f.format(max(lista_area_zonas)))
    # Imprimimos el valor total de las areas de zona del departamento
    print("total", f.format(matriz_departamentos[indice][7]))

    print("old antenna")
    # Calculamos el promedio de las antenas iniciales del departamento
    promedio= matriz_departamentos[indice][9]/matriz_departamentos[indice][8]
    # Calculamos la desviacion de las antenas iniciales del departamento
    desviacion = statistics.stdev(lista_antenas_iniciales)
    # Imprimimos el promedio de las antenas iniciales del departamento
    print("mean", f.format(promedio))
    # Imprimimos la desviacion de las antenas iniciales departamento
    print("std", f.format(desviacion))
    # Imprimimos el minimo de las antenas iniciales departamento
    print("min", min(lista_antenas_iniciales))
    # Imprimimos el maximo de las antenas iniciales departamento
    print("max", max(lista_antenas_iniciales))
    # Imprimimos el total de las antenas iniciales departamento
    print("total", matriz_departamentos[indice][9])
    
    print("new antenna")
    # Imprimimos las cantidades totales de cada tipo de antena nueva por departamento
    print("a", matriz_departamentos[indice][0])
    print("b", matriz_departamentos[indice][1])
    print("c", matriz_departamentos[indice][2])
    print("d", matriz_departamentos[indice][3])
    print("e", matriz_departamentos[indice][4])

    # Borramos las listas area zonas y antenas iniciales para poder reutilizarlas en el proximo departamento
    lista_area_zonas.clear()
    lista_antenas_iniciales.clear()
  

