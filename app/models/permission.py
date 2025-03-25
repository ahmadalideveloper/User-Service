from app.database import db
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))

    # Define relationship with roles
    # roles = relationship("Role", secondary="role_permissions", back_populates="permissions")


    def __repr__(self):
        return f"<Permission {self.name}>"
