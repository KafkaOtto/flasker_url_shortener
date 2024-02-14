# Guidance of start the project

First, we need to make the docker engine running.

Then go to the directory of DB: `$cd flasker_url_shortener/db`


Then execute `docker-compose up` to initialize and start the DB.

This should start the database. The DB is now running at port 3306, make sure the port is not occupied.

Then, please go to the app directory. `$cd ../app`

And install the dependencies of the project. `$pip install -r requirements.txt`

Now you can start the service by executing: `$python /app.py`

The service is running at 127.0.0.1:8000

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
    │   ├── dbconfig.py                 # Configuration of DB
    │   ├── dbconfig.yaml        
    │   └── requirements.txt            # Requirements of the Project       
    ├── db/               
    │   ├── init_scripts/               
    │   |   └── demo.sql                # Initialization of DB
    │   └── docker_compose.yaml         # Setup the DB
    ├── README.md            
    └── .gitignore   
```
