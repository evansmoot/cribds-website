from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for index page of site"""

    return render(request, 'index.html')