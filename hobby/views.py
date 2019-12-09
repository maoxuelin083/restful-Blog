from flask import request
from flask_restful import Resource, marshal

from FlaskProject.extendsions import cache
from common.blog_fields import user_fields
from common.status import HTTP_401_PERMISSION_FAIL, HTTP_400_ERROR, HTTP_200_OK
from user.models import Users
from .models import HobbyBlog


class HobbyResource(Resource):

    def post(self):
        token = request.args.get("token")
        blog_id = request.args.get("blog_id")  # 传过来的收藏文章的id
        id = cache.get(token)
        user = Users.query.filter_by(id=id).first()
        if not user:
            data = {
                "msg": "login please",
                "status": HTTP_401_PERMISSION_FAIL
            }
            return data
        hobby = HobbyBlog()
        hobby.user_id = id
        hobby.blog_id = blog_id
        if not hobby.save():
            data = {
                "msg": "save error",
                "status": HTTP_400_ERROR
            }
            return data
        data = {
            "msg": "save success",
            "status": HTTP_200_OK,
            "data": marshal(user, user_fields)
        }
        return data


