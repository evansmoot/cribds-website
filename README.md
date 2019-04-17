# Southern Cameroons and Ambazonia Refugee Project Delivery Documentation

## Release Notes:
### New Features:
Projects are displayed on projects page for viewing by donors
Project information is displayed when individual projects are clicked on
Projects can be searched by creator, title, category, town, or camp
### Bug Fixes
Empty search string now returns all projects
Project search by name can now work for first name or last name
### Known Bugs
Cannot search projects by partial string matching (so entire title must be entered for example)
Consider using Algolia or ElasticSearch to allow for full-text searching of the Firestore database moving forward

## Website Install Information:
### Prerequisites:
Python 3.7.2 or latest version installed and configured (https://www.python.org/downloads/)
pip installed and configured (https://pypi.org/project/pip/)
### Dependent Libraries:
firebase-admin-python (https://github.com/firebase/firebase-admin-python) should be installed prior to running. If pip is installed, you can run pip install firebase_admin in the project directory
### Download Instructions:
https://github.com/evansmoot/cribds-website
Project can be downloaded as a zip and extracted in the desired directory or with git (https://git-scm.com/)
### Build Instructions
User will need credentials to access firebase:
Go to (https://console.firebase.google.com/) and log in with the credentials given to you by the developers. 
Navigate to the Service Accounts tab in the project's settings page
Click the Generate New Private Key button at the bottom of the Firebase Admin SDK section of the Service Accounts tab.
A JSON file containing the credentials needed to access the database will be downloaded. Add this to the project directory at the path cribds_website/projects/ (in the same folder as apps.py, urls.py, views.py, etc...)
Warning: Use extra caution when handling service account credentials in your code. Do not commit them to a public repository, deploy them in a client app, or expose them in any way that could compromise the security of your Firebase project.
### Run Instructions
Navigate to the root directory of the project in your terminal (in the same folder as manage.py) and type py manage.py runserver
The website should now be running on your local machine at the IP address specified in the terminal
