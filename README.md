# PhotoLair

An Image marketplace web app where users gain credits by selling images and 
acquire images by spending credits.

When selling an image, a user will need to provide a title, price and inventory 
(i.e. number of allowed downloads) for their image. To purchase an image,
a user must have enough credits and the desired image must be in stock.
By default, all new users start with 50 credits which can immediately be used
to purchase images on the marketplace. User's gain credits on the marketplace
when their images are sold. Once an image is sold out it is removed from the 
marketplace. An account is required to purchase and sell images, though anyone 
can view the available images on the marketplace. For authentication the 
application uses JSON Web Tokens (JWT) for authentication.

This project is currently hosted at: https://photolair.herokuapp.com/

## Screenshots 
![Homepage](https://imgur.com/DTNSr5b.jpeg)
![Sell-Page](https://imgur.com/JJ98a0I.jpeg)
![Login](https://imgur.com/xsEEFcw.jpeg)

## Built With
### Stack Used
- [React](https://reactjs.org/) - Framework used to design the frontend UI
- [Django](https://www.djangoproject.com/) - Backend Web Application Framework
- [PostgreSQL](https://www.postgresql.org/) - Databased used to store data
- [Node.js](https://nodejs.org/en/) - JavaScript run-time environment 

### Libraries and Services:
- [Django Rest Framework](https://www.django-rest-framework.org/) - Toolkit for building WEB APIs
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Provides a JSON Web Token authentication backend for the Django REST Framework
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK to configure S3 storage 

## About Django
This section provides a short over view to familiarize readers new to Django 
on how it works and the overall directory structure.

### What is Django?
Django is a backend framework written in Python that implements a variation of 
the **Model View Controller** (MVC) design pattern called 
**Model View Template** (MVT). The **Model** portion handles the database, 
**Template** handles User Interface and the **View** is used to implement 
the business logic and endpoints. In Django there is no separate controller, 
the application is completely handled by the relevant view. 


![Django-MVT](https://imgur.com/Vh26kdQ.png)
<br/>
Reference: https://djangobook.com/mdj2-django-structure/

### Django Project Structure
A Django web application is a self-contained package constructed from a number 
of what Django likes to call 'apps' that each provide a specific utility to the
overall application. 

Regarding the Django apps developed for this project, we have **photolair** and 
**photolair_api** that each provide a specific utility: 
- **photolair** app provides the models for the application along with any 
special helpers functions and Django Signals needed to operate on the models.
- **photolair_api** app utilizes the Django Rest Framework to defines the views 
needed for the endpoints, serializers to convert between JSON and model 
datatypes as well as any services needed to support the endpoints.

## Development
### Prerequisites
To run this application you'll need:
- Python 3.9.7 or higher
- NPM 7.21.0 or higher
- Node.js & npm installed 
- A local installation of [PostgreSQL](https://www.postgresql.org/download/)
- A PostgreSQL database instance titled ```photolair``` or another database 
name can be chosen by modifying the database settings in 
```core/core/settings.py```
   > ### Note
   >
   > If you have brew, install PostgreSQL with the following steps:
   >
   > -  `brew install postgresql` to install PostgreSQL
   > -  `brew services start postgresql` to start the PostgreSQL service 
   (stop it with `brew services stop PostgreSQL`)

#### [Optional] Using AWS S3 Bucket for Image Repository
By default the Photolair app will work right out the box and use the local
file storage to implement the image repository. If the user prefers, the app 
also supports connecting to an S3 bucket to store the image repo. To do so
follow the steps below:
- Create an AWS account
- Create a [public S3 bucket](https://havecamerawilltravel.com/photographer/how-allow-public-access-amazon-bucket/) 
with ```block all public access``` unchecked
- Assign a user to the newly created bucket with full S3 access
- Create an ```.env``` file with the following parameters filled out and 
placed in the projects ```core/core``` folder.
   > - AWS_S3=TRUE
   > - AWS_ACCESS_KEY_ID= <users_access_key>
   > - AWS_SECRET_ACCESS_KEY=<users_secret_access_key>
   > - AWS_STORAGE_BUCKET_NAME=<s3_bucket_name>

### Getting Started
In order to run the backend and/or the frontend locally follow the instructions 
below.

- Begin by cloning the repository 
```git clone https://github.com/harmanT23/PhotoLair.git```


#### Start Django Backend

- Install virtualenv: ```pip install virtualenv```
- Change directory to the project folder: ```cd PhotoLair```
- Create a virtual environment: ```virtualenv venv```
- Activate the virtual environment: ```source venv/bin/activate```
- Install python dependencies: ```pip install -r requirements.txt```
- Change directory to core: ```cd core```
- Make Migrations: ```./manage.py makemigrations```
- Apply DB migrations: ```./manage.py migrate```
- Runserver: ```./manage.py runserver```
#### Start React Frontend
- Change directory to client folder:  ```cd client```
- Install dependencies: ```npm install```
- Start frontend: ```npm start```

## Testing
Testing is split into two parts:
- Testing Models
- Testing API

### Testing Models
Detailed units tests for the models are available ```./core/photolair/tests```

To run all the unit tests at once simply run the following command in 
the ```./core``` folder
```
 ./manage.py test
```
### Testing API
Complete API testing of all the endpoints are provided in the postman collection available in ```./core/postman_collection```

Instruction for importing a postman collection are available [here](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman)
## PhotoLair API
The application provides an API for authentication, user accounts and images.
The following endpoints are currently implemented:

### Authentication Endpoints
- ```POST /api/token/``` - Takes the username and password of a user then 
returns an access and refresh JSON web token pair to prove the authentication 
of those credentials.
- ```POST /api/token/refresh/``` - Takes a refresh type JSON web token and 
returns an access type JSON web token if the refresh token is valid.
- ```POST /api/token/blacklist/``` - Used to blacklist refresh tokens 
after a user logs out.

### User Endpoints
- ```POST /api/users/``` - Register a new user with username and password.
- ```GET /api/users/me/``` - Get details about the currently authenticated user
- ```GET /api/users/{id}/``` - Get details about a specific user
- ```PATCH /api/users/{id}/``` - Update a specific user's details
- ```DELETE /api/users/{id}/``` - Delete a specific user's details 

### Image Endpoints
- ```GET /api/images/``` - Get all images on the marketplace 
(used to display a gallery on the homepage)
- ```POST /api/images/``` - Upload an image to sell on the marketplace by 
providing a title, price, inventory and image.
- ```GET /api/images/{image_id}/``` - Download the specified image, this 
endpoint will transfer the required amount of credits from the authenticated 
user to the user who posted the image as well as update the inventory of the 
image.
- ```PATCH /api/images/{image_id}``` - Update details of the image such as its 
title, price and inventory as well as the option to replace the image itself
- ```DEL /api/images/{image_id}``` - Delete the specified image

## Future Improvements 
- Transaction logs to record transactions made by a user. Use these
logs to notify a user when they attempt to buy the same image again or to
provide them insights about their recent purchase trends.
- Image tags to allow users to browse images matching certain search
criteria.
- Search and filters to allow users to search by keywords or filter
images by various parameters (i.e. location, date, author, etc).

## Contributing
1. [Fork it](https://github.com/harmanT23/PhotoLair/fork)
2. Create your feature branch i.e. ```git checkout -b feature/foo```
3. Commit your changes i.e. ```git commit -am 'Add some foo'```
4. Push to branch i.e. ```git push origin feature/foo```
5. Create a new Pull Request

## Authors
[Harman Tatla](https://github.com/harmanT23) - Project Developer

