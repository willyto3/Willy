# BLACK DOG SOLUTION

Proyecto Pagina Personal Orlando Korzo

www.orlandokorzo.com

SECTION VARIABLES
Idioma Ingles
Estilo de Escritura camelCase

SECTION COMENTARIOS
Idioma Español

BACKEND

SECTION PROCEDIMIENTO

- Se crea la carpeta para guardar el backend ok-backend
- se inicia el proyecto utilizando el comando npm init
- se instala Nodemon
- Se incluye en el archivo package.json estas dos configuraciones en los scripts
  "dev": "nodemon index.js",
  "start": "node index.js"
- se instala Express
- se crea el archivo de las variables de entorno .env
- se instala dotenv
- se instala Morgan
- se instala Mongoose
- se crea la carpeta db en la raiz, se genera un archivo config.js en esa carpeta
- -se crea la configuracion de la base de datos en ese archivo
- se crea la carpeta models, en esta carpeta se van a generar los archivos con la configuracion de los modelos que se van a guardar en la base de datos.

SECTION DEPENDENCIAS

Dependencias de Desarrollo

- Nodemon
  npm install --save-dev nodemon
  funciones
  Es una herramiento que ayuda con el desarrollo en Node.js, reinicia automaticamente el servidor cuando se realizan cambios.

Dependencias

- Express
  npm install express --save
  funciones
  Express, es un framework para crear aplicaciones web, APIs y web services, que ha sido inspirado en la librería Sinatra de Ruby. Es software libre y de código abierto, con licencia MIT

- Dotenv
  npm install dotenv
  funciones
  Dotenv es un modulo que carga las variables de ambiente desde un archivo .env hacia el process.env. Guardando las configuraciones, separadas del codigo del proyecto.

- Morgan
  npm install morgan
  funciones
  Morgan es un modulo que muestra las peticiones HTTP en la consola.
  Ejemplo morgan(':method :url :status :res[content-length] - :response-time ms')

- Mongoose
  npm install mongoose
  funciones
  Mongoose es una herramienta diseñada para modelar objetos en MongoDB, puede trabajar en ambientes asincronicos. Mongoose soporta promesas (promises) y llamadas (callbacks).
