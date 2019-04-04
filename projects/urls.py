from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<slug:id>', views.projects_detail, name='projects')
]