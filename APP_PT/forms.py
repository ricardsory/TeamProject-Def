from django import forms
from .models import User, Actividad, Project

# Create your views here.

class CreateAccount(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name1', 'last_name2' ,'email' , 'password',)

class CreateProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('pr_name', 'pr_description', 'pr_ini_date', 'pr_deadline',)

class CreateActivity(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('ac_name', 'ac_description', 'ac_ini_date', 'ac_deadline', 'ac_projectID',)