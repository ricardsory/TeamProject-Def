from django.shortcuts import render, render_to_response
from .models import User, Actividad, Project, Subject
from .forms import CreateAccount, CreateProject, CreateActivity, CreatePoll, Login
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
@csrf_exempt
def login(request):
    form = Login()
    if request.method == "POST":
        if request.POST.get("hlogin") == '1':
            if User.objects.filter(email=request.POST.get("lemail")).filter(password=request.POST.get("lpass")):
                user = User.objects.get(email=request.POST.get("lemail"))
                name = getattr(user, 'first_name')
                lastname = getattr(user, 'last_name1')
                request.session['user'] = name + ' ' + lastname
                request.session['idUser'] = getattr(user, 'id')
                return redirect('APP_PT.views.menu')
            else:
              return render_to_response('APP_PT/login.html', {'userError': '1'})
        else:
            if request.POST.get("hregister") == '1':
                if User.objects.filter(email=request.POST.get("remail")):
                    return render_to_response('APP_PT/login.html', {'userError': '2'})
                else:
                    user = User(first_name=request.POST.get("rname"), email=request.POST.get("remail"), password=request.POST.get("rpass"),birthyear=request.POST.get("ryear"), type="user")
                    user.save()
                    subject = '[Team Project] Welcome to Team Project '
                    message = 'Thanks to be confidence with us. Enjoy your expirience with us. Project Team is a web application based on manage & evaluate projects.'
                    email = request.POST.get("remail")
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [email],fail_silently=False)
                    return redirect('APP_PT.views.menu')
    else:
        return render(request, 'APP_PT/login.html',{'form': form})

def menu(request):
    return render(request, 'APP_PT/menu.html')

def newProject(request):
    if request.method == "POST":
        return render(request, 'APP_PT/menu.html')
    else:
        return render(request, 'APP_PT/formProject.html')

def newTeam(request):
    if request.method == "POST":
        return render(request, 'APP_PT/menu.html')
    else:
        return render(request, 'APP_PT/formTeam.html')

def subjects(request):
    subjects = Subject.objects.all()
    listsubjects = [{ 'name' : subject.sub_name } for subject in subjects ]
    return HttpResponse(json.dumps(listsubjects), content_type="application/json")


def newSubject(request):
    if request.method == "POST":
        subject = Subject(sub_name=request.POST.get("subName"), sub_description=request.POST.get("subDesc"), sub_who=User.objects.get(id=request.session['idUser']))
        subject.save()
        return redirect('APP_PT.views.menu')
    else:
        return render(request, 'APP_PT/formSubject.html')

def seeActivities(request):
    if request.method == "POST":
        return render(request, 'APP_PT/menu.html')
    else:
        return render(request, 'APP_PT/seeActivities.html')

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