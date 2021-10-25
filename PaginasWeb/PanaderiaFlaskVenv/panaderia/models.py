from panaderia import db
from werkzeug.security import generate_password_hash, check_password_hash

# MODELOS

# Modelo para la base de datos Prueba tabla 'Persona'


class Personas(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=True)
    apellido = db.Column(db.String(200), nullable=True)
    direccion = db.Column(db.String(200))
    celular = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(200), nullable=True)
    fechanacimiento = db.Column(db.String(200))

    # Genera un hash de la contraseña
    password_hash = db.Column(db.String(200), nullable=True)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Modelo para la base de datos Prueba tabla 'Productos'


class Productos(db.Model):
    idproducto = db.Column(db.Integer, primary_key=True)
    nombreproducto = db.Column(db.String(50), nullable=True)
    precioproducto = db.Column(db.Double, nullable=True)
    descripcionproducto = db.Column(db.String(200))


class Factura(db.Model):
    idfactura = db.Column(db.Integer, primary_key=True)
    fechafactura = db.Column(db.datetime, nullable=True)


class Rol(db.Model):
    idrol = db.Column(db.Integer, primary_key=True)
