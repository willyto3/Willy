from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
from flask.wrappers import Request
from werkzeug.utils import redirect
from models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Es un Secreto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database\Prueba.db'
db.init_app(app)


# Creacion de las Paginas

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crearregistro', methods=['POST'])
def create():

    try:       
        
        persona = Personas(nombre=request.form['nombre'], apellido = request.form['apellido'],
                    direccion=request.form['direccion'], celular=request.form['celular'],
                    email=request.form['email'], fechanacimiento=request.form['fechanacimiento'],
                    contrasena=request.form['contrasena'], vercontrasena=request.form['vercontrasena'])
        db.session.add(persona)
        db.session.commit()
        flash('Registro creado exitosamente')
        return render_template('registro.html')

    except Exception as e:
        flash("No se realizo el registro del Usuario")
        return render_template('registro.html')


@app.route('/Login')
def login():
    return render_template('login.html')


@app.route('/Registro')
def registro():
    return render_template('registro.html')


@app.route('/Busqueda')
def busqueda():
    return render_template('busqueda.html')


@app.route('/Menu')
def menu():
    return render_template('menu.html')


@app.route('/Perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/Carrito')
def carrito():
    return render_template('carrito.html')


@app.route('/Dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/Comentarios')
def comentarios():
    return render_template('comentarios.html')


@app.route('/Usuarios')
def usuarios():
    return render_template('usuarios.html')


def pagina_no_encontrada(error):
    return redirect(url_for('index'))

def error_de_servidor(error):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(500, error_de_servidor)
    app.run(debug=True, port=5000)
