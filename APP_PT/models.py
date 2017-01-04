from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime


# Create your models here.


class Rubrica(models.Model):
    e_who = models.IntegerField(default=0)
    e_when = models.DateField(default=datetime.datetime.now, blank=True)

class Pregunta(models.Model):
    p_enc_id = models.ForeignKey(Rubrica)
    question = models.CharField(max_length=200)
    type = models.IntegerField(default=1)

class Opcion(models.Model):
    o_preg_id = models.ForeignKey(Pregunta)
    o_option = models.CharField(max_length=200)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name1 = models.CharField(max_length=30)
    birthyear = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    disable = models.IntegerField(default=False)

class Subject(models.Model):
    sub_name = models.CharField(max_length=30)
    sub_description = models.CharField(max_length=300)
    sub_who = models.ForeignKey(User)

class Project(models.Model):
    pr_name = models.CharField(max_length=30)
    pr_description = models.CharField(max_length=200)
    pr_user = models.ForeignKey(User)
    pr_subject = models.ForeignKey(Subject)
    pr_ini_date = models.DateField(default=timezone.now)
    pr_deadline = models.DateField(default=timezone.now)

class RubricaProject(models.Model):
    rp_project = models.ForeignKey(Subject)
    rp_rubrica = models.ForeignKey(Rubrica)

class Actividad(models.Model):
    ac_name = models.CharField(max_length=30)
    ac_description = models.CharField(max_length=200)
    ac_percentage = models.IntegerField(default=0)
    ac_ini_date = models.DateField(default=timezone.now)
    ac_deadline = models.DateField(default=timezone.now)
    ac_projectID = models.ForeignKey(Project)

class Equipo(models.Model):
    eq_projectID = models.ForeignKey(Project)
    eq_name = models.CharField(max_length=30)

class Participante(models.Model):
    par_projectID = models.ForeignKey(Pregunta)
    par_userID = models.ForeignKey(User)

