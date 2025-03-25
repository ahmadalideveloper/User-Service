from enum import Enum

class MessageEnum(Enum):
    # Success Messages
    USER_CREATED = "User created successfully"
    USER_CREATION_FAILED = "Failed to create user!"
    USER_FETCHED = "Users retrieved successfully"
    USER_UPDATED = "User updated successfully"
    USER_DELETED = "User deleted successfully"

    ROLE_CREATED = "Role created successfully"
    ROLE_UPDATED = "Role updated successfully"
    ROLE_DELETED = "Role deleted successfully"

    PERMISSION_GRANTED = "Permission granted successfully"
    PERMISSION_REVOKED = "Permission revoked successfully"

    # Error Messages
    USER_NOT_FOUND = "User not found"
    ROLE_NOT_FOUND = "Role not found"
    PERMISSION_NOT_FOUND = "Permission not found"

    MISSING_FIELDS = "Missing required fields"
    INVALID_INPUT = "Invalid input data"
    UNAUTHORIZED = "Unauthorized access"
    FORBIDDEN = "You do not have permission to perform this action"
    INTERNAL_ERROR = "An internal server error occurred"
