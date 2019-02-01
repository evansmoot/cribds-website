# cribds-website
*NOTE*: Replace "py" with whatever command runs python 3

To install and run
```
git clone https://github.com/evansmoot/cribds-website.git
```
-install python 3.7.2 (and make sure it's added to your PATH)

-install pip

---
OPTIONAL: Install and use virtual environment software:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#Installing_the_virtual_environment_software

For Windows (you might need to be in command prompt for this to work):
```
pip install virtualenvwrapper-win
mkvirtualenv my_django_environment
```
To enter into virtual env from now on type:
```
workon name_of_environment
```
---

```
pip install Django
```
Since we'll be using PostgreSQL eventually you'll need
```
pip install Django psycopg2
```
Now install PostgreSQL 10.6 and in the command line type
```
psql -U postgres
```
If you get a "authentication failed for user: postgres" then go to settings.py in the cribds_website folder and change the password line to whatever you made your postgres database password. It is currently "ADmin"

If you get a "cribds" database does not exist in the command line type
```
createdb cribds
```
Or open psql (the application on your computer) and (after going through the login process that might automatically appear) type
```
create database cribds
```
Now in your project folder type
```
py manage.py makemigrations
py manage.py migrat
py manage.py createsuperuser
```
And finally
```
py manage.py runserver
```

The project should be running on the ip address specified in your console
