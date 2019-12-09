from flask_restful import fields

blogs_fields = {
    'title': fields.String(attribute="title"),
    'content': fields.String(attribute="content"),
    'user_id': fields.Integer(attribute="user_id")
}

user_fields = {
    'name': fields.String(attribute="username")
}

comment_fields = {
    'id': fields.Integer(attribute="user_id"),
    "content": fields.String(attribute="conten")
}
