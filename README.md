# Introduction
This is a project includes scalable user service and URL shorten service using python flask.
The user service is responsible for maintaining user information and request authentication using JWT.
The strategy of generating shorten URL is by leveraging auto-increment primary key in MYSQL DB and implementing Shuffled Hashing Algorithm to 
hash id into alphabets.(In the project, for readability the default alphabets are 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890').
The project support multiple users access with DB pre-checking and unique key constraint on column long_url.
The length of shorten url ranges in [1, 6].

# Guidance of starting the project

## Start the services

First, we need to make the docker engine running.

Then go to the directory of the project: `$cd /flasker_url_shortener`

Then execute `docker-compose up` to initialize and start the whole project.

Since we put the whole project inside a container, the whole services, including backend and DB are all running now.

We use Nginx to wrap those 2 services, so we can reach it by one endpoint.

The service is now running at http://127.0.0.1:80/

## Check running

You can execute the test program to check if it's running normally (please note the port is 80).

Also, if you want to use postman to test the APIs, just follow the input and endpoints in the assignment guidance. If you want to access the URL services, please login first and then include the JWT in the header.

# Structure of the project
```
└── flasker_url_shortener
    ├── shortener/                      # URL service
    │   ├── controller/                 # APIs
    │   |   └── url_controller.py         
    │   ├── models/                     # Database Model
    │   |   └── url.py
    │   ├── srvices/                    # Implemetation of Services
    │   |   ├── id_hashing.py           # Hashing
    │   |   └── url_services.py         # Database Query/Edit
    │   ├── app.py                      # Entry of this Application
    │   ├── appconfig.py                # Configuration of APP
    │   ├── dbconfig.yaml               
    │   ├── Dockerfile                  # File for building up the docker for this service
    │   └── requirements.txt            # Required pip packages of this service   
    ├── services/                       # User service
    │   ├── controller/                 # APIs
    │   |   └── user_controller.py         
    │   ├── models/                     # Database Model
    │   |   └── user.py
    │   ├── srvices/                    # Implemetation of Services
    │   |   ├── self_md5.py             # Hashing
    │   |   ├── jwt_service.py          # Generate/Encode/Decode the JWT
    │   |   └── user_services.py        # Database Query/Edit
    │   ├── app.py                      # Entry of this Application
    │   ├── appconfig.py                # Configuration of APP
    │   ├── dbconfig.yaml               
    │   ├── Dockerfile                  # File for building up the docker for this service
    │   └── requirements.txt            # Required pip packages of this service   
    ├── db/               
    │   ├── init_scripts/               
    │   |   └── demo.sql                # Initialization of DB
    │   └── docker_compose.yaml         # Setup the DB
    ├── nginx/               
    │   └── default.conf/               # The configuration of Nginx         
    ├── README.md            
    └── .gitignore   
```
