from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
import datetime
import criptografia as cript

register_bp = Blueprint("register", __name__)

@register_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if 'usuario' in request.form:
            usuario = request.form.get('usuario').lower()
        else:
            usuario = None  # Defina para None ou outro valor padrão, dependendo da sua lógica
        senha = request.form.get('senha')
        data_atual = datetime.datetime.now()
        hash, salt = cript.gera_hash(senha)

        conn = sqlite3.connect("./database/saturndb")
        cursor = conn.cursor()
        

        cursor.execute("""insert into usuarios (usuario, senha, nome_completo, 
                          status, ult_acesso, salt, hash)
                          values (?,?,?,'A',?,?,?)""",(usuario,senha,nome,data_atual,salt,hash))
        conn.commit()
        conn.close()

        return redirect(url_for("login.index"))
    return render_template("register.html")