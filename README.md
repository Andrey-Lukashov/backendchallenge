# Python Backend Challenge
This app was built as a part of Python backend challenge using Flask and postgresql. It is a service that lets you perform CRUD operations on Car, Drivers and Branch records.  
This document contains API documentation and Local Installation Instructions at the bottom. 
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

# Local Installation Instructions
To install and run this REST service locally you will need to install Ubuntu 18.04 OS, set up python and dependencies as well as set up postgresql and user for it. The plan is to get the code from this repo, create virtual environment with Python3 and then run the necesssary services in order to get REST service up locally.

**PLEASE NOTE**: This instruction is an example of a setup. It is NOT RECOMMENDED to use this in production as I have not added instructions for how to safeguard the server. This is NOT the best practice. 
## Clean Machine
### Install Ubuntu 18.04
Download and install a clean Ubuntu 18.04 (latest stable version):  
During the installation:
- Set up username: flaskapi
- Set up password: 123456789

Once you login to your new Ubuntu - run software updater and update to the latest version. 

### Setup Git
GitHub has provided us with a great instructions here: [Set up Git | GitHub Help](https://help.github.com/en/articles/set-up-git)
### Get Source Code
Create a sites directory and clone backendchallenge into it.  
- Open terminal and run following commands
- mkdir sites
- cd sites
- git clone git@github.com:Andrey-Lukashov/backendchallenge.git
- cd  backendchallenge 

## Install Necessary Modules and Dependencies
**Install Python Dependencies** 
- sudo apt-get update
- sudo apt-get install python3 python3-pip virtualenv

**Create Virtual Environment**
-  virtualenv --python=python3 venv

**Activate Virtual Environment**
- source environment.env 

**Install PostgreSQL and Python modules for it**
- sudo apt-get install postgresql 
- sudo apt-get install python-psycopg2
- sudo apt-get install libpq-dev

**Install Flask and necessary dependencies**
- pip3 install psycopg2 
- pip3 install flask flask-sqlalchemy flask_migrate flask_script flask_api

# PostgreSQL Setup
## Set Up User
- sudo -u postgres createuser flaskapi

## Create Database
- sudo -u postgres createdb flask_api

## Change User Password
- psql
- \password  
- 123456
- 123456
- \q

## Migrate Database
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade 

# Running the app
- flask run  

You should be able to see following if everything was installed successfully:
 * Serving Flask app "run.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# Import Test Data
## Install curl
- sudo apt install curl
## Populate Tables 
### Driver 
- curl -d '{"first_name":"John", "middle_name":"Gavin", "last_name":"Malkovich", "dob":"09/12/1953"}' -H "Content-Type: application/json" -X POST http://localhost:5000/driver/create
- curl -d '{"first_name":"James", "middle_name":"Eugene", "last_name":"Carrey", "dob":"09/12/1953"}' -H "Content-Type: application/json" -X POST http://localhost:5000/driver/create

For both requests you should get this response: {"message":"Driver created","status_code":201}
### Branch 
- curl -d '{"city":"Wokingham", "postcode":"RG40 2AP", "capacity":2}' -H "Content-Type: application/json" -X POST http://localhost:5000/branch/create

Response should be: {"message":"Branch created","status_code":201}

### Car
Assigned to drivers:
- curl -d '{"make":"BMW", "model":"530d", "year":"2014", "assigned_type":1, "assigned_id":1}' -H "Content-Type: application/json" -X POST http://localhost:5000/car/create
- curl -d '{"make":"Toyota", "model":"Prius", "year":2015, "assigned_type":1, "assigned_id":2}' -H "Content-Type: application/json" -X POST http://localhost:5000/car/create

Assigned to branch:
- curl -d '{"make":"Tesla", "model":"Model S", "year":2019, "assigned_type":2, "assigned_id":1}' -H "Content-Type: application/json" -X POST http://localhost:5000/car/create
- curl -d '{"make":"Tesla", "model":"Model X", "year":2018, "assigned_type":2, "assigned_id":1}' -H "Content-Type: application/json" -X POST http://localhost:5000/car/create

## Bonus: check db for population
- psql 
- \c flask_api
- \d 
-  SELECT * FROM branch;
-  SELECT * FROM driver;
-  SELECT * FROM car;
- \q

## Flask Logs
Your flask logs should look like that if successfully used curl to populate data:
- 127.0.0.1 - - [16/Aug/2019 02:40:49] "POST /driver/create HTTP/1.1" 200 -
- 127.0.0.1 - - [16/Aug/2019 02:41:25] "POST /driver/create HTTP/1.1" 200 -
- 127.0.0.1 - - [16/Aug/2019 02:45:40] "POST /branch/create HTTP/1.1" 200 -
- 127.0.0.1 - - [16/Aug/2019 02:49:18] "POST /car/create HTTP/1.1" 200 -
- 127.0.0.1 - - [16/Aug/2019 02:49:44] "POST /car/create HTTP/1.1" 200 -
- 127.0.0.1 - - [16/Aug/2019 02:50:04] "POST /car/create HTTP/1.1" 200 -
- 127.0.0.1 - - [16/Aug/2019 02:50:20] "POST /car/create HTTP/1.1" 200 -

# Testing
Simply run this command:
- python tests.py