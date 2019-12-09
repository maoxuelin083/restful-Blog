from flask_restful import Api

from blog.views import BlogResource

blog_api = Api(prefix='/blog')

blog_api.add_resource(BlogResource, '/')