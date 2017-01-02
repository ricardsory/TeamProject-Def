from django.shortcuts import render, render_to_response
from .models import User, Actividad, Project, Subject, Pregunta, Rubrica, RubricaProject
from .forms import CreateAccount, CreateProject, CreateActivity, CreatePoll, Login
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils import timezone


# Create your views here.
@csrf_exempt
def login(request):
    form = Login()
    if request.method == "POST":
        if request.POST.get("hlogin") == '1':
            if User.objects.filter(email=request.POST.get("lemail")).filter(password=request.POST.get("lpass")).filter(disable=False):
                user = User.objects.get(email=request.POST.get("lemail"))
                name = getattr(user, 'first_name')
                lastname = getattr(user, 'last_name1')
                request.session['user'] = name + ' ' + lastname
                request.session['idUser'] = getattr(user, 'id')
                request.session['userType'] = getattr(user, 'type')
                request.session['userEmail'] = getattr(user, 'email')
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

def signout(request):
     request.session['user'] = ""
     request.session['idUser'] = ""
     request.session['userType'] = ""
     return redirect('APP_PT.views.login')


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

def editProfile(request):
    if request.method == "POST":
        user = User.objects.get(email=request.session["userEmail"])
        user.first_name = request.POST.get("name")
        user.last_name1 = request.POST.get("lastname")
        user.birthyear = request.POST.get("birthyear")
        user.password = request.POST.get("newpass")
        user.save()
        return redirect('APP_PT.views.menu')
    else:
        user = User.objects.get(email=request.session["userEmail"])
        return render(request, 'APP_PT/formProfile.html', {'username' : getattr(user, 'first_name'), 'password' : getattr(user, 'password'),'lastname' : getattr(user, 'last_name1') ,'birthyear': getattr(user, 'birthyear')})

def newPoll(request):
    if request.method == "POST":
        for input in request.POST.keys():
            if input == "nQ":
                nQ = int(request.POST.get(input))
                poll = Rubrica(e_who=request.session['idUser'],e_when=timezone.now())
                poll.save()
                for x in range(1, nQ+1):
                    question = Pregunta(question=request.POST.get("question|" + str(x)), type=request.POST.get("type|" + str(x)), p_enc_id=poll)
                    question.save()
        return redirect('APP_PT.views.menu')
    else:
        return render(request, 'APP_PT/formPoll.html')

def disable(request):
    user = User.objects.get(email=request.session["userEmail"])
    user.disable = True
    user.save()
    return redirect('APP_PT.views.signout')

def evaluateActivity(request):
    if request.method == "POST":
        return
    else:
        idProject = request.GET.get('idProject')
        rp = RubricaProject.objects.get(rp_project_id=idProject)
        rubrica = Rubrica.objects.get(id=rp.rp_rubrica_id)
        questions = Pregunta.objects.filter(p_enc_id=rubrica.id)
        return render(request, 'APP_PT/evaluatePoll.html',{'questions': questions})
