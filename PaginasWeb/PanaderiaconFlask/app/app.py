from flask import Flask, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)


# Paginas

@app.route('/')
def index():
    return render_template('index.html')


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


def pagina_no_encontrada(error):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
