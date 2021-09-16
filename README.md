**Aspire Assessment**

***Aspire assessment is developed on top of https://the-one-api.dev api. it exposes api endpoints that return resources regarding the lord of the rings character, quotes, etc. and
With this endpoint, authenticated users can assess the service for all the characters of The lord of the rings movie, quotes made by the characters. 
Authenticated users can also mark characters and their quotes as their favourites***

**Installation**

1. clone the application using this url and change directory to the root directory
2. install python if you don't already have python installed
3. install virtualenv using "pip install virtualenv"
4. create virtual environment using "virtualenv venv" or any method you are familiar with.
5. activate the virtual environment using "source venv/bin/activate"
6. install the project requirements using "pip install -r requirements"
7. create a .env file to look like the env.example (ensure to put the necessary value)
   go to https://the-one-api.dev/documentation to read on how to get their api key
9. run the migrations using "python manage.py migrate"
10. process and save the characters' data from the one api using "python manage.py process_characters"
11. process and save the quotes' data from the one api using "python manage.py process_quotes"
12. run the server using "python manage.py runserver"
