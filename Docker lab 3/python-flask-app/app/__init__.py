from flask import Flask
from flask_migrate import Migrate  # Импортируем Flask-Migrate
from app.extensions import db
from app.routes import main

def create_app():
    app = Flask(__name__)
    
    # Загружаем конфигурацию из окружения
    app.config.from_prefixed_env()
    
    # Инициализируем базу данных
    db.init_app(app)
    
    # Инициализация Flask-Migrate
    migrate = Migrate(app, db)  # Инициализируем Flask-Migrate с приложением и базой данных

    # Регистрируем blueprint для маршрутов
    app.register_blueprint(main)

    return app