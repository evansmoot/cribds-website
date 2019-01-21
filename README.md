# cribds-website


To install and run
```
git clone https://github.com/evansmoot/cribds-website.git
```
-install python 3.7.2

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
And finally
```
python manage.py runserver
```

The project should be running on the ip address specified in your console
