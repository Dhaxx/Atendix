from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

login_bp = Blueprint("login", __name__)

@login_bp.route('/')
def index():
    return render_template("login.html")

@login_bp.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    conn = sqlite3.connect("F:\\Kaio\\PROGRAMAÇÃO\\Atendimentos\\database\\saturndb")
    cursor = conn.cursor()

    login = cursor.execute("SELECT * FROM Usuarios WHERE USUARIO = ? AND SENHA = ? AND STATUS = 'A'", (usuario, senha)).fetchone()

    conn.close()

    if login:
        return redirect(url_for("main.main"))
    else:
        return render_template("login.html", error="Usuário ou senha inválida")
