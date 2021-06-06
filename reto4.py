# RETO NUMERO 4 CURSO MINTIC 2021

# IMPORTACIONES
# Importacion modulo Matematicas
import math
# Importacion modulo terminal
import os

# borramos el terminal
# os.system("cls")

# DECLARAMOS LAS VARIABLES
n = 0
antenas_iniciales = -1
lista_departamentos = []
lista_antenas_a = []
lista_antenas_b = []
lista_antenas_c = []
lista_antenas_d = []
lista_antenas_e = []
antenas_totales = 0
numero_de_antenas = 0

# Funciones
# Funcion para calcular el numero de antenas recibe 3 variables
# (Area de Zona, Antenas Iniciales y Alcance de antena nueva) y retorna el numero de antenas

def nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva):
    numero_de_antenas = (
        area_de_zona-(int(antenas_iniciales)*8_400))/alcance_antena_nueva
    numero_de_antenas = math.ceil(numero_de_antenas)
    if numero_de_antenas <0:
        numero_de_antenas =0
    return numero_de_antenas


# Realizamos un bucle while para que la cantidad de departamentos (Numero entero mayor o igual a cero)
while n < 1:

    # Solicitamos la cantidad de departamentos (n) y la cantidad de zonas o terrenos (m)
    n,m = input().split(" ")
    n = int(n) 
    m = int(m)
    
    # Opcion 2 para solicitar la cantidad de departamentos y cantidad de zonas o terrenos (m)
    """
    datos_iniciales= input().split(" ") 
    n=int(datos_iniciales[0])
    m=int(datos_iniciales[1])
    """
    # Opcion 3 para solicitar la cantidad de departamentos y cantidad de zonas o terrenos (m)
    """n,m = map(int,input().split(" "))"""

# Creamos una lista con el numero de antenas en cada departamento y lo iniciamos en cero
for i in range(n):
    lista_departamentos.append(0)
    lista_antenas_a.append(0)
    lista_antenas_b.append(0)
    lista_antenas_c.append(0)
    lista_antenas_d.append(0)
    lista_antenas_e.append(0)

# ENTRADAS
# Realizamos un ciclo for por cada una de las zonas o terrenos
for i in range(m):
    antenas_a = 0
    antenas_b = 0
    antenas_c = 0
    antenas_d = 0
    antenas_e = 0

    # Realizamos un ciclo while mientras que las antenas iniciales sean menores de 1
    while antenas_iniciales < 0:
      # Solicitamos numero de departamento, area de zona, antenas previamente instaladas y el tipo de antena a instalar
      numero_departamento,area_de_zona,antenas_iniciales,tipo_antenas_nuevas = input().split(" ") 
      numero_departamento = int(numero_departamento) 
      area_de_zona = float(area_de_zona)
      antenas_iniciales = int(antenas_iniciales)
      
      if numero_departamento > n:
        numero_departamento = False

      # Verificacion de tipo de antena a Instalar
      if tipo_antenas_nuevas == "a" and int(antenas_iniciales) >= 0:
        alcance_antena_nueva = 33_600
        # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
        antenas_a = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
        lista_antenas_a[numero_departamento-1] = antenas_a + \
            lista_antenas_a[numero_departamento-1]

      elif tipo_antenas_nuevas == "b" and int(antenas_iniciales) >= 0:
        alcance_antena_nueva = 48_900
        # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
        antenas_b = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
        lista_antenas_b[numero_departamento-1] = antenas_b + \
            lista_antenas_b[numero_departamento-1]
            
      elif tipo_antenas_nuevas == "c" and int(antenas_iniciales) >= 0:
        alcance_antena_nueva = 17_000
        # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
        antenas_c = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
        lista_antenas_c[numero_departamento-1] = antenas_c + \
            lista_antenas_c[numero_departamento-1]
            
      elif tipo_antenas_nuevas == "d" and int(antenas_iniciales) >= 0:
        alcance_antena_nueva = 21_000
        # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
        antenas_d = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
        lista_antenas_d[numero_departamento-1] = antenas_d + \
            lista_antenas_d[numero_departamento-1]
            
      elif tipo_antenas_nuevas == "e" and int(antenas_iniciales) >= 0:
        alcance_antena_nueva = 42_600
        # Ejecuta la funcion nantenas, para hallar el numero de antenas a instalar
        antenas_e = nantenas(area_de_zona, antenas_iniciales, alcance_antena_nueva)
        lista_antenas_e[numero_departamento-1] = antenas_e + \
            lista_antenas_e[numero_departamento-1]
            
      else:
        # Si es un tipo de antena no definido dentro del tipo de antenas (a,b,c,d,e) el tipo de antenas lo coloca como falso
        tipo_antenas_nuevas = False
    
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



print(lista_departamentos)
print("a",lista_antenas_a)
print("b",lista_antenas_b)
print("c",lista_antenas_c)
print("d",lista_antenas_d)
print("e",lista_antenas_e)

for i in range(n):
  print("numero del departamento", i+1)
  print("Cantidad de antenas totales en el departamento", lista_departamentos[i])
  lista_antenas_a[i]
  lista_antenas_b[i]
  lista_antenas_c[i]
  lista_antenas_d[i]
  lista_antenas_e[i]