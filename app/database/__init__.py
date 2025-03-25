from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()  # Define migrate globally

def init_db(app):
    """Initialize database and migration with the Flask app."""
    db.init_app(app)
    migrate.init_app(app, db)  # Attach Flask-Migrate to app
    with app.app_context():
        db.configure_mappers()