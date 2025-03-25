from flask import jsonify
from app.utils.message_enum import MessageEnum

def success_response(message=MessageEnum.USER_FETCHED.value, data=None, status_code=200):
    """Return a standardized success response."""
    response = {
        "success": True,
        "message": message,
        "data": data or {},
    }
    return jsonify(response), status_code

def error_response(message=MessageEnum.INTERNAL_ERROR.value, errors=None, status_code=400):
    """Return a standardized error response."""
    response = {
        "success": False,
        "message": message,
        "errors": errors or [],
    }
    return jsonify(response), status_code

def validation_error_response(errors, message=MessageEnum.INVALID_INPUT.value):
    """Return a standardized validation error response."""
    return error_response(message, errors, 422)
