# Description:

    This project provides a REST API for detecting spam phone numbers and searching for contact details. It is built with Django and uses PostgreSQL for data storage.

# Activate the venv environment by using following commands:

    python -m venv venv
    source venv/bin/activate


# Install Dependencies: 
    pip install -r requirements.txt

# Setup Database:

    Make sure PostgreSQL is installed and running.
    Create a PostgreSQL database and user and change configuration in settings.py file of this project.

# Commands to execute:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py populate_db
    python manage.py runserver

#  API Endpoints
    Register User: POST api/register/
    Search Contacts by Name: GET api/search/
    Search Contacts by Phone Number: GET api/search-by-phone/
    Mark Number as Spam: POST api/spam/
    Get Spam Likelihood: GET api/spam/<phone_number>/

# 
# If you don't want to run and interested in seeing the results then i have included the screenshots of these api's tested in the postman 