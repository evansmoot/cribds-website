# cribds-website
*NOTE*: Replace "py" with whatever command runs python 3

To install and run
```
git clone https://github.com/evansmoot/cribds-website.git
```
-install python 3.7.2

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
\c cribds (Maybe not, if it doesn't work skip this and let me know)
```
Now in your project folder type
```
py manage.py createsuperuser
py manage.py makemigrations
py manage.py migrate
```
And finally
```
python manage.py runserver
```

The project should be running on the ip address specified in your console
