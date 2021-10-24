# import flask and sqlaclhemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app configuration
app.config["SECRET_KEY"] = 'Es un Secreto'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database\panaderia.db'
db = SQLAlchemy(app)


if __name__ == '__main__':    
    app.run(debug=True, port=5000)
    