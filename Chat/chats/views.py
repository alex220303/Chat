from django.shortcuts import render
from django.db.models import Max
from .models import *
import operator

def base(request):
    # Получаем все чаты
    chats = Chat.objects.annotate(last_message_date=Max('message__date')).order_by('-last_message_date')

    return render(request, 'chats.html', context={'chats':chats,})

def view_chat_name(reauest):
    pass
