# Python Backend Challenge
This app was built as a part of Python backend challenge using Flask and postgresql. It is a service that lets you perform CRUD operations on Car, Drivers and Branch records. 
## Task
Please see README_old.md
## Attempted levels
- Novice
- Expert
# API Documentation
## Car
Represents possible operations (CRUD at the moment) to the Car records in the database. Can be assigned a Branch or Driver record during /car/create or via /car/update. Can assign Car to Driver or Branch. Branch record must exist and Branch must not exceed its capacity.
### Methods
#### POST /car/create
Creates a car object record and saves it to database.
##### Request Type
- Method: POST
- Content-type: application/json
##### Parameters
###### make
- required
- string
- length 100
- Represents car make
- Example: BMW, Mercedes, Lotus
###### model
- required
- string
- length 100
- Represents car make
- Example: Model 3, 525d, C65AMG
###### year
- required
- int
- length 100
- Represents car year
- Example: 1999, 2015, 2019
###### assigned_type
- required
- int
- Driver: 1, Branch: 2
- Represents type of assigned entity
- Example: 1, 2
###### assigned_id
- required
- int
- Represents id of assigned entity
- Example: 7, 123, 15
#### Response codes
- 400 : Invalid Request, Missing Parameters
- 201 : Car created
#### GET /car/get
Gets a car record based on supplied parameters. Returns first car that matches parameters. Returns car not found in case no cars were found.
##### Request Type
- Method: GET
- Content-type: application/json
- Returns JSON
##### Parameters
###### id
- optional
- int
- Represents id of a car in a database table
- Example: 1, 25, 1234
###### make
- optional
- string
- length 100
- Represents car make
- Example: BMW, Mercedes, Lotus
###### model
- optional
- string
- length 100
- Represents car make
- Example: Model 3, 525d, C65AMG
###### year
- optional
- int
- length 100
- Represents car year
- Example: 1999, 2015, 2019
###### assigned_type
- optional
- int
- Driver: 1, Branch: 2
- Represents type of assigned entity
- Example: 1, 2
###### assigned_id
- optional
- int
- Represents id of assigned entity
- Example: 7, 123, 15
#### Response codes
- 400 : Invalid request, Invalid parameters
- 404 : Car Not Found
- 200 : OK

#### PUT /car/update
Updates existing car record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
###### id
- required
- int
- Represents id of a record in a table you wish to update
###### make
- optional
- string
- length 100
- Represents car make
- Example: BMW, Mercedes, Lotus
###### model
- optional
- string
- length 100
- Represents car make
- Example: Model 3, 525d, C65AMG
###### year
- optional
- int
- length 100
- Represents car year
- Example: 1999, 2015, 2019
###### assigned_type
- optional
- int
- Driver: 1, Branch: 2
- Represents type of assigned entity
- Example: 1, 2
###### assigned_id
- optional
- int
- Represents id of assigned entity
- Example: 7, 123, 15
#### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Car not found
- 200 : Car record was updated

#### DELETE /car/delete
Deletes existing car record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
###### id
- required
- int
- Represents id of a record in a table you wish to update
#### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Car not found
- 200 : Car deleted

## Branch
### Methods
#### POST /branch/create
Creates a branch object and saves it to database.
##### Request Type
- Method: POST
- Content-type: application/json
##### Parameters
###### city
- required
- string
- length 60
- Represents city in which Branch is based
- Example: London, Glasgow, Cardiff
###### postcode
- required
- string
- length 8
- Represents UK-style postcode of a branch
- Example: E1W 3SS, GU27NQ, W6 8AB
###### capacity
- required
- int
- length 2147483647
- Represents capacity of a branch
- Example: 10, 25, 100
#### GET /branch/get
#### PUT /branch/update
#### DELETE /branch/delete

## Driver
### Methods
#### POST /driver/create
#### GET /driver/get
#### PUT /driver/update
#### DELETE /driver/delete

# Installation
## Update repo's
- sudo apt-get update
## Install Python
- sudo apt-get install python3
- sudo apt-get install python3-pip
- sudo pip install virtualenv
## PostgreSQL
- sudo apt-get install postgresql
## psycopg2 - PostgreSQL wrapper for Flask
- sudo apt-get install python-psycopg2
## libpq - postgresql interface
- sudo apt-get install libp
## Python3 dependencies
- sudo python3 install flask flask-sqlalchemy psycopg2 flask-migrate flask-script

# PostgreSQL Setup
## Set Up User
## Create Database
## Migrate Database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade 

# Running the app
source environment.env + flask run

