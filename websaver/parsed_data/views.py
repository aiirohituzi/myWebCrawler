from django.shortcuts import render
from django.http import HttpResponse
from parsed_data.models import RatingData
import json
import datetime
import config
import operator

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
            'SOLOFPP': r.solofpp,
            'DUOFPP': r.duofpp,
            'SQUADFPP': r.squadfpp,
            'Update_time': datetime.datetime.strftime(r.created_at, "%Y-%m-%d %H:%M:%S"),
        })
    data = json.dumps(data, indent=4)
    print("Get - rating data")
    # print(data)
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
            'SOLOFPP': r[0].solofpp,
            'DUOFPP': r[0].duofpp,
            'SQUADFPP': r[0].squadfpp,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    data = json.dumps(data, indent=4)
    print("Get - recent rating data")
    # print(data)
    return HttpResponse(data, content_type = "application/json")

def getUserRating(request):
    data = []
    userName = request.GET.get('userName', False)
    season = request.GET.get('season', config.CURRENT_SEASON)

    if userName:
        obj = RatingData.objects.filter(userName=userName, season=season).order_by('-created_at')
        for r in obj:
            data.append({
                'id': r.id,
                'USER': r.userName,
                'SOLO': r.solo,
                'DUO': r.duo,
                'SQUAD': r.squad,
                'SOLOFPP': r.solofpp,
                'DUOFPP': r.duofpp,
                'SQUADFPP': r.squadfpp,
                'SOLOKD': r.solokd,
                'DUOKD': r.duokd,
                'SQUADKD': r.squadkd,
                'SOLOFPPKD': r.solofppkd,
                'DUOFPPKD': r.duofppkd,
                'SQUADFPPKD': r.squadfppkd,
                'Update_time': datetime.datetime.strftime(r.created_at, "%Y-%m-%d %H:%M:%S"),
            })
        data = json.dumps(data, indent=4)
        print("Get - '" + userName + "' rating data")
        print(data)
    else:
        print("error - User not found")
    return HttpResponse(data, content_type = "application/json")


