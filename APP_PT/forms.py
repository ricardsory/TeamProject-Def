from django import forms
from .models import User, Actividad, Project, Rubrica

# Create your views here.

class CreateAccount(forms.ModelForm):

    class Meta:
        model = User
        fields = ()

class Login(forms.ModelForm):

    class Meta:
        model = User
        fields = ()

class CreateProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('pr_name', 'pr_description', 'pr_ini_date', 'pr_deadline',)

class CreateActivity(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('ac_name', 'ac_description', 'ac_ini_date', 'ac_deadline', 'ac_projectID',)

class CreatePoll(forms.ModelForm):

    class Meta:
        model = Rubrica
        fields = ('e_who', 'e_when',)