# PhotoLair

An image marketplace where users can sell their images for credits and spend credits
on downloading other user's images.

When selling an image, a user will need to provide a title, price 
and inventory (i.e. number of allowed downloads) for their image. To purchase an image,
a user must have enough credits and the desired image must be in stock.
By default, all new users start with 50 credits which can immediately be used
to purchase images on the marketplace. User's gain credits on the marketplace
when their images are bought. Once an image is sold out it is removed from the marketplace.
An account is required to purchase/sell images, though anyone can view the images on the
marketplace. The application uses simple token based authentication thus reducing the number
of times a user has to provide their credentials.

This project is currently hosted at: Soon to be hosted...

## Screenshots 
To be added...

## Built With
### Stack Used
- [React](https://reactjs.org/) - Framework used to design the front-end UI
- [Django](https://www.djangoproject.com/) - Back-end Web Application Framework
- [PostgreSQL](https://www.postgresql.org/) - Databased used to store data
- [Node.js](https://nodejs.org/en/) - JavaScript run-time environment 

## Libraries and Services:
- [Django Rest Framework](https://www.django-rest-framework.org/) - Toolkit for building WEB APIs
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Provides a JSON Web Token authentication backend for the Django REST Framework
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK to configure S3 storage 

## Development
### Prerequisites
To run this application you'll need:
- Python 3.7 or higher
- Node.js & npm installed 
- A local installation of [PostgreSQL](https://www.postgresql.org/download/) and a database instance named photolair
or anything else by changing the database name in ```core/core/settings.py```
   > ### Note
   >
   > If you have brew, install PostgreSQL with the following steps:
   >
   > -  `brew install postgresql` to install PostgreSQL
   > -  `brew services start postgresql` to start the PostgreSQL service (stop it with `brew services stop PostgreSQL`)

### Getting Started
In order to run the back-end and/or the front-end locally follow the instructions below.

Begin by cloning the repository
```
https://github.com/harmanT23/PhotoLair.git
```

#### Django Backend

Set up a virtual environment for development (recommend using venv)
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

#### React Front-End

Change directory to client directory from project directory
```
cd client
```

Install all front-end dependencies
```
npm install
```

Start front-end
```
npm start
```

## PhotoLair API
The application provides an API for authentication, user accounts and images.
The following endpoints are currently implemented:

### Authentication Endpoints
- ```POST /api/token/``` - Takes the username and password of a user and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
- ```POST /api/token/refresh/``` - Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
- ```POST /api/logout/blacklist/``` - Used to blacklist refresh tokens after a user logs out.

### User Endpoints
- ```POST /api/users/``` - Register a new user with username and password.
- ```GET /api/users/{id}/``` - Get details about a specific user
- ```GET /api/users/me/``` - Get details about the currently authenticated user
- ```PUT/PATCH /api/users/{id}/``` - Update a specific user's details
- ```DELETE /api/users/{id}/``` - Delete a specific user's details 

### Image Endpoints
- ```GET /api/images/``` - Get all images on the marketplace (used to display a gallery on the homepage)
- ```POST /api/images/``` - Upload a image to sell on the marketplace by providing a title, price, inventory and image.
- ```GET /api/images/{image_id}/``` - Download the specified image, this endpoint will transfer the required amount of credits from the authenticated user 
to the user who posted the image as well as update the inventory of the image.
- ```PATCH /api/images/{image_id}``` - Update details of the image such as its title, price and inventory as well as the option to replace the image itself
- - ```PATCH /api/images/{image_id}``` - Delete the specified image

## Contributing
1. [Fork it](https://github.com/harmanT23/PhotoLair/fork)
2. Create your feature branch i.e. ```git checkout -b feature/foo```
3. Commit your changes i.e. ```git commit -am 'Add some foo'```
4. Push to branch i.e. ```git push origin feature/foo```
5. Create a new Pull Request

## Authors
[Harman Tatla](https://github.com/harmanT23) - Project Developer

