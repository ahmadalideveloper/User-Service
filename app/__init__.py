from flask import Flask
from app.config import Config
from dotenv import load_dotenv
from app.database import db, migrate, init_db  # Import migrate and init_db

# Load environment variables
load_dotenv()

def create_app():
    """Flask application factory function."""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize database
    init_db(app)  # Initialize database and migrations

    # Import models here to ensure they are registered with SQLAlchemy
    from app.models.user import User
    from app.models.role import Role
    from app.models.permission import Permission
    # from app.models.associations import user_roles, role_permissions


    # Register Blueprints (We will create these later)
    from app.routes.user_routes import user_bp
    # from app.routes.role_routes import role_bp

    app.register_blueprint(user_bp, url_prefix="/api/users")
    # app.register_blueprint(role_bp, url_prefix="/api/roles")

    return app
