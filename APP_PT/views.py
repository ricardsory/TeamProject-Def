from django.shortcuts import render
from .models import User
from .forms import CreateAccount

# Create your views here.

def login(request):
    users = User.objects.all()
    return render(request, 'APP_PT/login.html', {'users': users})

def newUser(request):
    form = CreateAccount()
    return render(request, 'APP_PT/newUser.html', {'form': form})