from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
import datetime

atendimentos_bp = Blueprint("atendimentos", __name__)

@atendimentos_bp.route('/')
def fecha():
    return render_template("main.html")

@atendimentos_bp.route('/atendimentos', methods=['POST','GET'])
def registra_atendimento():
    if request.method == 'POST' and 'usuario' in session:
        cliente = request.form.get('cliente')
        entidade = request.form.get('entidade')
        municipio = request.form.get('cidade')
        observacoes = request.form.get('observacoes')

        usuario = session['usuario']

        conn = sqlite3.connect("./database/saturndb")
        cursor = conn.cursor()
        data_registro = datetime.datetime.now()

        ultimo_atendimento = cursor.execute(f"select * from atendimentos where usuario = '{usuario}' order by atendimento_id desc limit 1").fetchone()

        if ultimo_atendimento:
            if (
                ultimo_atendimento[1] == cliente and
                ultimo_atendimento[2] == entidade and
                ultimo_atendimento[3] == municipio and
                ultimo_atendimento[4] == observacoes
            ):
                conn.close()
                mensagem = "O novo atendimento é idêntico ao último. Não foi registrado."
                return render_template("atendimento.html", msg_erro=mensagem)

        try:
            cursor.execute("Insert into Atendimentos (cliente, entidade, municipio, obs, dt_atendimento, usuario) values (?,?,?,?,?,?)", 
                        (cliente, entidade, municipio, observacoes, data_registro, usuario))
            conn.commit()
            conn.close()
            mensagem = "Atendimento Registrado!"
            return render_template("atendimento.html", msg_sucesso=mensagem)
        except:
            mensagem = "Erro ao Salvar Atendimento!"
            conn.close()
            return render_template("atendimento.html", msg_erro=mensagem)
    elif request.method == 'GET':
        return render_template("atendimento.html")
    else:
        return render_template("atendimento.html")