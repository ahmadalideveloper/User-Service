from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=3, max=50))
    middle_name = fields.String(required=False, validate=validate.Length(min=0, max=50))
    last_name = fields.String(required=True, validate=validate.Length(min=3, max=50))
    username = fields.String(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))
    primary_phone_number = fields.String(required=True,validate=validate.Length(min=11, max=11))
    secondary_phone_number = fields.String(required=False, validate=validate.Length(min=0, max=11) )
    role_id = fields.Integer(required=False)

class RoleSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3, max=50))
