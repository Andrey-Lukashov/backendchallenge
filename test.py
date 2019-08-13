import unittest
from app import create_app, db
from flask import json


class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_can_create_car_without_assigning(self):
        """ Test that API can create a new car via POST request to the endpoint"""
        data = dict(make="Tesla", model="Model 3", year=2018)

        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)

        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Successfully saved a car object.')

    def test_can_create_car_with_assigning(self):
        pass

    def test_cant_create_car_invalid_request(self):
        """ Test that API will return 400 (bad request) for invalid requests"""
        res = self.client.post('/car/create')
        self.assertEqual(res.status_code, 400)

        res = self.client.post('/car/create', data=None, content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_cant_create_car_missing_params(self):
        """ Test that API will return expected errors when params are missing"""
        data = dict()
        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Missing car make. Missing car model. Missing car year. ')

        data = dict(model="Model 3", year=2018)
        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Missing car make. ')

        data = dict(make="Tesla", year=2018)
        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Missing car model. ')

        data = dict(make="Tesla", model="Model 3")
        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Missing car year. ')

        data = dict(make="Tesla", model="Model 3", year=2018, assigned_type=1)
        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Both assigned type and assigned id must be provided.')

        data = dict(make="Tesla", model="Model 3", year=2018, assigned_id=1)
        res = self.client.post('/car/create', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Both assigned type and assigned id must be provided.')

    def test_can_get_car(self):
        data = dict(make="BMW", model="530d", year=2018)
        self.client.post('/car/create', data=json.dumps(data), content_type='application/json')

        data = dict(car_id=1)
        res = self.client.get('/car/get', query_string=data, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['make'], 'BMW')
        self.assertEqual(json_response['model'], '530d')
        self.assertEqual(json_response['year'], 2018)

    def test_cant_get_car_invalid_request(self):
        res = self.client.get('/car/get')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Missing car ID parameter')

    def test_cant_get_car_missing_params(self):
        data = dict()
        res = self.client.get('/car/get', query_string=data, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], 'Missing car ID parameter')

    def test_cant_get_car_id_doesnt_exist(self):
        data = dict(car_id=100)
        res = self.client.get('/car/get', query_string=data, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], "Car doesn't exist")

    def test_cant_get_car_id_has_to_be_int(self):
        data = dict(car_id="abcd")
        res = self.client.get('/car/get', query_string=data, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        json_response = res.get_json()
        self.assertEqual(json_response['response'], "Invalid car ID parameter")

    def test_can_update_car(self):
        pass

    def test_can_delete_car(self):
        pass

    def test_can_assign_car_to_driver(self):
        pass

    def test_can_assign_car_to_branch(self):
        pass

    def test_wont_assign_to_non_existing_driver(self):
        pass

    def test_wont_assign_to_non_existing_branch(self):
        pass

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


class BranchTestCase(unittest.TestCase):
    pass


class DriverTestCase(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
