"""websaver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from parsed_data.views import getRating
from parsed_data.views import getRecentRating
from parsed_data.views import getUserRating

from parsed_data.views import getTPPRanking

# from parsed_data.views import getSoloRanking
# from parsed_data.views import getDuoRanking
# from parsed_data.views import getSquadRanking

from parsed_data.views import getFPPRanking

# from parsed_data.views import getSolofppRanking
# from parsed_data.views import getDuofppRanking
# from parsed_data.views import getSquadfppRanking

from parsed_data.views import getUserRatingChart
from parsed_data.views import getUserList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rating/$', getRating, name='getRating'),
    url(r'^recentRating/$', getRecentRating, name='getRecentRating'),
    url(r'^userRating/$', getUserRating, name='getUserRating'),
    url(r'^TPPRanking/$', getTPPRanking, name='getTPPRanking'),
    # url(r'^soloRanking/$', getSoloRanking, name='getSoloRanking'),
    # url(r'^duoRanking/$', getDuoRanking, name='getDuoRanking'),
    # url(r'^squadRanking/$', getSquadRanking, name='getSquadRanking'),
    url(r'^FPPRanking/$', getFPPRanking, name='getFPPRanking'),
    # url(r'^solofppRanking/$', getSolofppRanking, name='getSolofppRanking'),
    # url(r'^duofppRanking/$', getDuofppRanking, name='getDuofppRanking'),
    # url(r'^squadfppRanking/$', getSquadfppRanking, name='getSquadfppRanking'),
    url(r'^userRatingChart/$', getUserRatingChart, name='getUserRatingChart'),
    url(r'^userList/$', getUserList, name='getUserList'),
]