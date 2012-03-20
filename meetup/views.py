from models import Meetup
from datetime import datetime
from django.shortcuts import render


def get_nearest_meetup():
    """
    Get the nearest meetup if it exists, else return None
    """
    meetups = Meetup.objects.filter(
        datetime__gte=datetime.now()
    ).order_by('datetime')

    if meetups.exists():
        meetup = meetups[0]
    else:
        meetup = None

    return meetup


def front(request):

    meetup = get_nearest_meetup()

    return render(request, 'frontpage.html', {'meetup': meetup})
