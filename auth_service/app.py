from routes import auth_bp
from flask import Flask
from dotenv import load_dotenv
import os

from extensions import db, bcrypt, jwt  # ✅ cambia esto

load_dotenv()

app = Flask(__name__)

# Configuración
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

# Inicializar extensiones
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Importar rutas dentro del bloque de ejecución
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
