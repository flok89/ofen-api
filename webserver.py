from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
import random
# from EmulatorGUI import GPIO

app = Flask(__name__)
api = Api(app)

class Live(Resource):
    def get(self):
        now = datetime.now()
        temp = round(random.uniform(20, 30), 1)
        return {'temperature': temp, 'date': now.strftime('%Y-%m-%d %H:%M:%S')}, 200

class History(Resource):
    def get(self):
        now = datetime.now()
        temp = round(random.uniform(0, 10), 1)
        return {'id': 1, 'temperature': temp,
            'date': now.strftime('%Y-%m-%d %H:%M:%S')}, 200

api.add_resource(Live, '/')
api.add_resource(History, '/history')

if __name__ == '__main__':
    app.run(debug=True)
else:
    app.run()