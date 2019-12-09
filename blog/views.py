from flask import request
from flask_restful import Resource, marshal

from FlaskProject.extendsions import cache
from common.blog_fields import blogs_fields
from common.status import HTTP_400_ERROR, HTTP_401_PERMISSION_FAIL, HTTP_200_OK
from user.models import Users
from .models import UserBlog


class BlogResource(Resource):

    # 输入用户token 进行发帖
    def post(self):
        token = request.args.get("token")
        title = request.args.get("title")
        content = request.args.get("content")
        id = cache.get(token)
        user = Users.query.filter_by(id=id).first()
        if not user:
            data = {
                "msg": "login please",
                "status": HTTP_401_PERMISSION_FAIL
            }
            return data
        if title =="" or content == "":
            data = {
                "msg": "save error",
                "status": HTTP_400_ERROR
            }
            return data
        blog = UserBlog()
        blog.title = title
        blog.content = content
        blog.user_id = id
        if not blog.save():
            data = {
                "msg": "save error",
                "status": HTTP_400_ERROR
            }
            return data
        data = {
            "msg": "save success",
            "status": HTTP_200_OK,
            "data": marshal(blog, blogs_fields)
        }
        return data

