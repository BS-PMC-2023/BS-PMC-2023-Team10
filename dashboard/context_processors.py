def message_count(request):
    from .models import Message
    messages = Message.objects.filter(status='Pending').count()
    return {'message_count': messages}
