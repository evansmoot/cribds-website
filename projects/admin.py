from django.contrib import admin
from projects.models import Project, Refugee, ProjectType, Camp, Town

# Register your models here.
admin.site.register(Project)
admin.site.register(Refugee)
admin.site.register(ProjectType)
admin.site.register(Camp)
admin.site.register(Town)