from sqlite3.dbapi2 import Connection
from sqlite3.dbapi2 import Cursor
from tkinter import *
import sqlite3

# Creando la pantalla de inicio
splash = Tk()

# Esconder la barra de titulo
splash.overrideredirect(True)

# Asignamos el alto y el ancho de nuestra aplicacion
anchoapp = 400
altoapp = 400

# Obtenemos el ancho y el alto de la pantalla
anchopantalla = splash.winfo_screenwidth()
altopantalla = splash.winfo_screenheight()

# Obtenemos las coordenadas del centro
x = (anchopantalla / 2) - (anchoapp / 2)
y = (altopantalla / 2) - (altoapp / 2)

# Centramos la pantalla inicial
splash.geometry(f"{anchoapp}x{altoapp}+{int(x)}+{int(y)}")

# BASE DE DATOS

# Crear la Base de Datos o Conectarse a una
conn = sqlite3.connect("Datos_Personal")

# Crear el Cursor
c = conn.cursor()

# # Crear Tablas
# c.execute("CREATE TABLE DatosPersonal (\n"
#           "        ID integer,\n"
#           "        pnombre text,\n"
#           "        snombre text,\n"
#           "        papellido text,\n"
#           "        sapellido text,\n"
#           "        direccion text,\n"
#           "        ciudad text,\n"
#           "        celular integer  )\n"
#           "    ")

# Commit Cambios
conn.commit()

# Cerrar Conexion
conn.close()


