# ORLANDO KORZO

Proyecto Pagina Personal Orlando Korzo
www.orlandokorzo.com
BLACK DOG SOLUTION

SECTION VARIABLES
Idioma Ingles
Estilo de Escritura camelCase

SECTION COMENTARIOS
Idioma Español

SECTION FRAMEWORK
Bootstrap

NOTE FRONTEND

SECTION PROCEDIMIENTO

- Se crea la carpeta para guardar el frontend ok-frontend
- se inicia el proyecto utilizando el comando ng -- new ok-frontend
- se prueba la pagina utilizando el siguiente codigo ng -- serve -o
- Instalamos Bootstrap como Framework de diseño. usando este codigo npm i bootstrap@5.2.0-beta1

-

NOTE BACKEND

SECTION PROCEDIMIENTO

- Se crea la carpeta para guardar el backend ok-backend
- se inicia el proyecto utilizando el comando npm init
- se instala Nodemon
- Se incluye en el archivo package.json estas dos configuraciones en los scripts
  "dev": "nodemon index.js",
  "start": "node index.js"
- se instala Express
- se instala Morgan
- se instala Mongoose
- Se instala Corse
- Se instala Express-Validator
- Se instala Bcryptjs
- Se instala Json Web Token
- se crea el archivo de las variables de entorno .env
- se instala dotenv
- se crea la carpeta db en la raiz, se genera un archivo config.js en esa carpeta
- -se crea la configuracion de la base de datos en ese archivo
- se crea la carpeta models, en esta carpeta se van a generar los archivos con la configuracion de los modelos que se van a guardar en la base de datos.
- se crea la carpeta controllers, en esta carpeta se van a guardar los controladores de la base de datos.
- Se crea la carpeta middleware, en esta carpeta van los servicios que vamos a utilizar.
- Se crea la carpeta routes, en esta carpeta se van a guardar las rutas del api.
- Se genera el modelo para el usuario. Por el momento se va a guardar esta informacion (Nombre, Username, Password y imagen)

- SECTION DEPENDENCIAS

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

- Cors
  npm install cors
  explicacion
  Control de acceso HTTP (CORS)
  El Intercambio de Recursos de Origen Cruzado (CORS (en-US)) es un mecanismo que utiliza cabeceras HTTP adicionales para permitir que un user agent (en-US) obtenga permiso para acceder a recursos seleccionados desde un servidor, en un origen distinto (dominio) al que pertenece. Un agente crea una petición HTTP de origen cruzado cuando solicita un recurso desde un dominio distinto, un protocolo o un puerto diferente al del documento que lo generó.
  funciones
  Cors es una herramienta diseñada para proveer el intercambio de recursos en express

- Express-Validator
  npm install express-validator
  funciones
  Express-Validator es una herramienta diseñada para validar y sanitizar funciones.

- Bcryptjs
  npm install bcryptjs
  funciones
  Bcryptjs es una herramienta diseñada para encriptar contraseñas.

- JSON Web Token
  npm install jsonwebtoken
  funciones
  JSON Web Token es una herramienta diseñada para guardar el token del usuario.
