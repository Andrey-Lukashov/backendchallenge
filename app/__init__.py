from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
from flask import request, jsonify, abort
import re
import datetime
from datetime import date

db = SQLAlchemy()


def create_app(config_name):
    from app.models import Car, Branch, Driver

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/car/create', methods=['POST'])
    def car_create():
        if request.method == "POST":
            request_data = request.get_json(force=True)

            if request_data is None:
                return jsonify({
                    "status": 400,
                    "message": "Invalid request"
                })

            # Make, model and year are necessary in order to create a car object
            if "make" in request_data.keys():
                make = request_data['make']
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing make"
                })

            if "model" in request_data.keys():
                model = request_data['model']
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing model"
                })

            if "year" in request_data.keys():
                try:
                    int(request_data['year'])
                    year = request_data['year']
                except:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid year"
                    })
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing year"
                })

            assigned_type = None
            if "assigned_type" in request_data.keys():
                assigned_type = request_data['assigned_type']

            assigned_id = None
            if "assigned_id" in request_data.keys():
                assigned_id = request_data['assigned_id']

            if (assigned_type or assigned_id) and not (assigned_type and assigned_id):
                return jsonify({
                    "status": 400,
                    "message": "Both assigned type and id must be present"
                })

            car = Car(make, model, year, assigned_type, assigned_id)
            car.save()
            return jsonify({
                "status": 201,
                "message": "Car created"}
            )

    @app.route('/car/get', methods=['GET'])
    def car_get():
        if request.method == "GET":
            car_id = request.args.get('car_id')

            if not car_id:
                return jsonify({
                    "status": 400,
                    "message": "Missing car ID"
                })
            try:
                int(car_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid car ID"
                })

            car = Car.get(car_id)
            if not car:
                return jsonify({
                    "status": 404,
                    "message": "Car not found"
                })

            return jsonify(car.serialize())

    @app.route('/car/update', methods=['PUT'])
    def car_update():
        if request.method == "PUT":
            request_data = request.get_json(force=True)

            if request_data is None:
                return jsonify({
                    "status": 400,
                    "message": "Invalid request"
                })

            if "car_id" not in request_data.keys():
                return jsonify({
                    "status": 400,
                    "message": "Missing car ID"
                })

            car_id = request_data['car_id']

            try:
                int(car_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid car ID"
                })

            car = Car.get(car_id)

            if not car:
                return jsonify({
                    "status": 404,
                    "message": "Car not found"
                })

            if "make" in request_data.keys():
                car.make = request_data['make']

            if "model" in request_data.keys():
                car.model = request_data['model']

            if "year" in request_data.keys():
                try:
                    int(request_data['year'])
                    car.year = request_data['year']
                except:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid year"
                    })

            car.save()

            return jsonify({
                "status": 200,
                "message": "Car record was updated"
            })

    @app.route('/car/delete', methods=['DELETE'])
    def car_delete():
        if request.method == "DELETE":

            if not "car_id" in request.args:
                return jsonify({
                    "status": 400,
                    "message": "Missing car ID"
                })

            car_id = request.args.get("car_id")

            try:
                int(car_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid car ID"
                })

            car = Car.get(car_id)

            if not car:
                return jsonify({
                    "status": 404,
                    "message": "Car not found"
                })

            car.delete()

            return jsonify({
                "status": 200,
                "message": "Car deleted"
            })

    @app.route('/branch/create', methods=['POST'])
    def branch_create():
        if request.method == "POST":
            request_data = request.get_json(force=True)

            if request_data is None:
                return jsonify({
                    "status": 400,
                    "message": "Invalid request"
                })

            # Make, model and year are necessary in order to create a car object
            if "city" in request_data.keys():
                city = request_data['city']
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing city"
                })

            if "postcode" in request_data.keys():
                postcode = request_data['postcode']
                if len(postcode) > 8:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid postcode"
                    })
                pattern = re.compile(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b')
                if not pattern.match(postcode):
                    return jsonify({
                        "status": 400,
                        "message": "Invalid postcode"
                    })
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing postcode"
                })

            if "capacity" in request_data.keys():
                try:
                    int(request_data['capacity'])
                    capacity = request_data['capacity']
                except:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid capacity"
                    })
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing capacity"
                })

            car = Branch(city, postcode, capacity)
            car.save()
            return jsonify({
                "status": 201,
                "message": "Branch created"}
            )

    @app.route('/branch/get', methods=['GET'])
    def branch_get():
        if request.method == "GET":
            branch_id = request.args.get('branch_id')

            if not branch_id:
                return jsonify({
                    "status": 400,
                    "message": "Missing branch ID"
                })
            try:
                int(branch_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid branch ID"
                })

            branch = Branch.get(branch_id)
            if not branch:
                return jsonify({
                    "status": 404,
                    "message": "Branch not found"
                })

            return jsonify(branch.serialize())

    @app.route('/branch/update', methods=['PUT'])
    def branch_update():
        if request.method == "PUT":
            request_data = request.get_json(force=True)

            if request_data is None:
                return jsonify({
                    "status": 400,
                    "message": "Invalid request"
                })

            if "branch_id" not in request_data.keys():
                return jsonify({
                    "status": 400,
                    "message": "Missing branch ID"
                })

            branch_id = request_data['branch_id']

            try:
                int(branch_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid branch ID"
                })

            branch = Branch.get(branch_id)

            if not branch:
                return jsonify({
                    "status": 404,
                    "message": "Branch not found"
                })

            if "city" in request_data.keys():
                branch.city = request_data['city']

            if "postcode" in request_data.keys():
                postcode = request_data['postcode']
                if len(postcode) > 8:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid postcode"
                    })
                pattern = re.compile(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b')
                if not pattern.match(postcode):
                    return jsonify({
                        "status": 400,
                        "message": "Invalid postcode"
                    })
                branch.postcode = request_data['postcode']

            if "capacity" in request_data.keys():
                try:
                    int(request_data['capacity'])
                    branch.capacity = request_data['capacity']
                except:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid capacity"
                    })

            branch.save()

            return jsonify({
                "status": 200,
                "message": "Branch record was updated"
            })

    @app.route('/branch/delete', methods=['DELETE'])
    def branch_delete():
        if request.method == "DELETE":

            if not "branch_id" in request.args:
                return jsonify({
                    "status": 400,
                    "message": "Missing branch ID"
                })

            branch_id = request.args.get("branch_id")

            try:
                int(branch_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid branch ID"
                })

            branch = Branch.get(branch_id)

            if not branch:
                return jsonify({
                    "status": 404,
                    "message": "Branch not found"
                })

            branch.delete()

            return jsonify({
                "status": 200,
                "message": "Branch deleted"
            })

    @app.route('/driver/create', methods=['POST'])
    def driver_create():
        if request.method == "POST":
            request_data = request.get_json(force=True)

            # Make, model and year are necessary in order to create a car object
            if "name" in request_data.keys():
                name = request_data['name']
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing name"
                })

            if "dob" in request_data.keys():
                try:
                    dob = datetime.datetime.strptime(request_data['dob'], '%d/%m/%Y')

                    # Won't let drivers below age 18 to join
                    min_age = datetime.timedelta(weeks=52 * 18)
                    if datetime.datetime.now() - dob < min_age:
                        return jsonify({
                            "status": 400,
                            "message": "Invalid DOB"
                        })

                    dob = dob.strftime("%m/%d/%Y")

                except:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid DOB"
                    })
            else:
                return jsonify({
                    "status": 400,
                    "message": "Missing DOB"
                })

            driver = Driver(name, dob)
            driver.save()
            return jsonify({
                "status": 201,
                "message": "Driver created"}
            )

    @app.route('/driver/get', methods=['GET'])
    def driver_get():
        if request.method == "GET":
            driver_id = request.args.get('driver_id')

            if not driver_id:
                return jsonify({
                    "status": 400,
                    "message": "Missing driver ID"
                })
            try:
                int(driver_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid driver ID"
                })

            driver = Driver.get(driver_id)
            if not driver:
                return jsonify({
                    "status": 404,
                    "message": "Driver not found"
                })

            return jsonify(driver.serialize())

    @app.route('/driver/update', methods=['PUT'])
    def driver_update():
        if request.method == "PUT":
            request_data = request.get_json(force=True)

            if "driver_id" not in request_data.keys():
                return jsonify({
                    "status": 400,
                    "message": "Missing driver ID"
                })

            driver_id = request_data['driver_id']

            try:
                int(driver_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid driver ID"
                })

            driver = Driver.get(driver_id)

            if not driver:
                return jsonify({
                    "status": 404,
                    "message": "Driver not found"
                })

            if "name" in request_data.keys():
                driver.name = request_data['name']

            if "dob" in request_data.keys():
                try:
                    dob = datetime.datetime.strptime(request_data['dob'], '%d/%m/%Y')

                    # Won't let drivers below age 18 to join
                    min_age = datetime.timedelta(weeks=52 * 18)
                    if datetime.datetime.now() - dob < min_age:
                        return jsonify({
                            "status": 400,
                            "message": "Invalid DOB"
                        })

                    driver.dob = request_data['dob']

                except:
                    return jsonify({
                        "status": 400,
                        "message": "Invalid DOB"
                    })

            driver.save()

            return jsonify({
                "status": 200,
                "message": "Driver record was updated"
            })

    @app.route('/driver/delete', methods=['DELETE'])
    def driver_delete():
        if request.method == "DELETE":

            if not "driver_id" in request.args:
                return jsonify({
                    "status": 400,
                    "message": "Missing driver ID"
                })

            driver_id = request.args.get("driver_id")

            try:
                int(driver_id)
            except:
                return jsonify({
                    "status": 400,
                    "message": "Invalid driver ID"
                })

            driver = Driver.get(driver_id)

            if not driver:
                return jsonify({
                    "status": 404,
                    "message": "Driver not found"
                })

            driver.delete()

            return jsonify({
                "status": 200,
                "message": "Driver deleted"
            })

    return app
