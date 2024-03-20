from django import template
from ..models import Message

register = template.Library()

@register.simple_tag(takes_context=True)
def unread_messages_count(context, chat_id):
    # Предполагается, что 'viewed' - это поле ManyToManyField в модели Message
    # для отслеживания пользователей, просмотревших сообщение
    if context['request'].user.is_authenticated:
        # If authenticated, proceed as before
        unread_messages = Message.objects.filter(chat_id=chat_id).exclude(viewed=context['request'].user).count()
    else:
        # If not authenticated, return  0 or handle accordingly
        unread_messages =  0
    return unread_messages
