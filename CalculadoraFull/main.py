from tkinter import *


# Creando la pantalla de arranque
pantallasplash = Tk()

# Esconder la barra de titulo
pantallasplash.overrideredirect(True)

# Asignamos el alto y el ancho de nuestra aplicacion
anchoapp = 400
altoapp = 400

# Obtenemos el ancho y el alto de la pantalla
anchopantalla = pantallasplash.winfo_screenwidth()
altopantalla = pantallasplash.winfo_screenheight()

# Obtenemos las coordenadas del centro
x = (anchopantalla / 2) - (anchoapp / 2)
y = (altopantalla / 2) - (altoapp / 2)

# Centramos la pantalla inicial
pantallasplash.geometry(f"{anchoapp}x{altoapp}+{int(x)}+{int(y)}")


# Creamos la funcion pantalla principal
def pantallaprincipal():

    # Pantalla Principal
    pantallasplash.destroy()
    pantallainicial = Tk()
    pantallainicial.title("CALCULADORA")
    pantallainicial.iconbitmap('C:/Users/willy/Desktop/Proyectos Willy/CalculadoraFull/Health.contrast-black.ico')

    # Asignamos el alto y el ancho de nuestra aplicacion
    anchoapp2 = 500
    altoapp2 = 400

    # Obtenemos el ancho y el alto de la pantalla
    anchopantalla2 = pantallainicial.winfo_screenwidth()
    altopantalla2 = pantallainicial.winfo_screenheight()

    # Obtenemos las coordenadas del centro
    x2 = (anchopantalla2 / 2) - (anchoapp2 / 2)
    y2 = (altopantalla2 / 2) - (altoapp2 / 2)

    # Centramos la pantalla inicial
    pantallainicial.geometry(f"{anchoapp2}x{altoapp2}+{int(x2)}+{int(y2)}")

    # Creando funcion Credito
    def credito():
        pass

    # Creamos el Menu
    mimenu = Menu(pantallainicial)
    pantallainicial.config(menu=mimenu)

    # Añadimos items al el menu
    filemenu = Menu(mimenu, tearoff=False)
    mimenu.add_cascade(label="Opciones", menu=filemenu)
    filemenu.add_command(label="Creditos", command=credito)
    filemenu.add_command(label="Salir", command=exit)

    # Creando funcion numero
    def click_boton(numero):
        actual = campo.get()
        campo.delete(0, END)
        campo.insert(0, str(actual) + str(numero))

    # Creando funcion limpiar
    def limpiar_boton():
        campo.delete(0, END)

    # Creando funcion sumar
    def sumar_boton():
        temporal = campo.get()
        global num1
        global funcion
        funcion = "suma"
        num1 = int(temporal)
        campo.delete(0, END)

    # Creando funcion restar
    def restar_boton():
        temporal = campo.get()
        global num1
        global funcion
        funcion = "resta"
        num1 = int(temporal)
        campo.delete(0, END)

    # Creando funcion division
    def division_boton():
        temporal = campo.get()
        global num1
        global funcion
        funcion = "division"
        num1 = int(temporal)
        campo.delete(0, END)

    # Creando funcion multiplicacion
    def multiplicacion_boton():
        temporal = campo.get()
        global num1
        global funcion
        funcion = "multiplicacion"
        num1 = int(temporal)
        campo.delete(0, END)

    # Creando funcion igual
    def igual_boton():
        temporal = campo.get()
        campo.delete(0, END)
        num2 = int(temporal)
        if funcion == "suma":
            campo.insert(0, num2 + num1)
        if funcion == "resta":
            campo.insert(0, num1 - num2)
        if funcion == "multiplicacion":
            campo.insert(0, num2 * num1)
        if funcion == "division":
            campo.insert(0, num1 / num2)

    # Creando Campo de Ingreso
    campo = Entry(pantallainicial, width=60, borderwidth=2)

    # Creando Botones
    boton1 = Button(pantallainicial, text="1", padx=30, pady=10, command=lambda: click_boton(1))
    boton2 = Button(pantallainicial, text="2", padx=30, pady=10, command=lambda: click_boton(2))
    boton3 = Button(pantallainicial, text="3", padx=30, pady=10, command=lambda: click_boton(3))
    boton4 = Button(pantallainicial, text="4", padx=30, pady=10, command=lambda: click_boton(4))
    boton5 = Button(pantallainicial, text="5", padx=30, pady=10, command=lambda: click_boton(5))
    boton6 = Button(pantallainicial, text="6", padx=30, pady=10, command=lambda: click_boton(6))
    boton7 = Button(pantallainicial, text="7", padx=30, pady=10, command=lambda: click_boton(7))
    boton8 = Button(pantallainicial, text="8", padx=30, pady=10, command=lambda: click_boton(8))
    boton9 = Button(pantallainicial, text="9", padx=30, pady=10, command=lambda: click_boton(9))
    boton0 = Button(pantallainicial, text="0", padx=30, pady=10, command=lambda: click_boton(0))
    botonsuma = Button(pantallainicial, text="+", padx=30, pady=10, command=sumar_boton)
    botonresta = Button(pantallainicial, text="-", padx=30, pady=10, command=restar_boton)
    botonmultiplicacion = Button(pantallainicial, text="*", padx=30, pady=10, command=multiplicacion_boton)
    botondivision = Button(pantallainicial, text="/", padx=30, pady=10, command=division_boton)
    botonigual = Button(pantallainicial, text="=", padx=30, pady=10, command=igual_boton)
    botonborrar = Button(pantallainicial, text="CE", padx=26, pady=10, command=limpiar_boton)

    # Creando lista de Botones
    lista_botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0, botonborrar,
                     botonigual, botondivision, botonresta, botonsuma, botonmultiplicacion]

    # Definimos el contador numero de fila y columna
    contador = 0

    # Ciclo en la lista de botones para configurar cada fila y columna
    for button in lista_botones:
        Grid.rowconfigure(pantallainicial, contador, weight=1)
        Grid.columnconfigure(pantallainicial, contador, weight=1)
        # Incrementando el contador
        contador += 1

    def resize(e):
        size = e.width / 25
        # Configurar el tamaño del entry
        campo.config(font=("Helvetica", int(size)))
        # Ciclo en la lista de botones para configurar cada boton
        for button2 in lista_botones:
            button2.config(font=("Helvetica", int(size)))

    # Bind la aplicacion
    pantallainicial.bind("<Configure>", resize)

    # Mostrando Elementos en pantalla
    campo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
    boton7.grid(row=1, column=0, sticky="nsew")
    boton8.grid(row=1, column=1, sticky="nsew")
    boton9.grid(row=1, column=2, sticky="nsew")
    boton4.grid(row=2, column=0, sticky="nsew")
    boton5.grid(row=2, column=1, sticky="nsew")
    boton6.grid(row=2, column=2, sticky="nsew")
    botonresta.grid(row=2, column=3, sticky="nsew")
    boton1.grid(row=3, column=0, sticky="nsew")
    boton2.grid(row=3, column=1, sticky="nsew")
    boton3.grid(row=3, column=2, sticky="nsew")
    botonmultiplicacion.grid(row=3, column=3, sticky="nsew")
    botonsuma.grid(row=1, column=3, sticky="nsew")
    botonborrar.grid(row=4, column=0, sticky="nsew")
    boton0.grid(row=4, column=1, sticky="nsew")
    botondivision.grid(row=4, column=2, sticky="nsew")
    botonigual.grid(row=4, column=3, sticky="nsew")


# temporizador de la pantalla Splash
pantallasplash.after(4000, pantallaprincipal)

mainloop()
