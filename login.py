from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
import criptografia as cript
import datetime

login_bp = Blueprint("login", __name__)

@login_bp.route('/')
def index():
    return render_template("login.html")

@login_bp.route('/login', methods=['GET','POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    conn = sqlite3.connect("D:\Programação\Atendix\database\saturndb")
    cursor = conn.cursor()
    salt = cursor.execute("SELECT salt FROM USUARIOS WHERE USUARIO = ?", (usuario,)).fetchone()[0]
    data_atual = datetime.datetime.now()
    hash = cript.valida_hash(senha=senha, salt=salt)

    login = cursor.execute("SELECT * FROM USUARIOS WHERE USUARIO = ? AND SENHA = ? AND HASH = ? AND STATUS = 'A'", (usuario, senha, hash)).fetchone()

    if login:
        cursor.execute("update usuarios set ult_acesso = ? where usuario = ?", (data_atual, login[1]))
        conn.close()
        return redirect(url_for("main.main"))
    else:
        return render_template("login.html", error="Usuário ou senha inválida")
