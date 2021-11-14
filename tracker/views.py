from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle, Navigation, Track
from django.contrib.auth.models import User
from datetime import timedelta, datetime
import json
from django.http import JsonResponse

posts = [
    {
        'id': '1',
        'plate': '35 IZM 35',
    },
    {
        'id': '2',
        'plate': '06 ANK 06',
    },
    {
        'id': '3',
        'plate': '07 ANT 07',
    }
]


def home(request):
    navigationList = Navigation.objects.values()
    for i in navigationList:
        v_index = i['id']
        v_longitude = Track.objects.filter(navigation_id_id = v_index).values()[0]['longitude']
        v_latitude = Track.objects.filter(navigation_id_id= v_index).values()[0]['latitude']
        navigationList[v_index - 1]['longitude'] = v_longitude
        navigationList[v_index - 1]['latitude'] = v_latitude

        i.pop('id', None)

    context = {
        'posts': navigationList # Navigation.objects.values('vehicle_id')
    }

    return render(request, 'tracker/home.html', context )

