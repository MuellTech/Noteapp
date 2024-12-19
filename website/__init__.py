from flask import Flask
import os
from dotenv import load_dotenv
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
  load_dotenv()
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
  db.init_app(app)
  
  from website.auth import auth_bp
  from website.home import home_bp
  app.register_blueprint(auth_bp)
  app.register_blueprint(home_bp)

  from website.models import User, Note

  with app.app_context():
    db.create_all()

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  return app
