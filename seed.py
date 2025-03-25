import click
from flask import Flask
from app.database import db
from app.models.role import Role
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.config import Config  # Import the existing Config class

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load configurations from Config.py

db.init_app(app)

# Define Roles
DEFAULT_ROLES = [
    "Admin",
    "Care Coordinator",
    "Nurse",
    "Doctor",
]


@click.command()
@click.option('--reset', is_flag=True, help="Reset the database before seeding")
def seed(reset):
    """Seed the database with initial roles and a default admin user."""
    with app.app_context():
        if reset:
            click.confirm("Are you sure you want to reset the database?", abort=True)
            db.drop_all()
            db.create_all()
            click.echo("Database reset completed.")

        # Insert Roles
        for role_name in DEFAULT_ROLES:
            role = Role.query.filter_by(name=role_name).first()
            if not role:
                db.session.add(Role(name=role_name))

        db.session.commit()
        click.echo("Roles seeded successfully.")

        # Insert Default Admin User
        admin_role = Role.query.filter_by(name="Admin").first()
        if admin_role:
            admin_user = User.query.filter_by(email="admin@example.com").first()
            if not admin_user:
                hashed_password = generate_password_hash("Admin@123", method="pbkdf2:sha256")
                new_admin = User(
                    username="Admin User",
                    email="admin@example.com",
                    password_hash=hashed_password,
                    role_id=admin_role.id
                )
                db.session.add(new_admin)
                db.session.commit()
                click.echo("Admin user created successfully.")
            else:
                click.echo("Admin user already exists.")
        else:
            click.echo("Admin role not found, skipping user creation.")


if __name__ == "__main__":
    seed()
