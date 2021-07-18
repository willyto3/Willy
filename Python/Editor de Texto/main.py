from tkinter import *
from tkinter import filedialog
from tkinter import font

# Crear Pantalla principal

pantallaprincipal = Tk()
pantallaprincipal.geometry("1200x660")

# Crear Frame principal
frameprincipal = Frame(pantallaprincipal)
frameprincipal.pack(pady=5)

# VARIABLES GLOBALES
# Estado de Apertura
global estadodeapertura
estadodeapertura = False
# Estado de Elegido
global elegido
elegido = False


# FUNCIONES
# Funcion Nuevo
def nuevo():
    cuadrotexto.delete("1.0", END)
    pantallaprincipal.title("Archivo Nuevo")
    barradeestado.config(text="Archivo Nuevo        ")
    global estadodeapertura
    estadodeapertura = False


# Funcion Abir
def abrir():
    cuadrotexto.delete("1.0", END)
    # Obtener nombre de Archivo
    nombrearchivo = filedialog.askopenfilename(title="Abrir Archivo", filetypes=(
        ("Text Files", "*.txt"), ("HTML files", "*.html"), ("Python Files", "*.py")))
    if nombrearchivo:
        global estadodeapertura
        estadodeapertura = nombrearchivo

    name = nombrearchivo

    barradeestado.config(text=name + "        ")
    pantallaprincipal.title(name)
    # Abrir el Archivo
    nombrearchivo = open(nombrearchivo, "r")
    stuff = nombrearchivo.read()
    # Añadir los archivos al cuadro de texto
    cuadrotexto.insert(END, stuff)
    # Cerrar el archivo abierto
    nombrearchivo.close()


# Funcion guardar Como
def guardarcomo():
    nombrearchivo = filedialog.asksaveasfilename(defaultextension=".*", title="Guardar Como", filetypes=(
        ("Text Files", "*.txt"), ("HTML files", "*.html"), ("Python Files", "*.py")))
    if nombrearchivo:
        name = nombrearchivo
        barradeestado.config(text=f"Guardado como {name}        ")
        pantallaprincipal.title(f"{name}")
        # Guardar el Archivo
        nombrearchivo = open(nombrearchivo, "w")
        nombrearchivo.write(cuadrotexto.get(1.0, END))
        global estadodeapertura
        estadodeapertura = nombrearchivo
        nombrearchivo.close()


# Funcion Guardar
def guardar():
    global estadodeapertura
    if estadodeapertura:
        # Guardar el Archivo
        nombrearchivo = open(estadodeapertura, "w")
        nombrearchivo.write(cuadrotexto.get(1.0, END))
        nombrearchivo.close()
        barradeestado.config(text="Guardado        ")
    else:
        guardarcomo()


# Funcion Cortar
def cortar(e):
    global elegido
    # Verificar si se usaron los atajos del teclado
    if e:
        elegido = pantallaprincipal.clipboard_get()
    else:
        if cuadrotexto.selection_get():
            # Agarra el texto seleccionado del cuadro de texto
            elegido = cuadrotexto.selection_get()
            # Borra el texto seleccionado del cuadro de texto
            cuadrotexto.delete("sel.first", "sel.last")
            pantallaprincipal.clipboard_clear()
            pantallaprincipal.clipboard_append(elegido)


# Funcion Copiar
def copiar(e):
    global elegido
    # Verificar si se usaron los atajos del teclado
    if e:
        elegido = pantallaprincipal.clipboard_get()

    if cuadrotexto.selection_get():
        # Agarra el texto seleccionado del cuadro de texto
        elegido = cuadrotexto.selection_get()
        pantallaprincipal.clipboard_clear()
        pantallaprincipal.clipboard_append(elegido)


# Funcion Pegar
def pegar(e):
    global elegido
    # Verificar si se usaron los atajos del teclado
    if e:
        elegido = pantallaprincipal.clipboard_get()
    else:
        if elegido:
            position = cuadrotexto.index(INSERT)
            cuadrotexto.insert(position, elegido)


# Crear Scrollbar Y para el cuadro de texto
text_scroll = Scrollbar(frameprincipal)
text_scroll.pack(side=RIGHT, fill=Y)

# Crear Scrollbar X para el cuadro de texto
text_scroll2 = Scrollbar(frameprincipal, orient="horizontal")
text_scroll2.pack(side=BOTTOM, fill=X)

# Crear cuadro de texto
cuadrotexto = Text(frameprincipal, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=text_scroll2.set)
cuadrotexto.pack()

# Configurar el Scrollbar
text_scroll.config(command=cuadrotexto.yview)

# Crear Menu
mimenu = Menu(pantallaprincipal)
pantallaprincipal.config(menu=mimenu)

# Añadir menu Archivo
menu_archivo = Menu(mimenu, tearoff=False)
mimenu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_command(label="Guardar como", command=guardarcomo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=exit)

# Añadir menu Edicion
menu_edicion = Menu(mimenu, tearoff=False)
mimenu.add_cascade(label="Editar", menu=menu_edicion)
menu_edicion.add_command(label="Cortar", command=lambda: cortar(False), accelerator="Control + X")
menu_edicion.add_command(label="Copiar", command=lambda: copiar(False), accelerator="Control + C")
menu_edicion.add_command(label="Pegar", command=lambda: pegar(False), accelerator="Control + V")
menu_edicion.add_separator()
menu_edicion.add_command(label="Atras", command=cuadrotexto.edit_undo, accelerator="Control + Z")
menu_edicion.add_command(label="Adelante", command=cuadrotexto.edit_redo, accelerator="Control + Y")

# Añadir barra de estado al final de la App
barradeestado = Label(pantallaprincipal, text="Listo        ", anchor=E)
barradeestado.pack(fill=X, side=BOTTOM, ipady=5)

# Editar Binding
pantallaprincipal.bind("<Control-Key-x>", cortar)
pantallaprincipal.bind("<Control-Key-c>", copiar)
pantallaprincipal.bind("<Control-Key-v>", pegar)

pantallaprincipal.mainloop()
