# Bucketlist_v2
Django Bucketlist Api is an API built in django. It is a bucketlist API that demonstrates CRUD operations. 

# Installation

1. Clone the repository with the url. `https://github.com/andela-amutava/Bucketlist.git`

2. Install requirements to your virtual environment using the command. `pip install -r requirements.txt`

3. Install docker and ensure it's running before you run the application.

4. Run the command 'docker compose up'. This will run the application on the port specified in the docker-compose.yml file.

5. If you have the app running you are good to go.


# How to test the API.

1. Download postman.
2. Hit the api in the below endpoints. Make sure you choose the appropriate methods.

## API Endpoints

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
|  `/get-token` | `POST` | Login and retrieve token|
| `/bucketlists` | `POST` | Create a new Bucketlist |
| `/bucketlists` | `GET` | Retrieve all bucketlists for user |
| `/bucketlists/<id>` | `GET` |  Retrieve bucketlist details |
| `/bucketlists/<id>` | `PUT` | Update bucket list details |
| `/bucketlists/<id>` | `DELETE` | Delete a bucket list |
| `/bucketlists/<id>/items` | `POST` |  Create items in a bucket list |
| `/bucketlists/<id>/items/<item_id>` | `DELETE`| Delete a item in a bucket list|
| `/bucketlists/<id>/items/<item_id>` | `PUT`| update a bucket list item details|

Note that login is handled by django superuser.