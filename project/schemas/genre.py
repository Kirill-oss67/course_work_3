from marshmallow import fields, Schema


class GenreSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
