import threading

import requests
from bs4 import BeautifulSoup
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
import django
django.setup()

from parsed_data.models import RatingData

import config

CRAWLER_TIME = 3600

class Paser:
    def __init__(self):
        pass

    def parse_rating(self):
        data = []
        for user in config.USER_LIST:
            print(user)
            req = requests.get(config.SITE_ADDRESS + user)

            html = req.text

            soup = BeautifulSoup(html, 'html.parser')

            first_rating = soup.select(
                '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(2) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            )

            second_rating = soup.select(
                '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(3) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            )

            third_rating = soup.select(
                '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(4) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            )

            first_category = soup. select(
                '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(2) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            )

            second_category = soup. select(
                '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(3) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            )

            third_category = soup. select(
                '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(4) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            )

            if third_rating == []:
                if second_rating == []:
                    data.append({
                        user: {first_category[0].text : first_rating[0].text}
                    })
                else:
                    data.append({
                        user: {
                            first_category[0].text : first_rating[0].text,
                            second_category[0].text: second_rating[0].text
                        }
                    })
            else:
                data.append({
                    user: {
                        first_category[0].text : first_rating[0].text,
                        second_category[0].text: second_rating[0].text,
                        third_category[0].text: third_rating[0].text
                    }
                })

        return data

    def dbSave(self):
        rating_data = self.parse_rating()
        for arr in rating_data:
            for user, rating in arr.items():
                print(rating.get('solo'))
                print(rating.get('duo'))
                print(rating.get('squad'))
                RatingData(userName=user, solo=rating.get('solo'), duo=rating.get('duo'), squad=rating.get('squad')).save()
        threading.Timer(CRAWLER_TIME, self.dbSave).start()

if __name__=='__main__':
    p = Paser()
    p.dbSave()