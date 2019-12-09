from flask import request
from flask_restful import Resource, marshal

from FlaskProject.extendsions import cache
from common.blog_fields import comment_fields
from common.status import HTTP_401_PERMISSION_FAIL, HTTP_400_ERROR, HTTP_200_OK
from user.models import Users
from .models import UserComment


class CommentResource(Resource):

    def post(self):
        token = request.args.get("token")
        content = request.args.get("content")
        id = cache.get(token)
        user = Users.query.filter_by(id=id).first()
        if not user:
            data = {
                "msg": "login please",
                "status": HTTP_401_PERMISSION_FAIL
            }
            return data
        if content == "":
            data = {
                "msg": "error",
                "status": HTTP_401_PERMISSION_FAIL
            }
            return data
        comment = UserComment()
        comment.conten = content
        comment.user_id = id
        if not comment.save():
            data = {
                "msg": "save error",
                "status": HTTP_400_ERROR
            }
            return data
        data = {
            "msg": "save success",
            "statuc": HTTP_200_OK,
            "data": marshal(comment, comment_fields)
        }
        return data







