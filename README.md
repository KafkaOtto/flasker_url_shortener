# Introduction
This is a project implementing scalable URL shorten service using python flask. The strategy of generating
shorten URL is by leveraging auto-increment primary key in MYSQL DB and implementing Shuffled Hashing Algorithm to 
hash id into alphabets.(In the project, for readability the default alphabets are 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890').
The project support multiple users access with DB pre-checking and unique key constraint on column long_url.
The length of shorten url ranges in [1, 6].

# Guidance of starting the project

## Database

First, we need to make the docker engine running.

Then go to the directory of DB: `$cd flasker_url_shortener/db`


Then execute `docker-compose up` to initialize and start the DB.

This should start the database. The DB is now running at port 3306, make sure the port is not occupied.

## Backend service

Then, please go to the app directory. `$cd ../app`

And install the dependencies of the project. `$pip install -r requirements.txt`

Now you can start the service by executing: `$python /app.py`

The service is running at 127.0.0.1:8000

## Check running

You can execute the test program to check if it's running normally.

Or directly visit http://127.0.0.1:8000/, it should return the result of get_all_urls(). In this case, it should contain 3 records that we put in the DB during the initialization.



# Structure of the project
```
└── flasker_url_shortener
    ├── app/                            # application
    │   ├── controller/                 # APIs
    │   |   └── user_controller.py         
    │   ├── models/                     # Database Model
    │   |   └── url.py
    │   ├── srvices/                    # Implemetation of Services
    │   |   ├── id_hashing.py           # Hashing
    │   |   └── url_services.py         # Database Query/Edit
    │   ├── app.py                      # Entry of Application
    │   ├── appconfig.py                 # Configuration of APP(db and secret key for hashing algorithm)
    │   ├── dbconfig.yaml        
    │   └── requirements.txt            # Required pip packages of the Project       
    ├── db/               
    │   ├── init_scripts/               
    │   |   └── demo.sql                # Initialization of DB
    │   └── docker_compose.yaml         # Setup the DB
    ├── README.md            
    └── .gitignore   
```
