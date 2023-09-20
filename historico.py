from flask import Blueprint, render_template, request, session
import sqlite3
from datetime import datetime

historico_bp = Blueprint("historico",__name__)

@historico_bp.route('/')
def fechar():
    return render_template('main.html')

@historico_bp.route('/historico', methods=['GET', 'POST'])
def historico():
    if request.method == 'POST':
        data_inicial_str = request.form.get('dataInicial')
        data_final_str = request.form.get('dataFinal')

        data_inicial = datetime.fromisoformat(data_inicial_str).strftime('%Y-%m-%d %H:%M:%S.%f')
        data_final = datetime.fromisoformat(data_final_str).strftime('%Y-%m-%d %H:%M:%S.%f')

        usuarioLogado = session['usuario']

        conn = sqlite3.connect("./database/saturndb")
        cursor = conn.cursor()
        
        atendimentos = cursor.execute('select * from atendimentos where usuario = ? and dt_atendimento >= ? and dt_atendimento <= ?', (usuarioLogado, data_inicial, data_final)).fetchall()
        if atendimentos:
            return render_template('historico.html', atendimentos=atendimentos)
        else:
            return render_template('historico.html')
    else:
        return render_template('historico.html')