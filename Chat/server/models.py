from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    first_name =    models.CharField(max_length=20, default='Аккаунт удален', null=True)
    last_name =     models.CharField(max_length=20, default='', null=True)
    age =           models.IntegerField(default=0, null=True)
    gender =        models.BooleanField(default=False, null=True)
    email =         models.EmailField(unique=True, null=True)
    login =         models.CharField(max_length=20, unique=True, null=True)
    password =      models.CharField(max_length=100, null=True)

class Chat(models.Model):
    name =          models.CharField(max_length=20, null=True)
    user =          models.ForeignKey('User', on_delete = models.SET_NULL, null=True)

class Party(models.Model):
    chat =          models.ForeignKey('Chat', on_delete = models.CASCADE, null=True)
    user =          models.ForeignKey('User', on_delete = models.SET_NULL, null=True)

class Message(models.Model):
    chat =          models.ForeignKey('Chat', on_delete = models.CASCADE, null=True)
    user =          models.ForeignKey('User', on_delete = models.SET_NULL, null=True)
    content =       models.CharField(max_length=1000, null=True)
    date =          models.DateTimeField(null=True)
