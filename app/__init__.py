from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    mail.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from app.api import bp as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    from app import views, models

    return app