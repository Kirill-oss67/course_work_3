from marshmallow import fields, Schema


class UserCreatedSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class AuthRegisterRequest(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
