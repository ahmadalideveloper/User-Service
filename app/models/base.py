from datetime import datetime
from app.database import db
from sqlalchemy import DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declared_attr

class BaseModel(db.Model):
    __abstract__ = True  # This tells SQLAlchemy that this is a base class, not a table.

    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, onupdate=datetime.utcnow)
    is_removed = db.Column(Boolean, default=False)

    @declared_attr
    def created_by(cls):
        return db.Column(db.Integer, ForeignKey("users.id"), nullable=True)

    @declared_attr
    def updated_by(cls):
        return db.Column(db.Integer, ForeignKey("users.id"), nullable=True)

    @declared_attr
    def removed_by(cls):
        return db.Column(db.Integer, ForeignKey("users.id"), nullable=True)
