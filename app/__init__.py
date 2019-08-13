from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
from flask import request, jsonify, abort

db = SQLAlchemy()


def create_app(config_name):
    from app.models import Car

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/car/create', methods=['POST'])
    def car_create():
        if request.method == "POST":
            request_data = request.get_json(force=True)

            error = False
            message = ""

            # Make, model and year are necessary in order to create a car object
            make = ""
            if "make" in request_data.keys():
                make = request_data['make']
            else:
                error = True
                message = message + "Missing car make. "

            model = ""
            if "model" in request_data.keys():
                model = request_data['model']
            else:
                error = True
                message = message + "Missing car model. "

            year = ""
            if "year" in request_data.keys():
                year = request_data['year']
            else:
                error = True
                message = message + "Missing car year. "

            assigned_type = None
            if "assigned_type" in request_data.keys():
                assigned_type = request_data['assigned_type']

            assigned_id = None
            if "assigned_id" in request_data.keys():
                assigned_id = request_data['assigned_id']

            if (assigned_type or assigned_id) and not (assigned_type and assigned_id):
                error = True
                message = message + "Both assigned type and assigned id must be provided."

            if not error:
                car = Car(make, model, year, assigned_type, assigned_id)

                car.save()

                message = "Successfully saved a car object."
                return jsonify({"response": message})
            else:
                return jsonify({"response": message})

    @app.route('/car/get', methods=['GET'])
    def car_get():
        if request.method == "GET":
            car_id = request.args.get('car_id')

            if not car_id:
                return jsonify({"response": "Missing car ID parameter"})

            try:
                int(car_id)
            except:
                return jsonify({"response": "Invalid car ID parameter"})

            car = Car.get(car_id)
            if not car:
                return jsonify({"response": "Car doesn't exist"})

            return jsonify(car.serialize())

    @app.route('/car/update', methods=['post'])
    def car_update():
        if request.method == "POST":
            request_data = request.get_json(force=True)

            if "car_id" not in request_data.keys():
                return jsonify({"response": "Missing car ID parameter"})

            car_id = request_data['car_id']

            try:
                int(car_id)
            except:
                return jsonify({"response": "Invalid car ID parameter"})

            car = Car.get(car_id)
            if not car:
                return jsonify({"response": "Couldn't update car: ID doesn't exist"})
            return jsonify({"response": "Car updated"})
    return app
