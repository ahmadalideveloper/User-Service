from marshmallow import ValidationError
from app.models.user import User
from app.models.role import Role
from app.database import db
from app.utils.response_helper import success_response, error_response
from app.utils.message_enum import MessageEnum
from app.schemas.user_schema import UserSchema

class UserService:
    """Handles all user-related operations"""

    @staticmethod
    def create_user(data):
        """Create a new user"""
        try:
            validated_data = UserSchema.load(data)
        except ValidationError as err:
            return error_response("Failed to create user", str(err.messages))

        try:
            user = User(
                name=data["name"],
                email=data["email"],
                password_hash=data["password"],  # TODO: Hash password before storing
                role_id=data.get("role_id")  # Assign role if provided
            )
            db.session.add(user)
            db.session.commit()
            return success_response(MessageEnum.USER_CREATED, user.to_dict())
        except Exception as e:
            return error_response(MessageEnum.USER_CREATION_FAILED, str(e))

    @staticmethod
    def get_users():
        """Retrieve all users"""
        users = User.query.all()
        return success_response("Users retrieved", [user.to_dict() for user in users])

    @staticmethod
    def get_user(user_id):
        """Retrieve a single user"""
        user = User.query.get(user_id)
        if not user:
            return error_response("User not found")
        return success_response("User retrieved", user.to_dict())

    @staticmethod
    def update_user(user_id, data):
        """Update user details"""
        user = User.query.get(user_id)
        if not user:
            return error_response("User not found")

        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        db.session.commit()
        return success_response("User updated successfully", user.to_dict())

    @staticmethod
    def delete_user(user_id):
        """Delete a user"""
        user = User.query.get(user_id)
        if not user:
            return error_response("User not found")

        db.session.delete(user)
        db.session.commit()
        return success_response("User deleted successfully")

    @staticmethod
    def assign_role(user_id, role_id):
        """Assign a role to a user"""
        user = User.query.get(user_id)
        role = Role.query.get(role_id)

        if not user:
            return error_response("User not found")
        if not role:
            return error_response("Role not found")

        user.role_id = role_id
        db.session.commit()
        return success_response("Role assigned successfully", {"user_id": user_id, "role_id": role_id})
