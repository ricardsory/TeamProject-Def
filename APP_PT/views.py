from django.shortcuts import render
from .models import User, Actividad, Project
from .forms import CreateAccount, CreateProject, CreateActivity, CreatePoll, Login
from django.shortcuts import redirect

# Create your views here.

def login(request):
    form = Login()
    if request.method == "POST":
        if request.POST.get("hlogin") == '1':
            if User.objects.filter(email=request.POST.get("lemail")).filter(password=request.POST.get("lpass")):
                request.session['user'] = email=request.POST.get("lemail")
                return redirect('APP_PT.views.menu')
            else:
              return redirect('APP_PT.login.html', {'message': 'Incorrect user'})
        else:
            if request.POST.get("hregister") == '1':
                user = User(first_name=request.POST.get("rname"), email=request.POST.get("remail"), password=request.POST.get("rpass"),birthyear=request.POST.get("ryear"), type="user")
                user.save()
                return redirect('APP_PT.views.menu')
    else:
        return render(request, 'APP_PT/login.html',{'form': form})

def menu(request):
    return render(request, 'APP_PT/menu.html')

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

def newPoll(request):
    if request.method == "POST":
        form = CreatePoll(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            id = poll.save()
            i = 0
            while i < request.POST.get('nquestions', 0):
                question = form.save(commit=False)
                question.question = request.POST.get('nquestions' + i, '')
                i = i + 1
                question.p_enc_id = id

            return redirect('APP_PT.views.login')
    else:
        form = CreateActivity()
    return render(request, 'APP_PT/createActivity.html', {'form': form})