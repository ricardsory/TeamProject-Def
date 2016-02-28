from django.shortcuts import render
from .models import User
from .forms import CreateAccount
from django.shortcuts import redirect

# Create your views here.

def login(request):
    users = User.objects.all()
    return render(request, 'APP_PT/login.html', {'users': users})

def newUser(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()
            return redirect('APP_PT.views.login')
    else:
        form = CreateAccount()
        return render(request, 'APP_PT/newUser.html', {'form': form})