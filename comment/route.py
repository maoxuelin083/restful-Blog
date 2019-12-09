from flask_restful import Api

from comment.views import CommentResource

comment_api = Api(prefix='/comment')

comment_api.add_resource(CommentResource, '/')
