from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

api=Api(app)

capitals ={
    'Mumbai':'Maharashtra',
    'Delhi' : 'Delhi',
    'Bhopal' :'MP'
}

capital_post_args=reqparse.RequestParser()
capital_post_args.add_argument('city',type=str,required=True,help='City is required')
capital_post_args.add_argument('state',type=str,required=True,help='state is required')
 
class Hello(Resource):
    def get(self):
        return {'data': 'Hello World!, This is for capital list'}
    
class GetCapitals(Resource):
    def get(self):
        return capitals
    
class GetState(Resource):
    def get(self,city):
        return {city: capitals[city]}

class AddCapital(Resource):
    def post(self):
        args=capital_post_args.parse_args()
        capitals[args['city']]=args['state']
        return capitals

class DeleteCapital(Resource):
    def delete(self,city):
        del capitals[city]
        return capitals




api.add_resource(Hello,'/')
api.add_resource(GetCapitals,'/capitals')
api.add_resource(GetState,'/getState/<string:city>')
api.add_resource(AddCapital,'/add')
api.add_resource(DeleteCapital,'/remove/<string:city>')


if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)