from blog.route import blog_api
from comment.route import comment_api
from hobby.route import hobby_api
from user.route import user_api


def init_route(app):
    user_api.init_app(app)
    blog_api.init_app(app)
    hobby_api.init_app(app)
    comment_api.init_app(app)
