from flask_restful import Api

from hobby.views import HobbyResource

hobby_api = Api(prefix='/hobby')

hobby_api.add_resource(HobbyResource, '/')
