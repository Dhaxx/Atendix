from flask import Flask, session
from flask_session import Session
import secrets
app = Flask(__name__, template_folder='templates')

# Rotas dos outros módulos
from login import login_bp
from main import main_bp
from register import register_bp
from atendimentos import atendimentos_bp
from historico import historico_bp

# Configurar Flask-Session
chave_secreta = secrets.token_hex(32)
app.config['SESSION_TYPE'] = 'filesystem' # Armazenamento em cookies
app.config['SECRET_KEY'] = chave_secreta
Session(app)

# Registrar os blueprints (rotas) no app
app.register_blueprint(login_bp)
app.register_blueprint(main_bp)
app.register_blueprint(register_bp)
app.register_blueprint(atendimentos_bp)
app.register_blueprint(historico_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=879)