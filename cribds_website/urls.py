"""cribds_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from projects import views
from projects.api import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)
router.register(r'project_type', viewsets.ProjectTypeViewSet)
router.register(r'projects', viewsets.ProjectViewSet)
router.register(r'refugees', viewsets.RefugeeViewSet)
router.register(r'camps', viewsets.CampViewSet)
router.register(r'towns', viewsets.TownViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    # path('projects/<int:id>', include('projects.urls')),
    path('info/', views.info, name='index'),
    path('', RedirectView.as_view(url='/info/', permanent=True)),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #This addition during development ONLY

