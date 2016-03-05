from django.shortcuts import render
from .models import User, Actividad, Project
from .forms import CreateAccount, CreateProject, CreateActivity
from django.shortcuts import redirect

# Create your views here.

def login(request):
    users = User.objects.all()
    return render(request, 'APP_PT/login.html', {'users': users})

def newUser(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.type = request.POST.get('type', 'student')
            user.save()
            return redirect('APP_PT.views.login')
    else:
        form = CreateAccount()
    return render(request, 'APP_PT/newUser.html', {'form': form})

def newProject(request):
    if request.method == "POST":
        form = CreateProject(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('APP_PT.views.login')
    else:
        form = CreateProject()
        users = User.objects.all()
    return render(request, 'APP_PT/createProject.html', {'form': form, 'users': users})

def newActivity(request):
    if request.method == "POST":
        form = CreateActivity(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.ac_percentage = request.POST.get('type', 'student')
            activity.save()
            return redirect('APP_PT.views.login')
    else:
        form = CreateActivity()
    return render(request, 'APP_PT/createActivity.html', {'form': form})