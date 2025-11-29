from django.shortcuts import render
from django.utils import timezone
from .models import Event

def event_list(request):
    # Filter for upcoming events (date >= today)
    today = timezone.now().date()
    events = Event.objects.filter(date__gte=today).order_by('date')
    return render(request, 'events/event_list.html', {'events': events})
