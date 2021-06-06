import os
os.system("cls")
#Variables
med1 = int(input())
med2 = int(input())
contador = 0
paciente1 = 0
paciente2 = 0
pacientet = 0
porcentaje1 = 0
porcentaje2 = 0

while med1 > 0 and med2 > 0:

    estado = input().lower()
    nivel_glucosa = float(input())
    contador = contador + 1

#Procesos
    if estado == 'ayunas':
        if nivel_glucosa < 0.44:
            med2 = med2 - 4
            paciente2 = paciente2 + 1
            pacientet = pacientet + 1
            #categoria = 'hipoglusemia'
            
        elif 0.44 <= nivel_glucosa < 0.61:
            pacientet = pacientet + 1
            #categoria = 'normal'

        elif  0.61 <= nivel_glucosa < 0.7:
            med1 = med1 - 6
            paciente1 = paciente1 + 1
            pacientet = pacientet + 1
            #categoria = 'elevado'
            
        elif nivel_glucosa >= 0.7:
            med1 = med1 - 12
            paciente1 = paciente1 + 1
            pacientet = pacientet + 1
            #categoria = 'diabetes'
            
    elif estado == 'posprandial':
        if nivel_glucosa < 0.78:
            pacientet = pacientet + 1
            #categoria = 'normal'

        elif 0.78 <= nivel_glucosa < 1.1:
            paciente1 = paciente1 + 1
            pacientet = pacientet + 1
            med1 = med1 - 9
            #categoria = 'elevado'
                
        elif nivel_glucosa >= 1.1:
            paciente1 = paciente1 + 1
            pacientet = pacientet + 1
            med1 = med1 - 18
            categoria = 'diabetes'
                
    else:
        pacientet = pacientet + 1
if contador == 0:
    contador = 1

porcentaje1 = round(paciente1/contador*100,2)
porcentaje2 = round(paciente2/contador*100,2)

#Salidas

print(f'''{pacientet}
{paciente1} {porcentaje1}%
{paciente2} {porcentaje2}%''')