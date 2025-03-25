from flask import Blueprint, request
from app.models.user import User
from app.database import db
from app.utils.response_helper import success_response, error_response
from app.utils.message_enum import MessageEnum

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def get_users():
    """Retrieve all users"""
    users = User.query.all()

    if not users:
        return error_response(MessageEnum.USER_NOT_FOUND.value, status_code=404)

    return success_response(MessageEnum.USER_FETCHED.value, [user.to_dict() for user in users])


@user_bp.route("/", methods=["POST"])
def create_user():
    """Create a new user"""
    data = request.get_json()

    if not data or "username" not in data or "email" not in data:
        return error_response(MessageEnum.MISSING_FIELDS.value, status_code=400)

    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()

    return success_response(MessageEnum.USER_CREATED.value, user.to_dict(), status_code=201)
