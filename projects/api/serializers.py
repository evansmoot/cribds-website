from django.contrib.auth.models import User, Group
from rest_framework import serializers
from projects.models import ProjectType, Project, Refugee, Camp, Town

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProjectTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectType
        fields = ('id', 'name')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'refugee', 'description', 'funds', 'submission_date', 'status', 'project_type')

class RefugeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refugee
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'camp', 'hometown', 'email', 'phone', 'profession')

class CampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camp
        fields = ('id', 'name')

class TownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Town
        fields = ('id', 'town', 'lga', 'county')