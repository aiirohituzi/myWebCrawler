import threading

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import json
import random
import datetime

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
import django
django.setup()

from parsed_data.models import RatingData

import config

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome('../chromedriver/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3)

CRAWLER_TIME = 600

SEASON = config.CURRENT_SEASON

class Paser:
    SAVE_COUNT = 0

    def __init__(self, count):
        self.SAVE_COUNT = count

    def parse_rating(self):
        data = []
        
        for user in config.USER_LIST:
            print(user)
            
            ratings = {}

            driver.get(config.SITE_ADDRESS + user)

            html = driver.page_source

            # req = requests.get(config.SITE_ADDRESS + user)

            # html = req.text

            soup = BeautifulSoup(html, 'html.parser')


            
            solo = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.solo.modeItem > div.mode-section.tpp > div.overview > div.rating > span.value'
            )
            duo = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.duo.modeItem > div.mode-section.tpp > div.overview > div.rating > span.value'
            )
            squad = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.squad.modeItem > div.mode-section.tpp > div.overview > div.rating > span.value'
            )

            solofpp = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.solo.modeItem > div.mode-section.fpp > div.overview > div.rating > span.value'
            )
            duofpp = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.duo.modeItem > div.mode-section.fpp > div.overview > div.rating > span.value'
            )
            squadfpp = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.overview > div.rating > span.value'
            )

            solokd = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.solo.modeItem > div.mode-section.tpp > div.stats > div.kd.stats-item.stats-top-graph > p'
            )
            duokd = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.duo.modeItem > div.mode-section.tpp > div.stats > div.kd.stats-item.stats-top-graph > p'
            )
            squadkd = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.squad.modeItem > div.mode-section.tpp > div.stats > div.kd.stats-item.stats-top-graph > p'
            )

            solofppkd = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.solo.modeItem > div.mode-section.fpp > div.stats > div.kd.stats-item.stats-top-graph > p'
            )
            duofppkd = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.duo.modeItem > div.mode-section.fpp > div.stats > div.kd.stats-item.stats-top-graph > p'
            )
            squadfppkd = soup.select(
                '#profile > div.profileContent > div.modeSummary > section.squad.modeItem > div.mode-section.fpp > div.stats > div.kd.stats-item.stats-top-graph > p'
            )

            if solo != []:
                ratings.update({'solo': solo[0].text})
            if duo != []:
                ratings.update({'duo': duo[0].text})
            if squad != []:
                ratings.update({'squad': squad[0].text})

            if solofpp != []:
                ratings.update({'solofpp': solofpp[0].text})
            if duofpp != []:
                ratings.update({'duofpp': duofpp[0].text})
            if squadfpp != []:
                ratings.update({'squadfpp': squadfpp[0].text})

            if solokd != []:
                ratings.update({'solokd': solokd[0].text.replace(" ", "").rstrip().lstrip()})
            if duokd != []:
                ratings.update({'duokd': duokd[0].text.replace(" ", "").rstrip().lstrip()})
            if squadkd != []:
                ratings.update({'squadkd': squadkd[0].text.replace(" ", "").rstrip().lstrip()})

            if solofppkd != []:
                ratings.update({'solofppkd': solofppkd[0].text.replace(" ", "").rstrip().lstrip()})
            if duofppkd != []:
                ratings.update({'duofppkd': duofppkd[0].text.replace(" ", "").rstrip().lstrip()})
            if squadfppkd != []:
                ratings.update({'squadfppkd': squadfppkd[0].text.replace(" ", "").rstrip().lstrip()})
            
            data.append({
                user: ratings
            })

        driver.close()

        return data

    def dbSave(self):
        rating_data = self.parse_rating()
        print(rating_data)
        # if self.SAVE_COUNT > 5:
        for arr in rating_data:
            for user, rating in arr.items():
                print(user)
                print(str(rating.get('solo')) + '/' + str(rating.get('duo')) + '/' + str(rating.get('squad')))
                print(str(rating.get('solofpp')) + '/' + str(rating.get('duofpp')) + '/' + str(rating.get('squadfpp')))
                print(str(rating.get('solokd')) + '/' + str(rating.get('duokd')) + '/' + str(rating.get('squadkd')))
                print(str(rating.get('solofppkd')) + '/' + str(rating.get('duofppkd')) + '/' + str(rating.get('squadfppkd')))
                RatingData(
                    userName=user,
                    solo=rating.get('solo'),
                    duo=rating.get('duo'),
                    squad=rating.get('squad'),
                    solofpp=rating.get('solofpp'),
                    duofpp=rating.get('duofpp'),
                    squadfpp=rating.get('squadfpp'),
                    solokd=rating.get('solokd'),
                    duokd=rating.get('duokd'),
                    squadkd=rating.get('squadkd'),
                    solofppkd=rating.get('solofppkd'),
                    duofppkd=rating.get('duofppkd'),
                    squadfppkd=rating.get('squadfppkd'),
                    season=SEASON
                ).save()
            # self.SAVE_COUNT = 0
        # self.SAVE_COUNT += 1
        # threading.Timer(CRAWLER_TIME + random.randrange(1,5), self.dbSave).start()

if __name__=='__main__':
    p = Paser(0)
    p.dbSave()