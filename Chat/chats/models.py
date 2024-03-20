from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    name =          models.CharField(max_length=20, null=True)
    user =          models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

class Party(models.Model):
    chat =          models.ForeignKey('Chat', on_delete = models.CASCADE, null=True)
    user =          models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

class Message(models.Model):
    chat =          models.ForeignKey('Chat', on_delete = models.CASCADE, null=True)
    user =          models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    content =       models.CharField(max_length=1000, null=True)
    date =          models.DateTimeField()
    viewed =        models.ManyToManyField(User, related_name='viewed_messages', blank=True)
