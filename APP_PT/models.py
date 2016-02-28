from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.

class Rubrica(models.Model):
    e_who = models.IntegerField
    e_when = models.IntegerField


class Pregunta(models.Model):
    p_enc_id = models.ForeignKey(Rubrica)
    question = models.CharField(max_length=200)

class Opcion(models.Model):
    o_preg_id = models.ForeignKey(Pregunta)
    o_option = models.CharField(max_length=200)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name1 = models.CharField(max_length=30)
    last_name2 = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    type = models.IntegerField()

class Project(models.Model):
    pr_name = models.CharField(max_length=30)
    pr_description = models.CharField(max_length=200)
    pr_user = models.ForeignKey(User)
    p_ini_date = models.DateField
    p_deadline = models.DateField

class Actividad(models.Model):
    ac_name = models.CharField(max_length=30)
    ac_description = models.CharField(max_length=200)
    ac_percentage = models.IntegerField
    ac_ini_date = models.DateField
    ac_deadline = models.DateField
    ac_projectID = models.ForeignKey(Project)

class Equipo(models.Model):
    eq_projectID = models.ForeignKey(Pregunta)
    eq_name = models.CharField(max_length=30)

class Participante(models.Model):
    par_projectID = models.ForeignKey(Pregunta)
    par_userID = models.ForeignKey(User)

