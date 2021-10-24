from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import *
from models import *

# Creacion de las Paginas

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crearregistro', methods=['POST'])
def create():

    if request.form['password_hash'] == request.form['password_hash2']:
        try:       
            pw_hash= generate_password_hash(request.form['password_hash'], "sha256")
            persona = Personas(nombre=request.form['nombre'], apellido = request.form['apellido'],
                        direccion=request.form['direccion'], celular=request.form['celular'],
                        email=request.form['email'], fechanacimiento=request.form['fechanacimiento'],
                        password_hash=pw_hash)
            db.session.add(persona)
            db.session.commit()
            flash('Registro creado exitosamente')
            return render_template('registro.html')

        except Exception as e:
            flash("No se realizo el registro del Usuario")
            return render_template('registro.html')
    else:
        flash("Las Contraseñas deben ser iguales")
        return render_template('registro.html')


@app.route('/ingresar', methods=['POST'])
def ingreso():

    try:
        persona = Personas.query.filter_by(celular=request.form['celular']).first()
        if persona and check_password_hash(persona.password_hash, request.form['contrasena']):
            return render_template('perfil.html')
        else:
            flash('Usuario o Contraseña incorrectos')
            return render_template('login.html')
    except Exception as e:
        flash('Usuario o Contraseña incorrectos')
        return render_template('login.html')

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