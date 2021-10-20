import sqlite3
from sqlite3 import Error
from flask import g

def get_conex():
    try:
        if "conex" not in g:
            g.conex = sqlite3.connect("datosclientes.db")
            return g.conex
    except Error:
        print(Error)

def close_conex():
    conex = g.pop("conex", None)
    if conex is not None:
        conex.close()