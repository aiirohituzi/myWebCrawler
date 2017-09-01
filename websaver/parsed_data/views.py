from django.shortcuts import render
from django.http import HttpResponse
from parsed_data.models import RatingData
import json

# Create your views here.
def getRating(request):
    data = []
    for r in RatingData.objects.all():
        data.append({
            'id': r.id,
            'USER': r.userName,
            'SOLO': r.solo,
            'DUO': r.duo,
            'SQUAD': r.squad,
        })
    data = json.dumps(data, indent=4)
    print("Get - rating data")
    # print(data)
    return HttpResponse(data, content_type = "application/json")