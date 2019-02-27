from django.shortcuts import render
import requests
import json

# Create your views here.
def projects(request):
    """View function for projects page of site"""
    r = requests.get('http://localhost:8000/api/projects/')
    r = r.json()
    print(r['results'][0]['name'])
    return render(request, 'projects.html')

def info(request):
    return render(request, 'index.html')