from flask import Flask
app = Flask(__name__, template_folder='templates')

# Rotas dos outros módulos
from login import login_bp
from main import main_bp

# Registrar os blueprints (rotas) no app
app.register_blueprint(login_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=879)