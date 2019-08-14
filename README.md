# REST API
This app was built as a part of Python backend challenge using Flask and postgresql. It is a service that 
# Documentation
## Car
### Methods
#### POST /car/create
Creates a car object and saves it to database.
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
Gets a car object based on supplied parameters. Returns first car that matches parameters. Returns car not found in case no cars were found.
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
#### DELETE /car/delete
#### POST /car/assign

## Branch
### Methods
#### POST /branch/create
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
sudo apt-get update
## PostgreSQL
sudo apt-get install postgresql
## psycopg2 - PostgreSQL wrapper for Flask
sudo apt-get install python-psycopg2
## libpq - postgresql interface
sudo apt-get install libp
## Python3 dependencies
flask flask-sqlalchemy psycopg2 flask-migrate flask-script

# PostgreSQL Setup
## Set Up User
## Create Database
## Migrate Database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade 

# Running the app
source environment.env + flask run

