from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './scarp-8329-firebase-adminsdk-p2gz4-5c17831320.json')

cred = credentials.Certificate(filename)
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

# Create your views here.
def projects(request):
    """View function for projects page of site"""
    query = request.GET.get('q')
    
    print(query)
    if (query is not None and query.strip() != ""):
        camps_ref = db.collection('camps').where('name', '==', query).get()
        camp_list = { camp.id for camp in camps_ref }

        towns_ref = db.collection('towns').where('town', '==', query).get()
        town_list = { town.id for town in towns_ref }

        refugee_list = []
        name_query = query.split(" ")
        if(len(name_query) == 2):
            refugee_first_name_ref = db.collection('refugees').where('first_name', '==', name_query[0]).get()
            for refugee in refugee_first_name_ref:
                refugee_list.append(refugee.id)

            refugee_last_name_ref = db.collection('refugees').where('last_name', '==', name_query[1]).get()
            for refugee in refugee_last_name_ref:
                if refugee.id not in refugee_list:
                    refugee_list.append(refugee.id)

        refugee_first_name_ref = db.collection('refugees').where('first_name', '==', query).get()
        for refugee in refugee_first_name_ref:
                refugee_list.append(refugee.id)

        refugee_last_name_ref = db.collection('refugees').where('last_name', '==', query).get()
        for refugee in refugee_last_name_ref:
                if refugee.id not in refugee_list:
                    refugee_list.append(refugee.id)

        for camp_id in camp_list:
            refugee_camp_ref = db.collection('refugees').where('camp', '==', camp_id).get()
            for refugee in refugee_camp_ref:
                if refugee.id not in refugee_list:
                    refugee_list.append(refugee.id)
        for town_id in town_list:
            refugee_town_ref = db.collection('refugees').where('hometown', '==', town_id).get()
            for refugee in refugee_town_ref:
                if refugee.id not in refugee_list:
                    refugee_list.append(refugee.id)

        project_list = []
        project_type_ref = db.collection('project_types').where('name', '==', query).get()
        project_type_list = { project_type.id for project_type in project_type_ref }
        for project_type_id in project_type_list:
            project_type_ref = db.collection('projects').where('project_type', '==', project_type_id).get()
            for project in project_type_ref:
                project_list.append(project.id)

        for refugee_id in refugee_list:
            project_ref = db.collection('projects').where('creator', '==', refugee_id).get()
            for project in project_ref:
                if project.id not in project_list:
                    project_list.append(project.id)

        project_title_ref = db.collection('projects').where('title', '==', query).get()
        for project in project_title_ref:
            if project.id not in project_list:
                project_list.append(project.id)

        page_content = {}
        for project in project_list:
            ref = db.collection('projects').document(project).get()
            page_content[project] = ref.to_dict()
    else:
        ref = db.collection('projects').get()
        page_content = { project.id: project.to_dict() for project in ref }

    data_list = []
    for key, value in page_content.items():
        value["id"] = key
        data_list.append(value)

    return render(request, 'projects.html', {'data' : data_list})

def projects_detail(request, id):
    """View function for projects page of site"""
    project_ref = db.collection('projects').document(id).get().to_dict()
    refugee_ref = db.collection('refugees').document(project_ref["creator"]).get().to_dict()
    camps_ref = db.collection('camps').document(refugee_ref["camp"]).get().to_dict()
    town_ref = db.collection('towns').document(refugee_ref["hometown"]).get().to_dict()
    context = {
        'project': project_ref,
        'refugee': refugee_ref,
        'camp': camps_ref,
        'town': town_ref
    }
    return render(request, 'projects_detail.html', context)

def info(request):
    return render(request, 'index.html')