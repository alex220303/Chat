# Generated by Django 5.0.2 on 2024-02-23 20:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='viewed',
            field=models.ManyToManyField(blank=True, related_name='viewed_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
