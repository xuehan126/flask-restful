from flask import request
from flask_restful import Api, Resource, reqparse

api = Api()
def init_api(app):
    api.init_app(app)

class UserApi(Resource):
    def get(self):
        return {'state':'ok',
                'data':[{"name":"disen","age":20},
                        {"name":"jack","age":10}]}
# api.add_resource(UserApi,'/user/')
    def post(self):
        # 从上传的form对象中取出namehe
        name = request.form.get('name')
        phone = request.form.get('phone')
        print(name, phone)

        return {"state":"ok", "msg":"添加{} 用户成功".format(name)}

