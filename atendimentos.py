from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
import datetime

atendimentos_bp = Blueprint("atendimentos", __name__)

@atendimentos_bp.route('/atendimentos', methods=['POST'])
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

        cursor.execute("Insert into Atendimentos (cliente, entidade, municipio, obs, dt_atendimento, usuario) values (?,?,?,?,?,?)", 
                       (cliente, entidade, municipio, observacoes, data_registro, usuario))

        conn.commit()
        conn.close()

        return redirect(url_for("atendimentos.atendimentos"))
