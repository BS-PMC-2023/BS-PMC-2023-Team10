def message_count(request):
    from .models import Message, Reservation
    messages = Message.objects.filter(status='Pending').count()
    reservations = Reservation.objects.filter(status='Pending').count()
    return {'message_count': messages, 'reservation_count': reservations}