# Creamos la funcion pantalla principal
def pantallaprincipal():
    # Pantalla Principal
    splash.destroy()
    pantallainicial = Tk()
    pantallainicial.title("BASE DE DATOS")
    pantallainicial.iconbitmap('icono.ico')
    pantallainicial.geometry("600x600")

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

    # Creando funcion limpiar
    def limpiar():
        # Limpiar campos de ingreso
        c_id.delete(0, END)
        c_pnombre.delete(0, END)
        c_snombre.delete(0, END)
        c_papellido.delete(0, END)
        c_sapellido.delete(0, END)
        c_direcion.delete(0, END)
        c_ciudad.delete(0, END)
        c_celular.delete(0, END)
        c_seleccionar.delete(0, END)

    # Creando funcion para añadir un registro
    def anadirregistro():
        # Crear la Base de Datos o Conectarse a una
        conn: Connection = sqlite3.connect("Datos_Personal")

        # Crear el Cursor
        c: Cursor = conn.cursor()

        # Insertar Datos en la Base de Datos
        c.execute("INSERT INTO DatosPersonal VALUES(\n"
                  "        :ID,\n"
                  "        :pnombre,\n"
                  "         :snombre ,\n"
                  "        :papellido,\n"
                  "        :sapellido ,\n"
                  "        :direccion ,\n"
                  "        :ciudad ,\n"
                  "        :celular  )\n",
                  {
                      "ID": c_id.get(),
                      "pnombre": c_pnombre.get(),
                      "snombre": c_snombre.get(),
                      "papellido": c_papellido.get(),
                      "sapellido": c_sapellido.get(),
                      "direccion": c_direcion.get(),
                      "ciudad": c_ciudad.get(),
                      "celular": c_celular.get()
                  })
        # Llamamos la funcion limpiar
        limpiar()

        # Commit Cambios
        conn.commit()

        # Cerrar Conexion
        conn.close()

    # Creando funcion para eliminar un Registro
    def eliminarregistro():
        # Crear la Base de Datos o Conectarse a una
        conn: Connection = sqlite3.connect("Datos_Personal")

        # Crear el Cursor
        c: Cursor = conn.cursor()

        # Eliminar un registro de la Base de Datos
        c.execute("DELETE from DatosPersonal WHERE oid=" + c_seleccionar.get())

        # Borrar registros en pantalla
        c_seleccionar.delete(0, END)
        # Pendiente borrar label de busqueda

        # Commit Cambios
        conn.commit()

        # Cerrar Conexion
        conn.close()

    # Creando funcion Actualizar un Registro
    def actualizarregistro():
        editor = Tk()
        editor.title("MODIFICAR UN REGISTRO")
        editor.iconbitmap('icono.ico')
        editor.geometry("600x600")

        # Crear la Base de Datos o Conectarse a una
        conn: Connection = sqlite3.connect("Datos_Personal")

        # Crear el Cursor
        c: Cursor = conn.cursor()

        # obtener el valor buscado
        record_id = c_seleccionar.get()

        # Busqueda en la base de datos
        c.execute("SELECT * FROM DatosPersonal WHERE oid =" + record_id)
        records = c.fetchall()

        def guardarregistro():
            # Crear la Base de Datos o Conectarse a una
            conn: Connection = sqlite3.connect("Datos_Personal")

            # Crear el Cursor
            c: Cursor = conn.cursor()

            record_id = c_seleccionar.get()

            c.execute("""UPDATE DatosPersonal SET
                    ID=ID,
                    pnombre = :pnombre,
                    snombre = :snombre,
                    papellido = :papellido,
                    sapellido = :sapellido,
                    direccion = :direccion,
                    ciudad = :ciudad,
                    celular=:celular
                    WHERE oid =:oid""",
                      {"ID": c_id_editor.get(),
                       "pnombre": c_pnombre_editor.get(),
                       "snombre": c_snombre_editor.get(),
                       "papellido": c_papellido_editor.get(),
                       "sapellido": c_sapellido_editor.get(),
                       "direccion": c_direcion_editor.get(),
                       "ciudad": c_ciudad_editor.get(),
                       "celular": c_celular_editor.get(),
                       "oid": record_id

                       })

            # Commit Cambios
            conn.commit()

            # Cerrar Conexion
            conn.close()

            # Cerrar Ventana Editor
            editor.destroy()

            # Limpiar el cuadro de texto seleccionar
            c_seleccionar.delete(0, END)

        # Creando Label de Ingreso
        l_id = Label(editor, text="ID")
        l_pnombre = Label(editor, text="Primer Nombre")
        l_snombre = Label(editor, text="Segundo Nombre")
        l_papellido = Label(editor, text="Primer Apellido")
        l_sapellido = Label(editor, text="Segundo Apellido")
        l_direcion = Label(editor, text="Direccion")
        l_ciudad = Label(editor, text="Ciudad")
        l_celular = Label(editor, text="Numero Celular")

        # Creamos variables globales para los campos de ingreso
        global c_id_editor
        global c_pnombre_editor
        global c_snombre_editor
        global c_papellido_editor
        global c_sapellido_editor
        global c_direcion_editor
        global c_ciudad_editor
        global c_celular_editor

        # Creando Campos de Ingreso
        c_id_editor = Entry(editor, width=60, borderwidth=2)
        c_pnombre_editor = Entry(editor, width=60, borderwidth=2)
        c_snombre_editor = Entry(editor, width=60, borderwidth=2)
        c_papellido_editor = Entry(editor, width=60, borderwidth=2)
        c_sapellido_editor = Entry(editor, width=60, borderwidth=2)
        c_direcion_editor = Entry(editor, width=60, borderwidth=2)
        c_ciudad_editor = Entry(editor, width=60, borderwidth=2)
        c_celular_editor = Entry(editor, width=60, borderwidth=2)

        # Creando Botones
        botonguardar = Button(editor, text="Guardar",
                              padx=20, pady=10, command=guardarregistro)

        # Hacer un ciclo para los resultados
        for record in records:
            c_id_editor.insert(0, record[0])
            c_pnombre_editor.insert(0, record[1])
            c_snombre_editor.insert(0, record[2])
            c_papellido_editor.insert(0, record[3])
            c_sapellido_editor.insert(0, record[4])
            c_direcion_editor.insert(0, record[5])
            c_ciudad_editor.insert(0, record[6])
            c_celular_editor.insert(0, record[7])

        # Mostrando labels en pantalla inicial
        l_id.grid(row=0, column=0, padx=10, pady=10)
        l_pnombre.grid(row=1, column=0, padx=10, pady=10)
        l_snombre.grid(row=2, column=0, padx=10, pady=10)
        l_papellido.grid(row=3, column=0, padx=10, pady=10)
        l_sapellido.grid(row=4, column=0, padx=10, pady=10)
        l_direcion.grid(row=5, column=0, padx=10, pady=10)
        l_ciudad.grid(row=6, column=0, padx=10, pady=10)
        l_celular.grid(row=7, column=0, padx=10, pady=10)

        # Mostrando Campos de Ingreso en editor
        c_id_editor.grid(row=0, column=1, padx=10, pady=10)
        c_pnombre_editor.grid(row=1, column=1, padx=10, pady=10)
        c_snombre_editor.grid(row=2, column=1, padx=10, pady=10)
        c_papellido_editor.grid(row=3, column=1, padx=10, pady=10)
        c_sapellido_editor.grid(row=4, column=1, padx=10, pady=10)
        c_direcion_editor.grid(row=5, column=1, padx=10, pady=10)
        c_ciudad_editor.grid(row=6, column=1, padx=10, pady=10)
        c_celular_editor.grid(row=7, column=1, padx=10, pady=10)

        # Mostrando Botones en editor
        botonguardar.grid(row=8, column=0, padx=10, pady=10)

        # Commit Cambios
        conn.commit()

        # Cerrar Conexion
        conn.close()

    # Creando funcion Consultar un Registro
    def consultarregistro():
        # Crear la Base de Datos o Conectarse a una
        conn: Connection = sqlite3.connect("Datos_Personal")

        # Crear el Cursor
        c: Cursor = conn.cursor()

        # Seleccionar Datos de la Base de Datos
        c.execute("SELECT *, oid FROM DatosPersonal")
        records = c.fetchall()
        print(records)

        # Buscar los registros
        print_records = ""
        for record in records:
            print_records += str(record) + "\n"

        # Mostrar los regristros en pantalla
        l_query = Label(pantallainicial, text=print_records)
        l_query.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

        # Commit Cambios
        conn.commit()

        # Cerrar Conexion
        conn.close()

    # Creando Label de Ingreso
    l_id = Label(pantallainicial, text="ID")
    l_pnombre = Label(pantallainicial, text="Primer Nombre")
    l_snombre = Label(pantallainicial, text="Segundo Nombre")
    l_papellido = Label(pantallainicial, text="Primer Apellido")
    l_sapellido = Label(pantallainicial, text="Segundo Apellido")
    l_direcion = Label(pantallainicial, text="Direccion")
    l_ciudad = Label(pantallainicial, text="Ciudad")
    l_celular = Label(pantallainicial, text="Numero Celular")
    l_seleccionar = Label(pantallainicial, text="Inserte el ID")

    # Creando Campos de Ingreso
    c_id = Entry(pantallainicial, width=60, borderwidth=2)
    c_pnombre = Entry(pantallainicial, width=60, borderwidth=2)
    c_snombre = Entry(pantallainicial, width=60, borderwidth=2)
    c_papellido = Entry(pantallainicial, width=60, borderwidth=2)
    c_sapellido = Entry(pantallainicial, width=60, borderwidth=2)
    c_direcion = Entry(pantallainicial, width=60, borderwidth=2)
    c_ciudad = Entry(pantallainicial, width=60, borderwidth=2)
    c_celular = Entry(pantallainicial, width=60, borderwidth=2)
    c_seleccionar = Entry(pantallainicial, width=60, borderwidth=2)

    # Creando Botones
    botonanadir = Button(pantallainicial, text="Añadir",
                         padx=20, pady=10, command=anadirregistro)
    botonconsulta = Button(pantallainicial, text="Consultar",
                           padx=20, pady=10, command=consultarregistro)
    botonactualizar = Button(
        pantallainicial, text="Actualizar", padx=20, pady=10, command=actualizarregistro)
    botoneliminar = Button(pantallainicial, text="Eliminar",
                           padx=20, pady=10, command=eliminarregistro)
    botonlimpiar = Button(pantallainicial, text="Limpiar",
                          padx=20, pady=10, command=limpiar)
    botonsalir = Button(pantallainicial, text="Salir",
                        padx=20, pady=10, command=exit)

    # # Crear Scrollbar para el cuadro de texto
    # text_scroll = Scrollbar(pantallainicial)

    # # Creando lista de Botones
    # lista_botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0, botonborrar,
    #                  botonigual, botondivision, botonresta, botonsuma, botonmultiplicacion]
    #
    # # Definimos el contador numero de fila y columna
    # contador = 0
    #
    # # Ciclo en la lista de botones para configurar cada fila y columna
    # for button in lista_botones:
    #     Grid.rowconfigure(pantallainicial, contador, weight=1)
    #     Grid.columnconfigure(pantallainicial, contador, weight=1)
    #     # Incrementando el contador
    #     contador += 1
    #
    # def resize(e):
    #     size = e.width / 25
    #     # Configurar el tamaño del entry
    #     campo.config(font=("Helvetica", int(size)))
    #     # Ciclo en la lista de botones para configurar cada boton
    #     for button2 in lista_botones:
    #         button2.config(font=("Helvetica", int(size)))
    #
    # # Bind la aplicacion
    # pantallainicial.bind("<Configure>", resize)

    # Mostrando labels en pantalla inicial
    l_id.grid(row=0, column=0, padx=10, pady=10, sticky=E)
    l_pnombre.grid(row=1, column=0, padx=10, pady=10, sticky=E)
    l_snombre.grid(row=2, column=0, padx=10, pady=10, sticky=E)
    l_papellido.grid(row=3, column=0, padx=10, pady=10, sticky=E)
    l_sapellido.grid(row=4, column=0, padx=10, pady=10, sticky=E)
    l_direcion.grid(row=5, column=0, padx=10, pady=10, sticky=E)
    l_ciudad.grid(row=6, column=0, padx=10, pady=10, sticky=E)
    l_celular.grid(row=7, column=0, padx=10, pady=10, sticky=E)
    l_seleccionar.grid(row=11, column=0, padx=10, pady=10, sticky=E)

    # Mostrando Campos de Ingreso en pantalla inicial
    c_id.grid(row=0, column=1, padx=10, pady=10)
    c_pnombre.grid(row=1, column=1, padx=10, pady=10)
    c_snombre.grid(row=2, column=1, padx=10, pady=10)
    c_papellido.grid(row=3, column=1, padx=10, pady=10)
    c_sapellido.grid(row=4, column=1, padx=10, pady=10)
    c_direcion.grid(row=5, column=1, padx=10, pady=10)
    c_ciudad.grid(row=6, column=1, padx=10, pady=10)
    c_celular.grid(row=7, column=1, padx=10, pady=10)
    c_seleccionar.grid(row=11, column=1, padx=10, pady=10)

    # Mostrando Botones en pantalla inicial
    botonanadir.grid(row=8, column=0, padx=10, pady=10)
    botonconsulta.grid(row=8, column=1, padx=10, pady=10)
    botonactualizar.grid(row=12, column=0, padx=10, pady=10)
    botoneliminar.grid(row=12, column=1, padx=10, pady=10)
    botonlimpiar.grid(row=13, column=0, padx=10, pady=10)
    botonsalir.grid(row=13, column=1, padx=10, pady=10)

    # # Mostrando Barra de Scroll
    # text_scroll.grid(column=2, rowspand=13)


# Creando Label de Ingreso
l_willy = Label(splash, text="Master Willy Corzo \n 301 789 38 83",
                font=("Helvetica", 26), anchor=E)

# Mostrando labels en pantalla splash
l_willy.pack(fill=X, side=BOTTOM, ipady=10)

# temporizador de la pantalla Splash
splash.after(2000, pantallaprincipal)

mainloop()
