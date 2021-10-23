from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo para la base de datos Prueba tabla 'Persona'


class Personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=True)
    apellido = db.Column(db.String(200), nullable=True)
    direccion = db.Column(db.String(200))
    celular = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(200), nullable=True)
    fechanacimiento = db.Column(db.String(200))
    contrasena = db.Column(db.String(200), nullable=True)
    vercontrasena = db.Column(db.String(200), nullable=True)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=True)
    apellido = db.Column(db.String(200), nullable=True)
    direccion = db.Column(db.String(200))
    celular = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(200), nullable=True)
    fechanacimiento = db.Column(db.String(200))
    contrasena = db.Column(db.String(200), nullable=True)
    vercontrasena = db.Column(db.String(200), nullable=True)
    tipo = db.Column(db.String(200), nullable=True)