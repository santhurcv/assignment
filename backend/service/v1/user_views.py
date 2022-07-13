from flask import Flask,jsonify,make_response, request
from flask_restx import Resource
from flask_pymongo import PyMongo
from service.v1.swagger_models import api
import pandas as pd
import json, sys


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo:27017/smarteye_test'
mongo=PyMongo(app)

class Pract(Resource):

    def post(self):
        try:
            xl_file = request.files['file']
            data = pd.read_excel(xl_file)
            if(data.empty):
                return make_response(
                    jsonify(
                        {
                            "message": "file is empty", 
                            "status_code": 400
                        }
                    ),
                    400,
                )
            json_data = json.loads(data.to_json(orient='records'))
            for json1 in json_data:
                mongo.db.xl.insert_one(
                    {
                        "json_data" : json1
                    }
                )
            return make_response(
                jsonify(
                    {
                        "message": "successfully Updated into DB", 
                        "status_code": 200
                    }
                ),
                200,
            )
        except Exception as e:
            msg1= 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e
            return make_response(
                jsonify(
                    {
                        "message": "Unable to process your request", 
                        "status_code": 500,
                        "error": msg1
                    }
                ),
                500,
            )

api.add_resource(Pract,'/create')