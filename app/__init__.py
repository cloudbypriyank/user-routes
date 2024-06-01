from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_mail import Mail
from flask_jwt_extended import JWTManager
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('app.config.Config')
    # app.config['JWT_SECRET_KEY'] = 'voicebot_secretKey'
    app.config['MAIL_SERVER']= 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'team@contactswing.com'
    app.config['MAIL_PASSWORD'] = 'abxn ldxu jmst ugwa'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False


    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    # Import and register blueprints inside the create_app function
    from .controllers.users_controller import user_bp
    # from .controllers.posts_controller import post_bp
    # from .controllers.profiles_controller import profiles_bp

    app.register_blueprint(user_bp)
    # app.register_blueprint(post_bp)
    with app.app_context():
        db.create_all()

    return app

# Import models here to avoid circular imports
from app.models import *