from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# Modelo para la base de datos Prueba tabla 'Persona'
class Personas(db.Model):
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