def getSoloRanking(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        solo = r[0].solo
        duo = r[0].duo
        squad = r[0].squad
        if r[0].solo != None:
            solo = int(solo.replace(',', ''))
        else:
            solo = 0
        if r[0].duo != None:
            duo = int(duo.replace(',', ''))
        else:
            duo = 0
        if r[0].squad != None:
            squad = int(squad.replace(',', ''))
        else:
            squad = 0
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLO': solo,
            'DUO': duo,
            'SQUAD': squad,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    sorted_data = sorted(data, key=operator.itemgetter('SOLO'), reverse=True)
    sorted_data = json.dumps(sorted_data, indent=4)
    print("Get - solo ranking data")
    # print(sorted_data)
    return HttpResponse(sorted_data, content_type = "application/json")


def getDuoRanking(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        solo = r[0].solo
        duo = r[0].duo
        squad = r[0].squad
        if r[0].solo != None:
            solo = int(solo.replace(',', ''))
        else:
            solo = 0
        if r[0].duo != None:
            duo = int(duo.replace(',', ''))
        else:
            duo = 0
        if r[0].squad != None:
            squad = int(squad.replace(',', ''))
        else:
            squad = 0
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLO': solo,
            'DUO': duo,
            'SQUAD': squad,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    sorted_data = sorted(data, key=operator.itemgetter('DUO'), reverse=True)
    sorted_data = json.dumps(sorted_data, indent=4)
    print("Get - duo ranking data")
    # print(sorted_data)
    return HttpResponse(sorted_data, content_type = "application/json")


def getSquadRanking(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        solo = r[0].solo
        duo = r[0].duo
        squad = r[0].squad
        if r[0].solo != None:
            solo = int(solo.replace(',', ''))
        else:
            solo = 0
        if r[0].duo != None:
            duo = int(duo.replace(',', ''))
        else:
            duo = 0
        if r[0].squad != None:
            squad = int(squad.replace(',', ''))
        else:
            squad = 0
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLO': solo,
            'DUO': duo,
            'SQUAD': squad,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    sorted_data = sorted(data, key=operator.itemgetter('SQUAD'), reverse=True)
    sorted_data = json.dumps(sorted_data, indent=4)
    print("Get - squad ranking data")
    # print(sorted_data)
    return HttpResponse(sorted_data, content_type = "application/json")


def getSolofppRanking(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        solofpp = r[0].solofpp
        duofpp = r[0].duofpp
        squadfpp = r[0].squadfpp
        if r[0].solofpp != None:
            solofpp = int(solofpp.replace(',', ''))
        else:
            solofpp = 0
        if r[0].duofpp != None:
            duofpp = int(duofpp.replace(',', ''))
        else:
            duofpp = 0
        if r[0].squadfpp != None:
            squadfpp = int(squadfpp.replace(',', ''))
        else:
            squadfpp = 0
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLOFPP': solofpp,
            'DUOFPP': duofpp,
            'SQUADFPP': squadfpp,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    sorted_data = sorted(data, key=operator.itemgetter('SOLOFPP'), reverse=True)
    sorted_data = json.dumps(sorted_data, indent=4)
    print("Get - solo-fpp ranking data")
    # print(sorted_data)
    return HttpResponse(sorted_data, content_type = "application/json")


def getDuofppRanking(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        solofpp = r[0].solofpp
        duofpp = r[0].duofpp
        squadfpp = r[0].squadfpp
        if r[0].solofpp != None:
            solofpp = int(solofpp.replace(',', ''))
        else:
            solofpp = 0
        if r[0].duofpp != None:
            duofpp = int(duofpp.replace(',', ''))
        else:
            duofpp = 0
        if r[0].squadfpp != None:
            squadfpp = int(squadfpp.replace(',', ''))
        else:
            squadfpp = 0
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLOFPP': solofpp,
            'DUOFPP': duofpp,
            'SQUADFPP': squadfpp,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    sorted_data = sorted(data, key=operator.itemgetter('DUOFPP'), reverse=True)
    sorted_data = json.dumps(sorted_data, indent=4)
    print("Get - duo-fpp ranking data")
    # print(sorted_data)
    return HttpResponse(sorted_data, content_type = "application/json")


def getSquadfppRanking(request):
    data = []
    for user in config.USER_LIST:
        r = RatingData.objects.filter(userName=user).order_by('-created_at')
        solofpp = r[0].solofpp
        duofpp = r[0].duofpp
        squadfpp = r[0].squadfpp
        if r[0].solofpp != None:
            solofpp = int(solofpp.replace(',', ''))
        else:
            solofpp = 0
        if r[0].duofpp != None:
            duofpp = int(duofpp.replace(',', ''))
        else:
            duofpp = 0
        if r[0].squadfpp != None:
            squadfpp = int(squadfpp.replace(',', ''))
        else:
            squadfpp = 0
        data.append({
            'id': r[0].id,
            'USER': r[0].userName,
            'SOLOFPP': solofpp,
            'DUOFPP': duofpp,
            'SQUADFPP': squadfpp,
            'Update_time': datetime.datetime.strftime(r[0].created_at, "%Y-%m-%d %H:%M:%S"),
        })
    sorted_data = sorted(data, key=operator.itemgetter('SQUADFPP'), reverse=True)
    sorted_data = json.dumps(sorted_data, indent=4)
    print("Get - squad-fpp ranking data")
    # print(sorted_data)
    return HttpResponse(sorted_data, content_type = "application/json")


def getUserRatingChart(request):
    data = []
    userName = request.GET.get('userName', False)
    season = request.GET.get('season', config.CURRENT_SEASON)

    if userName:
        obj = RatingData.objects.filter(userName=userName, season=season).order_by('created_at')
        for r in obj:
            solo = r.solo
            duo = r.duo
            squad = r.squad
            solofpp = r.solofpp
            duofpp = r.duofpp
            squadfpp = r.squadfpp

            if r.solo != None:
                solo = int(solo.replace(',', ''))
            else:
                solo = 0
            if r.duo != None:
                duo = int(duo.replace(',', ''))
            else:
                duo = 0
            if r.squad != None:
                squad = int(squad.replace(',', ''))
            else:
                squad = 0

            if r.solofpp != None:
                solofpp = int(solofpp.replace(',', ''))
            else:
                solofpp = 0
            if r.duofpp != None:
                duofpp = int(duofpp.replace(',', ''))
            else:
                duofpp = 0
            if r.squadfpp != None:
                squadfpp = int(squadfpp.replace(',', ''))
            else:
                squadfpp = 0
            
            data.append({
                'id': r.id,
                'USER': r.userName,
                'SOLO': solo,
                'DUO': duo,
                'SQUAD': squad,
                'SOLOFPP': solofpp,
                'DUOFPP': duofpp,
                'SQUADFPP': squadfpp,
                'Update_time': datetime.datetime.strftime(r.created_at, "%Y-%m-%d %H:%M:%S"),
            })
        data = json.dumps(data, indent=4)
        print("Get - '" + userName + "' rating chart data")
        # print(data)
    else:
        print("error - User not found")
    return HttpResponse(data, content_type = "application/json")

def getUserList(request):
    data = []
    for user in config.USER_LIST:
        data.append(user)
    data = json.dumps(data, indent=4)
    print("Get - User list")
    # print(data)
    return HttpResponse(data, content_type = "application/json")