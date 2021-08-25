# Importaciones
# Importar modulo para poder hacer la parte gráfica
from tkinter import *
# importar modulo para hacer el tree view
from tkinter import ttk
# Importar modulo para manejar imagenes
from PIL import Image
from PIL import ImageTk
# Importar modulo de la conexion
from conexion import conexion_datos
from conexion import generarusuario


# Creando la pantalla Splash
splash = Tk()

# Esconder la barra de titulo en la pantalla Splash
splash.overrideredirect(True)

# Asignamos el alto y el ancho de nuestra pantalla Splash
anchoapp = 620
altoapp = 620

# Obtenemos el ancho y el alto de la pantalla del computador
anchopantalla = splash.winfo_screenwidth()
altopantalla = splash.winfo_screenheight()

# Obtenemos las coordenadas del centro de la pantalla
x = (anchopantalla / 2) - (anchoapp / 2)
y = (altopantalla / 2) - (altoapp / 2)

# Centramos la pantalla Splash en la pantalla del computador
splash.geometry(f"{anchoapp}x{altoapp}+{int(x)}+{int(y)}")

# Creamos la funcion ventana inicial Que inicia nuestro CRUD
def ventanainicial():
  # Destruimos la pantalla Splash
  splash.destroy()
  # Inicializamos la ventana inicial
  ventanainicial = Tk()
  ventanainicial.title("BASE DE DATOS GAMER MARKET COLOMBIA")
  ventanainicial.iconbitmap('IcoGMC.ico')
  ventanainicial.geometry("600x600")

  # Llamamos la funcion para conectar a la base de datos MYSQL
  conexion_datos()


# Funcion para añadir un usuario en la base de datos MYSQL
  def ingresar():

    comandoSQL ="INSERT INTO Personas(cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido ) VALUES (%s,%s,%s,%s,%s)"
    valores = (txtcedula.get(), txtprimer_nombre.get(), txtsegundo_nombre.get(),txtprimer_apellido.get(),txtsegundo_apellido.get())
    
    generarusuario(comandoSQL, valores)
    
    # Limpiar Campos de la ventana inicial
    limpiar()
    pass


  # Funcion para limpiar los cuadros de texto en la ventana inicial
  def limpiar():
    txtcedula.delete(0, END)
    txtprimer_nombre.delete(0, END)
    txtsegundo_nombre.delete(0, END)
    txtprimer_apellido.delete(0, END)
    txtsegundo_apellido.delete(0, END)
    print("Se limpio")
    

  # CREAR PARTE GRAFICA

  # Crear frames para la aplicacion
  # En el Frame 1 se va a colocar el nombre de la aplicacion y en el frame 2 los labels y cuadro de texto

  frame1 = Frame(ventanainicial)
  frame1.pack(expand=True, fill = BOTH)
  frame2 = Frame(ventanainicial, bg = "red")
  frame2.pack(expand=True, fill = BOTH, pady=10)

  # Iniciamos los objetos que van en la ventana inicial y los colocamos en pantalla
  titulo = Label(frame1, text="Gamer Marker Colombia - Base de Datos Clientes", padx=10)
  titulo.grid(row = 0, column = 0, columnspan=2)

  # Creamos los labels que van en la pantalla inicial
  lblcedula = Label(frame1, text="Cedula")
  lblprimer_nombre = Label(frame1, text="Primer Nombre")
  lblsegundo_nombre = Label(frame1, text="Segundo Nombre")
  lblprimer_apellido = Label(frame1, text="Primer Apellido")
  lblsegundo_apellido = Label(frame1, text="Segundo Apellido")

  # Creamos los cuadros de texto que van en la pantalla inicial
  txtcedula = Entry(frame1)
  txtprimer_nombre = Entry(frame1)
  txtsegundo_nombre = Entry(frame1)
  txtprimer_apellido = Entry(frame1)
  txtsegundo_apellido = Entry(frame1)

  # Creamos los Botones que van en la pantalla inicial
  btningresar = Button(frame1, text= "INGRESAR", command=ingresar)
  btnlimpiar = Button(frame1, text= "LIMPIAR", command=limpiar)

  # Mostramos los elementos en la pantalla inicial
  lblcedula.grid(row = 1, column =0, sticky=W, padx=10)
  lblprimer_nombre.grid(row = 2, column =0, sticky=W, padx=10)
  lblsegundo_nombre.grid(row = 3, column =0, sticky=W, padx=10)
  lblprimer_apellido.grid(row = 4, column =0, sticky=W, padx=10)
  lblsegundo_apellido.grid(row = 5, column =0, sticky=W, padx=10)

  txtcedula .grid(row = 1, column =1)
  txtprimer_nombre .grid(row = 2, column =1)
  txtsegundo_nombre .grid(row = 3, column =1)
  txtprimer_apellido .grid(row = 4, column =1)
  txtsegundo_apellido .grid(row = 5, column =1)

  btningresar.grid(row =10, column = 0, pady=10)
  btnlimpiar.grid(row =10, column = 1, pady=10)

  # TREE VIEW
  # Hacemos el Estilo
  estilo = ttk.Style()
  # Elegimos un tema
  estilo.theme_use("default")
  # Configuramos el Tree View
  estilo.configure("Treeview",
      background ="#D3D3D3",
      foreground="black",
      rowheight=25,
      fieldbackground="#D3D3D3")

  # Cambiar color al seleccionar
  estilo.map("Treeview", background=[('selected', "#347083")])

  # Creamos un scrollbar en el tree View
  tree_scroll = Scrollbar(frame2)
  tree_scroll.pack(side=RIGHT, fill=Y)

  # Creamos el Tree View
  mitreeview=ttk.Treeview(frame2,yscrollcommand=tree_scroll.set, selectmode='extended')
  mitreeview.pack()

  # Configuramos el Scroll Bar
  tree_scroll.config(command=mitreeview.yview)

  # Definimos las columnas
  mitreeview['columns']=('Cedula','Primer Nombre', 'Segundo Nombre', 'Primer Apellido', 'Segundo Apellido')

  # Formato a las columnast
  # Ocultamos la columna cero del treeview
  mitreeview.column('#0',width=0,stretch=NO)
  mitreeview.column('Cedula',anchor=W,width=100)
  mitreeview.column('Primer Nombre',anchor=W,width=100)
  mitreeview.column('Segundo Nombre',anchor=W,width=100)
  mitreeview.column('Primer Apellido',anchor=W,width=100)
  mitreeview.column('Segundo Apellido',anchor=W,width=100)

  # Creamos la cabecera
  mitreeview.heading('#0',text='',anchor=CENTER)
  mitreeview.heading('Cedula',text='Cedula',anchor=CENTER)
  mitreeview.heading('Primer Nombre',text='Primer Nombre',anchor=CENTER)
  mitreeview.heading('Segundo Nombre',text='Segundo Nombre',anchor=CENTER)
  mitreeview.heading('Primer Apellido',text='Primer Apellido',anchor=CENTER)
  mitreeview.heading('Segundo Apellido',text='Segundo Apellido',anchor=CENTER)
  
  # Configuramos los colores de fila
  mitreeview.tag_configure('oddrow', background='white')
  mitreeview.tag_configure('evenrow', background='lightblue')







# Colocar la imagen de Gamer Market Colombia en la pantalla splash
miimagen = ImageTk.PhotoImage(Image.open("GamerMarketCol.jpg"))
lblimagen = Label(image =miimagen)
lblimagen.pack()
# temporizador de la pantalla Splash
splash.after(2000, ventanainicial)

mainloop()
