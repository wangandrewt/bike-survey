# Bike Survey

Code for the University of Maryland Bike Survey (Spring 2015).

Also see bikesurvey/static/humans.txt

## SQLite3 Database

The database (web/db.sqlite3) can be deleted. Running `python manage.py runserver`
will create a new database automatically. Create the models in the database by 
running `python manage.py migrate`. Remember to create a new superuser.

## Instructions

For Debian Linux

1. Install Python. Also install Python-dev: `sudo apt-get install python-dev`
2. Install Pip: `sudo apt-get install python-pip` [More Info](https://pip.pypa.io/en/latest/installing.html#using-the-installer)
3. Install virtualenv: `sudo pip install virtualenv`
4. Install Git and clone this repository
5. Create new virtualenv and activate [More Info](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
6. Install Django and other software: `cd bikesurvey && pip install -r requirements.txt`
7. Run the server: `python manage.py runserver` [http://127.0.0.1:8000/](http://127.0.0.1:8000/) is the default URL.

See above for database info.

 * [website URL]/ - Start here
 * [website URL]/list/ - View records
 * [website URL]/admin/ - Administrator interface