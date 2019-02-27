from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

#After making changes must migrate by running
#py manage.py makemigrations
#py manage.py migrate

class ProjectType(models.Model):
    """Model representing a project type"""
    name = models.CharField(max_length=200, help_text='Choose a project type')

    def __str__(self):
        """String for representing a project type object"""
        return self.name
    
    class Meta:
        ordering = ['name']
        db_table = "project_types"

class Project(models.Model):
    """Model representing a project"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    refugee = models.ForeignKey('Refugee', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter a description of the project')
    funds = models.DecimalField(max_digits=9, decimal_places=2, help_text='Enter the desired funds for the project')
    submission_date = models.DateField(auto_now_add=False)
    status = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(-1)]) #Status of rejected/approved project. 0 is pending, 1 is approved, -1 is rejected
    project_type = models.ForeignKey(ProjectType, help_text='Choose a project type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing a project object"""
        return f'{self.name} by {self.refugee}'

    def get_absolute_url(self):
        """Returns the url to access the details of this project"""
        return reverse('project-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['name']
        db_table = "projects"

class Refugee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    camp = models.ForeignKey("Camp", max_length=100, on_delete=models.SET_NULL, null=True)
    hometown = models.ForeignKey("Town", max_length=100, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    profession = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = "refugees"

    def get_absolute_url(self):
        """Returns the url to access the details of this refugee"""
        return reverse('refugee-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing a refugee"""
        return f'{self.last_name}, {self.first_name}'

class Camp(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        db_table = "camps"

class Town(models.Model):
    county = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    town = models.CharField(max_length=100)

    def __str__(self):
        return self.town
    
    class Meta:
        ordering = ['town']
        db_table = "towns"