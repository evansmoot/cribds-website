from django.shortcuts import render

# Create your views here.
def projects(request):
    """View function for projects page of site"""

    return render(request, 'projects.html')

def info(request):
    return render(request, 'index.html')