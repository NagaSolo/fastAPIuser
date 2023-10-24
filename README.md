# AHAM Assessment (User Management With FastAPI)


## Assessment Requirements
- User entity:
    - FirstName
    - LastName
    - EmailAddress
    - PhoneAddress
    - Address

- Tech stack
    - Python3.x
    - any Python web framework and library of choice (e.g., Flask, Django, FastAPI, etc.).
    - The candidate should also use a database (e.g., SQLite, MySQL, PostgreSQL, etc.) to store the customer records. 

- The candidate should create endpoints for the following operations:
    - Create a new customer record
    - Retrieve a customer record by ID 
    - Update a customer record by ID 
    - Delete a customer record by ID


## Decision
- Divide entity into User and Address to normalize data:
    - User entity:
        - FirstName
        - LastName
        - EmailAddress
        - Phone
        - is_superuser
        - is_active
    - Address entity:
        - Line
        - Postcode
        - City
        - State

- Postgres as data storage solution
- Naturally, pgAdmin will be used as graphical intermediary medium with postgres db
- Docker (compose) as development environment


## Setup & Run 🏃‍♂️

To set this up:

If you don't have one yet, set up a .env file with your configuration. For a basic version for local testing use:  
```bash
cp .env-template .env
```

Then build and start the test/debug stack with:
```bash
docker-compose up -d
```

Then:
- (Web Application) Visit http://localhost:4000/docs for the interactive API docs (Swagger). Authenticate first with super-username and password to available at your defined **.env** file.

- Run pytest in your container with `docker exec fastapi-app bash ./test.sh [optional parameters]`

- (PgAdmin) Visit http://localhost:5050/ for the PostgreSQL administrator. Upon first use you'll need to register your DB server using your **.env** file.
    - server name: `db`
    - connection/hostname: `user_db`
    - connection/user: `postgres`
    - connection/password: `passwordfromdotenv`


## Reference:
- This is based on fastAPI backend scaffold available at: https://github.com/bibektimilsina000/FastAPI-PgStarterKit by bibektimilsina000

- This scaffold allow fast development and offer some twelve factor app

- Changes have been made to accomodate requirements stated by the assessment.