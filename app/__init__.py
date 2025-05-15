from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.auth_routes import auth_bp
    from app.routes.obligation_routes import obligation_bp
    from app.routes.upload_routes import upload_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(obligation_bp)
    app.register_blueprint(upload_bp)

    return app
