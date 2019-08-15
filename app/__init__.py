from flask_api import FlaskAPI, exceptions
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
from flask import request, jsonify
from app import helpers

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
        """
        Creates a record based on params supplied
        Endpoint URL: /car/create
        :return: JSON successful message or exception response
        """
        if request.method == "POST":
            if request.data is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})
            request_data = request.data

            try:
                # Find and validate required parameters in order to create car record
                make = helpers.check_missing('list', request_data, 'make')
                model = helpers.check_missing('list', request_data, 'model')
                year = helpers.check_missing('list', request_data, 'year')
                year = helpers.validate_year(year)
                assigned_type = helpers.check_missing('list', request_data, 'assigned_type')
                assigned_id = helpers.check_missing('list', request_data, 'assigned_id')
                assigned_id = helpers.validate_int(assigned_id, 'assigned_id')

                # Validate the assigned type and id, more logic for assigning in a helper function
                assigned_type, assigned_id = helpers.validate_assigning(assigned_type, assigned_id)

                # Create object and save it in the database
                car = Car(make, model, year, assigned_type, assigned_id)
                car.save()
                return jsonify({"status_code": 201, "message": "Car created"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/car/get', methods=['GET'])
    def car_get():
        """
        Gets a record based on parameters supplied to the endpoint. Returns first suitable found object based on params
        Endpoint URL: /car/get
        :return: JSON of an object or exception status
        """
        if request.method == "GET":
            if request.args is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})

            try:
                params = {}  # list of params that we will search by
                # Check if any of the parameters are being passed and then validate them
                if "id" in request.args.keys():
                    params['id'] = helpers.validate_int(request.args.get('id'), 'id')
                if "make" in request.args.keys():
                    params['make'] = helpers.validate_string(request.args.get('make'), 'make')
                if "model" in request.args.keys():
                    params['model'] = helpers.validate_string(request.args.get('model'), 'model')
                if "year" in request.args.keys():
                    params['year'] = helpers.validate_year(request.args.get('year'))
                if "assigned_type" in request.args.keys():
                    params['assigned_type'] = helpers.validate_int(request.args.get('assigned_type'), 'assigned_type')
                if "assigned_id" in request.args.keys():
                    params['assigned_id'] = helpers.validate_int(request.args.get('assigned_id'), 'assigned_id')

                # If no allowed params were passed on - invalidate the request
                if not params:
                    raise Exception({"status_code": 400, "message": "Invalid request"})

                # Get the object based on the given parameters
                car = Car.get(params)
                if not car:
                    raise Exception({"status_code": 404, "message": "Car not found"})
                return jsonify(car.serialize())
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/car/update', methods=['PUT'])
    def car_update():
        """
        Updates a record based on id supplied
        Endpoint URL: /car/update
        :return: JSON successful message or exception response
        """
        if request.method == "PUT":
            if request.data is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})
            request_data = request.data

            try:
                # Validate id parameter passed
                id = helpers.check_missing('list', request_data, 'id')
                id = helpers.validate_int(id, 'id')

                # Find the object to update
                params = {"id": id}
                car = Car.get(params)

                # Return 404 if not found the object to update
                if not car:
                    raise Exception({"status_code": 404, "message": "Car not found"})

                # Find and validate any allowed parameters
                if "make" in request_data.keys():
                    car.make = helpers.validate_string(request_data['make'], 'make')
                if "model" in request_data.keys():
                    car.model = helpers.validate_string(request_data['model'], 'model')
                if "year" in request.data.keys():
                    car.year = helpers.validate_year(request_data['year'])

                # Logic to enforce assigned type and id to be passed on and validated together
                if "assigned_type" in request_data.keys() and not "assigned_id" in request_data.keys():
                    raise Exception({"status_code": 400, "message": "Missing assigned_id"})
                elif "assigned_id" in request_data.keys() and not "assigned_type" in request_data.keys():
                    raise Exception({"status_code": 400, "message": "Missing assigned_type"})
                elif set(("assigned_type", "assigned_id")) <= request_data.keys():
                    assigned_type, assigned_id = helpers.validate_assigning(request_data['assigned_type'],
                                                                            request_data['assigned_id'])
                    car.assigned_type = assigned_type
                    car.assigned_id = assigned_id

                # Save an object and return successful message
                car.save()
                return jsonify({"status_code": 200, "message": "Car record was updated"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/car/delete', methods=['DELETE'])
    def car_delete():
        """
        Deletes a record based on the id
        Endpoint URL: /car/delete
        :return: JSON successful message or exception response
        """
        if request.method == "DELETE":
            if request.args is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})

            try:
                # Validate id parameter passed
                id = helpers.check_missing('args', request, 'id')
                id = helpers.validate_int(id, 'id')

                # Find the object to delete
                params = {"id": id}
                car = Car.get(params)

                # Return 404 if not found the object to delete
                if not car:
                    return jsonify({"status_code": 404, "message": "Car not found"})

                # Delete object and return successful message
                car.delete()
                return jsonify({"status_code": 200, "message": "Car deleted"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/branch/create', methods=['POST'])
    def branch_create():
        """
        Creates a record based on params supplied
        Endpoint URL: /branch/create
        :return: JSON successful message or exception response
        """
        if request.method == "POST":
            if request.data is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})
            request_data = request.data

            try:
                # Find and validate required parameters in order to create branch record
                city = helpers.check_missing('list', request_data, 'city')
                city = helpers.validate_string(city, 'city')
                postcode = helpers.check_missing('list', request_data, 'postcode')
                postcode = helpers.validate_postcode(postcode)
                capacity = helpers.check_missing('list', request_data, 'capacity')
                capacity = helpers.validate_int(capacity, 'capacity')

                # Create object and save it in the database
                branch = Branch(city, postcode, capacity)
                branch.save()
                return jsonify({"status_code": 201, "message": "Branch created"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/branch/get', methods=['GET'])
    def branch_get():
        """
        Gets a record based on parameters supplied to the endpoint. Returns first suitable found object based on params
        Endpoint URL: /branch/get
        :return: JSON of an object or exception status
        """
        if request.method == "GET":
            if request.args is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})

            try:
                params = {}  # list of params that we will search by
                # Check if any of the parameters are being passed and then validate them
                if "id" in request.args.keys():
                    params['id'] = helpers.validate_int(request.args.get('id'), 'id')
                if "city" in request.args.keys():
                    params['city'] = helpers.validate_string(request.args.get('city'), 'city')
                if "postcode" in request.args.keys():
                    params['postcode'] = helpers.validate_postcode(request.args.get('postcode'))
                if "capacity" in request.args.keys():
                    params['capacity'] = helpers.validate_int(request.args.get('capacity'), 'capacity')

                # If no allowed params were passed on - invalidate the request
                if not params:
                    return jsonify({"status_code": 400, "message": "Invalid request"})

                # Get the object based on the given parameters
                branch = Branch.get(params)
                if not branch:
                    return jsonify({"status_code": 404, "message": "Branch not found"})
                return jsonify(branch.serialize())

            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/branch/update', methods=['PUT'])
    def branch_update():
        """
        Updates a record based on id supplied
        Endpoint URL: /branch/update
        :return: JSON successful message or exception response
        """
        if request.method == "PUT":
            if request.data is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})
            request_data = request.data

            try:
                # Validate id parameter passed
                id = helpers.check_missing('list', request_data, 'id')
                id = helpers.validate_int(id, 'id')

                # Find the object to update
                params = {"id": id}
                branch = Branch.get(params)

                # Return 404 if not found the object to update
                if not branch:
                    return jsonify({"status_code": 404, "message": "Branch not found"})

                # Find and validate any allowed parameters
                if "city" in request_data.keys():
                    branch.city = helpers.validate_string(request_data['city'], 'city')
                if "postcode" in request_data.keys():
                    branch.postcode = helpers.validate_postcode(request_data['postcode'])
                if "capacity" in request_data.keys():
                    branch.capacity = helpers.validate_int(request_data['capacity'], 'capacity')

                # Save an object and return successful message
                branch.save()
                return jsonify({"status_code": 200, "message": "Branch record was updated"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/branch/delete', methods=['DELETE'])
    def branch_delete():
        """
        Deletes a record based on the id
        Endpoint URL: /branch/delete
        :return: JSON successful message or exception response
        """
        if request.method == "DELETE":
            if request.args is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})

            try:
                # Validate id parameter passed
                id = helpers.check_missing('args', request, 'id')
                id = helpers.validate_int(id, 'id')

                # Find the object to delete
                params = {"id": id}
                branch = Branch.get(params)

                # Return 404 if not found the object to delete
                if not branch:
                    return jsonify({"status_code": 404, "message": "Branch not found"})

                # Delete object and return successful message
                branch.delete()
                return jsonify({"status_code": 200, "message": "Branch deleted"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/driver/create', methods=['POST'])
    def driver_create():
        """
        Creates a record based on params supplied
        Endpoint URL: /driver/create
        :return: JSON successful message or exception response
        """
        if request.method == "POST":
            if request.data is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})
            request_data = request.data

            try:
                # Find and validate required parameters in order to create driver record
                first_name = helpers.check_missing('list', request_data, 'first_name')
                first_name = helpers.validate_string(first_name, 'first_name')

                # Middle name is optional for creating a driver
                middle_name = None
                if "middle_name" in request_data.keys():
                    middle_name = helpers.validate_string(request_data['middle_name'], 'middle_name')
                last_name = helpers.check_missing('list', request_data, 'last_name')
                last_name = helpers.validate_string(last_name, 'last_name')
                dob = helpers.check_missing('list', request_data, 'dob')
                dob = helpers.validate_dob(dob)  # Only accepting drivers that are 18 or older

                # Create object and save it in the database
                driver = Driver(first_name, middle_name, last_name, dob)
                driver.save()
                return jsonify({"status_code": 201, "message": "Driver created"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/driver/get', methods=['GET'])
    def driver_get():
        """
        Gets a record based on parameters supplied to the endpoint. Returns first suitable found object based on params
        Endpoint URL: /driver/get
        :return: JSON of an object or exception status
        """
        if request.method == "GET":
            if request.args is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})

            try:
                params = {}  # list of params that we will search by
                # Check if any of the parameters are being passed and then validate them
                if "id" in request.args.keys():
                    params['id'] = helpers.validate_int(request.args.get('id'), 'id')
                if "first_name" in request.args.keys():
                    params["first_name"] = helpers.validate_string(request.args.get('first_name'), 'first_name')
                if "middle_name" in request.args.keys():
                    params["middle_name"] = helpers.validate_string(request.args.get('middle_name'), 'middle_name')
                if "last_name" in request.args.keys():
                    params["last_name"] = helpers.validate_string(request.args.get('last_name'), 'last_name')
                if "dob" in request.args.keys():
                    params["dob"] = helpers.validate_dob(request.args.get('dob'))

                # If no allowed params were passed on - invalidate the request
                if not params:
                    return jsonify({"status_code": 400, "message": "Invalid request"})

                # Get the object based on the given parameters
                driver = Driver.get(params)
                if not driver:
                    return jsonify({"status_code": 404, "message": "Driver not found"})
                return jsonify(driver.serialize())
            except Exception as e:  # Return messages of any exceptions raised during validation
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/driver/update', methods=['PUT'])
    def driver_update():
        """
        Updates a record based on id supplied
        Endpoint URL: /driver/update
        :return: JSON successful message or exception response
        """
        if request.method == "PUT":
            if request.data is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})
            request_data = request.data

            try:
                # Validate id parameter passed
                id = helpers.check_missing('list', request_data, 'id')
                id = helpers.validate_int(id, 'id')

                # Find the object to update
                params = {"id": id}
                driver = Driver.get(params)

                # Return 404 if not found the object to update
                if not driver:
                    return jsonify({"status_code": 404, "message": "Driver not found"})

                # Find and validate any allowed parameters
                if "first_name" in request_data.keys():
                    driver.first_name = helpers.validate_string(request_data['first_name'], 'first_name')
                if "middle_name" in request_data.keys():
                    driver.middle_name = helpers.validate_string(request_data['middle_name'], 'middle_name')
                if "last_name" in request_data.keys():
                    driver.last_name = helpers.validate_string(request_data['last_name'], 'last_name')
                if "dob" in request_data.keys():
                    driver.dob = helpers.validate_dob(request_data["dob"])

                # Save an object and return successful message
                driver.save()
                return jsonify({"status_code": 200, "message": "Driver record was updated"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    @app.route('/driver/delete', methods=['DELETE'])
    def driver_delete():
        """
        Deletes a record based on the id
        Endpoint URL: /driver/delete
        :return: JSON successful message or exception response
        """
        if request.method == "DELETE":
            if request.args is None:
                return jsonify({"status_code": 400, "message": "Invalid request"})

            try:
                # Validate id parameter passed
                id = helpers.check_missing('args', request, 'id')
                id = helpers.validate_int(id, 'id')

                # Find the object to delete
                params = {"id": id}
                driver = Driver.get(params)

                # Return 404 if not found the object to delete
                if not driver:
                    return jsonify({"status_code": 404, "message": "Driver not found"})

                # Delete object and return successful message
                driver.delete()
                return jsonify({"status_code": 200, "message": "Driver deleted"})
            except Exception as e:
                return jsonify({"status_code": e.args[0]['status_code'], "message": e.args[0]['message']})

    return app
