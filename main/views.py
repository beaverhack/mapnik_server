from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

from .models import *
import random

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    """
    Test url
    """
    return HttpResponse(json.dumps({ "test" : "success"}))


@csrf_exempt
def add_location(request):
    """
    Creates a Location object in the database.
    """
    try:
        print "---1---"
        data = json.loads(request.body)
        print data

        lat = data['lat']
        lon = data['lon']
        nick = data['nick']

        loc = Location(lat=lat, lon=lon, nick=nick)
        loc.save()

        return HttpResponse(json.dumps({ "created" : "y"}))
    except:
        s = json.dumps({ "created" : "error", "details": "None"})
        return HttpResponse(s)
