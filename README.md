# Pastaverse
*Work in progress, contributions are appreciated!*

Pastaverse is an evolving restaurant web application, meticulously built with Django to provide a full-stack web experience. My primary focus is on fostering modularity and code reuse to create a scalable and efficient dining experience. Each component is designed as a standalone app, promoting easy integration and adaptability for future projects.  
Explore a seamless dining experience with features like menu management, online ordering, reservations, and more.  

![Home page of the Web Application](description_gifs/home_page.gif "Home page of the Web Application")
## Project Structure:
1. Core App ([core](core)):
    - Common functionalities such as base templates, and global settings using the power of Django.
2. Menu App ([menu](menu)):
    - Utilizes Django models and templates to handle menu items, categories, and pricing in a flexible and efficient manner.
3. Ordering App ([ordering](ordering)):
    - Leverages Django Rest Framework for the creation, cart management, and streamlined checkout process, ensuring a smooth ordering experience.
5. Reservation App ([reservation](reservation)):
    - Integrates Django's powerful features to manage table reservations and availability seamlessly.
7. Review and Rating App ([reviews](reviews)):
    - Implements Django Rest Framework serializers and views for a dynamic customer review and rating system.
9. Location App ([location](location)):
    - Utilizes Django's capabilities to integrate features related to the restaurant's physical location, including maps and detailed address information.
11. User Profile App ([user_profile](user_profile)):
    - Harnesses Django's user authentication and profile management capabilities to provide a personalized user experience.
## Key Features:
- Built on the Django framework for a robust and maintainable codebase.
- Seamless integration of Django's ORM for efficient database interactions.
## Technological Stack:
- Framework: Django
- Database: MySQL, or SQLite for a quick view of the app's features
    - If you want to use the MySQL database, compile the 'DATABASE' section as follow:

    `DATABASES = { 
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database name',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'username',
        'PASSWORD': 'password',
        }
    }`
## How to Use:
1. Clone the repository to your local machine.
2. Set up a virtual environment and install dependencies writing the following commands in your Command Terminal. Pipenv take care of all the dependecies automatically, but make sure you have python 3.10 installed:
    - Install pipenv: pip3 install pipenv
    - Run the virtual environment: pipenv shell
    - Install the dependencies: pipenv install
    - Run the migrations: python manage.py migrate
    - Run the server: python manage.py runserver
    - Explore the website at 127.0.0.1:8000

## Contribution:
Contributions are welcome! Fork the repository, create a new branch, make your enhancements, and submit a pull request. Let's collaboratively enhance Pastaverse!
