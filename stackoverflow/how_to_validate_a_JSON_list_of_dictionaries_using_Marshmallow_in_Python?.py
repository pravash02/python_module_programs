from marshmallow import Schema, fields, validate


class AuthUserSchema(Schema):
    user = fields.String()
    password = fields.String()
    enabled = fields.Boolean()


class AuthDataSchema(Schema):
    data = fields.Nested(AuthUserSchema, many=True)


data = [
    {
        "enabled": True,
        "password": "6e5b5410415bde",
        "user": "admin"
    },
    {
        "enabled": True,
        "password": "4e5b5410415bde",
        "user": "guest"
    },
]

schema = AuthDataSchema()
errors = schema.validate({"data": data})
print(errors)
