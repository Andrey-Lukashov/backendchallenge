from app import db
import datetime

class Car(db.Model):
    __tablename__ = 'car'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    assigned_type = db.Column(db.Integer(), nullable=True)
    assigned_id = db.Column(db.Integer(), nullable=True)

    def __init__(self, make, model, year, assigned_type=None, assigned_id=None):
        self.make = make
        self.model = model
        self.year = year
        self.assigned_type = assigned_type
        self.assigned_id = assigned_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get(params):
        query = db.session.query(Car)
        if "id" in params.keys():
            query = query.filter(Car.id == params['id'])
        if "make" in params.keys():
            query = query.filter(Car.make == params['make'])
        if "model" in params.keys():
            query = query.filter(Car.model == params['model'])
        if "year" in params.keys():
            query = query.filter(Car.year == params['year'])
        if "assigned_type" in params.keys():
            query = query.filter(Car.assigned_type == params['assigned_type'])
        if "assigned_id" in params.keys():
            query = query.filter(Car.assigned_id == params['assigned_id'])
        return query.first()

    def serialize(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "assigned_type": self.assigned_type,
            "assigned_id": self.assigned_id
        }


class Branch(db.Model):
    __tablename__ = 'branch'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(60), nullable=False)
    postcode = db.Column(db.String(8), nullable=False)
    capacity = db.Column(db.Integer(), nullable=False)

    def __init__(self, city, postcode, capacity):
        self.city = city
        self.postcode = postcode
        self.capacity = capacity

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get(params):
        query = db.session.query(Branch)
        if "id" in params.keys():
            query = query.filter(Branch.id == params['id'])
        if "city" in params.keys():
            query = query.filter(Branch.city == params['city'])
        if "postcode" in params.keys():
            query = query.filter(Branch.id == params['postcode'])
        return query.first()

    def get_assigned_cars_count(self, id):
        query = db.session.query(Car.id)
        query = query.filter(Car.assigned_type == 2)
        query = query.filter(Car.assigned_id == id)
        return query.count()

    def serialize(self):
        return {
            "id": self.id,
            "city": self.city,
            "postcode": self.postcode,
            "capacity": self.capacity
        }


class Driver(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    def __init__(self, first_name, middle_name, last_name, dob):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = dob

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get(params):
        query = db.session.query(Driver)
        if "id" in params.keys():
            query = query.filter(Driver.id == params['id'])
        if "first_name" in params.keys():
            query = query.filter(Driver.first_name == params['first_name'])
        if "middle_name" in params.keys():
            query = query.filter(Driver.middle_name == params['middle_name'])
        if "last_name" in params.keys():
            query = query.filter(Driver.last_name == params['last_name'])
        if "dob" in params.keys():
            query = query.filter(Driver.dob == params['dob'])
        return query.first()

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "dob": self.dob.strftime("%d/%m/%Y")
        }