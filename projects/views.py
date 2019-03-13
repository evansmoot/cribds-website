from django.shortcuts import render
import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './scarp-8329-firebase-adminsdk-p2gz4-5c17831320.json')

cred = credentials.Certificate(filename)
default_app = firebase_admin.initialize_app(cred)

# options = {
#         'databaseURL':'https://scarp-8329.firebaseio.com',
#         'projectId': "scarp-8329",
#         'storageBucket': "scarp-8329.appspot.com",
#     }

db = firestore.client()

ref = db.collection('refugees').document('IpSj4Xp6aLk2jMvoTalQ')
print(ref)

doc = ref.get()
print(u'Document data: {}'.format(doc.to_dict()))

# Create your views here.
def projects(request):
    """View function for projects page of site"""
    query = request.GET.get('q')
    print(query)
    if (query is not None):
        q_string = 'http://localhost:8000/api/projects/?search=' + query
    else:
        q_string = 'http://localhost:8000/api/projects/'
    r = requests.get(q_string).json()
    # r = r.json()
    # for project in r['results']:
    #     project["description"] = project["description"][:140] + "..."
    # print(r['results'][0]['name'])
    return render(request, 'projects.html', {'data':r['results']})

def projects_detail(request, id):
    """View function for projects page of site"""
    project = requests.get('http://localhost:8000/api/projects/' + str(id))
    project = project.json()
    context = {
        'project': project,
    }
    return render(request, 'projects_detail.html', context)

def info(request):
    return render(request, 'index.html')