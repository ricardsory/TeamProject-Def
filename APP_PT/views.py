from django.shortcuts import render
from .models import User

# Create your views here.

def login(request):
    users = User.objects.all()
    return render(request, 'APP_PT/login.html', {'users': users})