import uuid

from flask import request
from flask_restful import Resource, marshal

from FlaskProject.extendsions import cache
from blog.models import UserBlog
from common import blog_fields
from common.status import HTTP_406_UNKNOW_ACCESS, HTTP_400_ERROR, HTTP_201_CREATE_OK, TIMEOUT, HTTP_200_OK
from .models import Users


class UserResource(Resource):

    def post(self):
        token = request.args.get("token")
        id = cache.get(token)
        blog = UserBlog.query.filter_by(user_id=id).first()
        if not blog:
            data = {
                "msg": "find error",
                "status": HTTP_400_ERROR
            }
            return data
        data = {
            "msg": "find success",
            "status": HTTP_200_OK,
            "data": marshal(blog, blog_fields)
        }
        return data


    def get(self):
        action = request.args.get("action")
        if action == "login":
            return self.do_login()
        elif action == "register":
            return self.do_register()
        else:
            data = {
                "msg": "unknow access",
                "status": HTTP_406_UNKNOW_ACCESS
            }
            return data

    def do_register(self):
        username = request.args.get("username")
        password = request.args.get("password")
        email = request.args.get("email")
        if username == "" or password == "" or email == "":
            data = {
                "msg": "not None",
                "status": HTTP_400_ERROR
            }
            return data
        user = Users()
        user.username = username
        user.password = password
        user.email = email
        if not user.save():
            data = {
                "msg": "save error",
                "status": HTTP_400_ERROR
            }
            return data
        data = {
            "msg": "save success",
            "status": HTTP_201_CREATE_OK
        }
        return data

    def do_login(self):
        username = request.args.get("username")
        password = request.args.get("password")
        user = Users.query.filter_by(username=username).first()
        if not user:
            data = {
                "msg": "No user",
                "status": HTTP_400_ERROR
            }
            return data
        if not user.verify_password(password):
            data = {
                "msg": "Password error",
                "status": HTTP_400_ERROR
            }
            return data
        token = uuid.uuid4().hex
        cache.set(token, user.id, TIMEOUT)
        data = {
            "msg": "login success",
            "status": HTTP_200_OK,
            "data": {
                "token": token
            }
        }
        return data







