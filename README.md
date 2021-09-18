# PhotoLair

An Image marketplace web app where users gain credits by selling images or acquire images by spending credits.

When selling an image, a user will need to provide a title, price 
and inventory (i.e. number of allowed downloads) for their image. To purchase an image,
a user must have enough credits and the desired image must be in stock.
By default, all new users start with 50 credits which can immediately be used
to purchase images on the marketplace. User's gain credits on the marketplace
when their images are sold. Once an image is sold out it is removed from the marketplace.
An account is required to purchase/sell images, though anyone can view the available images on the
marketplace. The application uses simple token based authentication thus reducing the number
of times a user has to provide their login credentials.

This project is currently hosted at: Soon to be hosted...

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
This section is intended to familiarize readers new to Django on how it works and the overall directory structure. It relates the working of Django with this project to help make the overall implementation clear.

### What is Django?
Django is a backend framework written in Python that implements a variation of the Model View Controller (MVC) design pattern called Model View Template (MVT). The **Model** portion handles the database, **Template** handles User Interface and the **View** is used to implement the business logic and endpoints. In Django there is no separate controller, the application is completely handled by the relevant view. 


![Django-MVT](https://imgur.com/CRVbSnC.png)
<br/>
Reference: https://djangobook.com/mdj2-django-structure/

### Django Project Structure
A Django web application is a self-contained package constructed from a number of what Django likes to call 'apps' that each provide a specific utility to the overall application. For this project, we have the high-level directory known as **core**  that provides application wide settings, integration of Django and third-party apps along with any database or external resource (i.e. S3 bucket) configurations. 

As for the Django apps developed for this project, we have **photolair** and **photolair_api** that each provide a specific utility. The **photolair** app provides the models for the application along with any special utilities and Django Signals needed to operate on the models. On the other hand, the **photolair_api** app utilizes the Django Rest Framework to implement the web api (i.e. **views**). The section below provides the overall directory of the project and labels key folders with what they contain.

![Django-Struct](https://djangobook.com/wp-content/uploads/structure_drawing1_new.png)
<br/>
Reference: https://djangobook.com/mdj2-django-structure/


### Django Project Structure
```
├── core                <= Project folder with application wide settings and integrations 
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── storage_backends.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── photolair          <= Django App for Models
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── managers       <= Manager for creating custom user model instances
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── user_manager.py
│   ├── migrations
│   ├── models          <= Models for the project
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── images.py
│   │   └── users.py
│   ├── signals        <= Signals for pre/post modification of DB instances
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── image_signals.py
│   └── utilities      <= Utility functions for creation/modification of DB instances
│       ├── __init__.py
│       ├── __pycache__
│       └── image_utilities.py
└── photolair_api     <= Django App for View Logic (i.e. implements API)
    ├── __init__.py
    ├── __pycache__
    ├── apps.py
    ├── migrations
    ├── permissions   <= Permissions required for objects returned from endpoints
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── image_permissions.py
    │   └── user_permissions.py
    ├── serializers   <= Serializers convert model instance to Python datatypes that are then rendered into JSON
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── image_serializers.py
    │   └── user_serializers.py
    ├── services      <= Provides services for endpoints that need to perform complex operatons on DB instances
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── image_services.py
    ├── urls.py
    └── views        <= Implements the API endpoints and any custom logic/settings 
        ├── __init__.py
        ├── __pycache__
        ├── image_views.py
        ├── token_views.py
        └── user_views.py
```

## Development
### Prerequisites
To run this application you'll need:
- Python 3.7 or higher
- Node.js & npm installed 
- A local installation of [PostgreSQL](https://www.postgresql.org/download/)
- A PostgreSQL database instance titled ```photolair``` or another database name can be chosen by modifying the database settings in ```core/core/settings.py```
   > ### Note
   >
   > If you have brew, install PostgreSQL with the following steps:
   >
   > -  `brew install postgresql` to install PostgreSQL
   > -  `brew services start postgresql` to start the PostgreSQL service (stop it with `brew services stop PostgreSQL`)
- The backend is capable of implementing the image marketplace either using local file storage or an S3 bucket. To use the S3 bucket you will need to create an AWS account, set up a S3 bucket with ```block all public access``` unchchecked and a user assigned to the bucket with full access. You will then need a .env file with the following parameters filled out and placed in the projects core/core folder.
   > - AWS_S3=TRUE
   > - AWS_ACCESS_KEY_ID= <users_access_key>
   > - AWS_SECRET_ACCESS_KEY=<users_secret_access_key>
   > - AWS_STORAGE_BUCKET_NAME=<s3_bucket_name>

### Getting Started
In order to run the backend and/or the frontend locally follow the instructions below.

Begin by cloning the repository
```
https://github.com/harmanT23/PhotoLair.git
```

#### Django Backend

Set up a virtual environment for development. Install virtualenv.
```
pip install virtualenv
```

Change directory to the project folder
```
cd PhotoLair
```

Create a virtual environment
```
virtualenv venv
```

Activate the virtual environment
```
source venv/bin/activate
```

Install python dependencies on the virtual environment
```
pip install -r requirements.txt
```

Change directory to core folder of backend
```
cd core
```

Start the backend
```
python manage.py runserver
```

#### React Frontend

Change directory to client directory from project directory
```
cd client
```

Install all frontend dependencies
```
npm install
```

Start frontend
```
npm start
```

## PhotoLair API
The application provides an API for authentication, user accounts and images.
The following endpoints are currently implemented:

### Authentication Endpoints
- ```POST /api/token/``` - Takes the username and password of a user and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
- ```POST /api/token/refresh/``` - Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
- ```POST /api/token/blacklist/``` - Used to blacklist refresh tokens after a user logs out.

### User Endpoints
- ```POST /api/users/``` - Register a new user with username and password.
- ```GET /api/users/me/``` - Get details about the currently authenticated user
- ```GET /api/users/{id}/``` - Get details about a specific user
- ```PATCH /api/users/{id}/``` - Update a specific user's details
- ```DELETE /api/users/{id}/``` - Delete a specific user's details 

### Image Endpoints
- ```GET /api/images/``` - Get all images on the marketplace (used to display a gallery on the homepage)
- ```POST /api/images/``` - Upload a image to sell on the marketplace by providing a title, price, inventory and image.
- ```GET /api/images/{image_id}/``` - Download the specified image, this endpoint will transfer the required amount of credits from the authenticated user 
to the user who posted the image as well as update the inventory of the image.
- ```PATCH /api/images/{image_id}``` - Update details of the image such as its title, price and inventory as well as the option to replace the image itself
- ```DEL /api/images/{image_id}``` - Delete the specified image

## Contributing
1. [Fork it](https://github.com/harmanT23/PhotoLair/fork)
2. Create your feature branch i.e. ```git checkout -b feature/foo```
3. Commit your changes i.e. ```git commit -am 'Add some foo'```
4. Push to branch i.e. ```git push origin feature/foo```
5. Create a new Pull Request

## Authors
[Harman Tatla](https://github.com/harmanT23) - Project Developer

