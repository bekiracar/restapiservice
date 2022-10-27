from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/<string:name>")  
def welcome(name):
    return "Hoşgeldin "+name

@app.route("/")  
def index():
    return "<html><head><title>Python Flask ile Restful api servisi</title></head><body><b>Kullanım şekilleri</b> <br>    url/string:name <br>url/hello <br>url/karesi/int:num</body></html>"

class Hello(Resource):
	def get(self):
		return jsonify({'message': 'hello world'})
    
	def post(self):
		data = request.get_json()	
		return jsonify({'data': data}), 201

class Karesi(Resource):
	def get(self, num):
		return jsonify({'karesi': num**2})
api.add_resource(Hello, '/hello')
api.add_resource(Karesi, '/karesi/<int:num>')

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=81)
