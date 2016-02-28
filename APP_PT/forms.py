from django import forms
from .models import User

# Create your views here.

class CreateAccount(forms.Form):

    class Meta:
        model = User
        fields = ('first_name', 'last_name1', 'last_name2' ,'email' , 'password', 'type')