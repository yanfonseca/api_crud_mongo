from marshmallow import Schema, fields

class BaseDoc(Schema):
    _id = fields.Integer(required=False , data_key="id")
    name = fields.String(required=False)

class Changes(Schema):
    name = fields.String(required=True)

class Add(Schema):
    _id = fields.Integer(required=True, data_key="id")
    name = fields.String(required=True)
    version = fields.Integer(required=False)

class Delete(Schema):
    id = fields.Integer(required=True)

class Update(Schema):
    query = fields.Nested(BaseDoc(), required=True)
    changes = fields.Nested(Changes(), required=True)