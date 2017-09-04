from django.shortcuts import render
from django.http import HttpResponse
from parsed_data.models import RatingData
import json
import datetime
import config

# Create your views here.
def getRating(request):
    data = []
    for r in RatingData.objects.all().order_by('-created_at'):
        data.append({
            'id': r.id,
            'USER': r.userName,
            'SOLO': r.solo,
            'DUO': r.duo,
            'SQUAD': r.squad,
            'Update_time': datetime.datetime.strftime(r.created_at, "%Y-%m-%d %H:%M:%S"),
        })
    data = json.dumps(data, indent=4)
    print("Get - rating data")
    print(data)
    return HttpResponse(data, content_type = "application/json")

def getRecentRating(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLO': r[0].solo,
            'DUO': r[0].duo,
            'SQUAD': r[0].squad,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    data = json.dumps(data, indent=4)
    print("Get - recent rating data")
    print(data)
    return HttpResponse(data, content_type = "application/json")