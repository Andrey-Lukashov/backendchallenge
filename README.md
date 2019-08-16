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
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| make | Yes | String | 100  | BMW
| model | Yes | String | 100 | 525d 
| year | Yes | Int | Int Max Size | 2019  
| assigned_type | Yes | Int | Int Max Size | 1
| assigned_id | Yes | Int | Int Max Size | 2 
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 201 : Car created
#### GET /car/get
Gets a car record based on supplied parameters. Returns first car that matches parameters. Returns car not found message with status 404 in case no cars were found.
##### Request Type
- Method: GET
- Content-type: application/json
- Returns JSON
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | No | Int | Int Max Size | 1
| make | No | String | 100  | BMW
| model | No | String | 100 | 525d 
| year | No | Int | Int Max Size | 2019  
| assigned_type | No | Int | Int Max Size | 1
| assigned_id | No | Int | Int Max Size | 2 
##### Response codes
- 400 : Invalid request, Invalid parameters
- 404 : Car Not Found
- 200 : OK

#### PUT /car/update
Updates existing car record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | Yes | Int | Int Max Size | 1
| make | No | String | 100  | BMW
| model | No | String | 100 | 525d 
| year | No | Int | Int Max Size | 2019  
| assigned_type | No | Int | Int Max Size | 1
| assigned_id | No | Int | Int Max Size | 2 
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Car not found
- 200 : Car record was updated

#### DELETE /car/delete
Deletes existing car record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | Yes | Int | Int Max Size | 1
##### Response codes
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
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| city | Yes | String | 60 | London |
| postcode | Yes | String | 6 | SW15 1RB | 
| capacity | Yes | Int | Int Max Size | 125
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 201 : Branch created

#### GET /branch/get
Gets a branch record based on supplied parameters. Returns first branch that matches parameters. Returns branch not found message with status 404 in case no branches were found.
##### Request Type
- Method: GET
- Content-type: application/json
- Returns JSON
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | No | Int | Int Max Size | 42 | 
| city | No | String | 60 | London |
| postcode | No | String | 6 | SW15 1RB | 
| capacity | No | Int | Int Max Size | 125
##### Response codes
- 400 : Invalid request, Invalid parameters
- 404 : Branch not found
- 200 : OK

#### PUT /branch/update
Updates existing branch record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | Yes | Int | Int Max Size | 42 | 
| city | No | String | 60 | London |
| postcode | No | String | 6 | SW15 1RB | 
| capacity | No | Int | Int Max Size | 125
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Branch not found
- 200 : Branch record was updated

#### DELETE /branch/delete
Deletes existing branch record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | Yes | Int | Int Max Size | 42 | 
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Branch not found
- 200 : Branch deleted

## Driver
### Methods
#### POST /driver/create
Creates a driver object and saves it to database.
##### Request Type
- Method: POST
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| first_name | Yes | String | 100 | John |
| middle_name | No | String | 100 | Gavin |
| last_name | Yes | String | 100 | Malkovich |
| dob | Yes | String | 6 | 09/12/1953 | 
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 201 : Driver created

#### GET /driver/get
Gets a driver record based on supplied parameters. Returns first driver that matches parameters. Returns driver not found message with status 404 in case no drivers were found.
##### Request Type
- Method: GET
- Content-type: application/json
- Returns JSON
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | No | Int | Int Max Size | 42 | 
| first_name | No | String | 100 | John |
| middle_name | No | String | 100 | Gavin |
| last_name | No | String | 100 | Malkovich |
| dob | No | String | 6 | 09/12/1953 | 
##### Response codes
- 400 : Invalid request, Invalid parameters
- 404 : Driver not found
- 200 : OK

#### PUT /driver/update
Updates existing driver record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | Yes | Int | Int Max Size | 42 | 
| first_name | No | String | 100 | John |
| middle_name | No | String | 100 | Gavin |
| last_name | No | String | 100 | Malkovich |
| dob | No | String | 6 | 09/12/1953 | 
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Driver not found
- 200 : Driver record was updated

#### DELETE /driver/delete
Deletes existing driver record. Finds the record to update based on id
##### Request Type
- Method: PUT
- Content-type: application/json
##### Parameters
| Param Name        | Required           | Type | Length | Example | 
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| id | Yes | Int | Int Max Size | 42 | 
##### Response codes
- 400 : Invalid Request, Missing Parameters
- 404 : Driver not found
- 200 : Driver deleted

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

