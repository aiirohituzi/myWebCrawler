import threading

import requests
from bs4 import BeautifulSoup
import json
import random

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
import django
django.setup()

from parsed_data.models import RatingData

import config

CRAWLER_TIME = 600

class Paser:
    SAVE_COUNT = 0

    def __init__(self, count):
        self.SAVE_COUNT = count

    def parse_rating(self):
        data = []
        
        for user in config.USER_LIST:
            print(user)
            
            ratings = {}

            req = requests.get(config.SITE_ADDRESS + user)

            html = req.text

            soup = BeautifulSoup(html, 'html.parser')


            for i in range(2, 8):
                r = soup.select(
                    '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(' + str(i) + ') > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
                )
                c = soup. select(
                    '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(' + str(i) + ') > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
                )

                if r != []:
                    ratings.update({c[0].text: r[0].text})


            # first_rating = soup.select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(2) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            # )

            # second_rating = soup.select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(3) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            # )

            # third_rating = soup.select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(4) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            # )

            # fourth_rating = soup.select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(5) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            # )

            # fifth_rating = soup.select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(6) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            # )

            # sixth_rating = soup.select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(7) > div > div.row.profile-match-overview-header > div.col-lg-10 > div > div:nth-of-type(1) > div > div.value.value-blue'
            # )


            # first_category = soup. select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(2) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            # )

            # second_category = soup. select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(3) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            # )

            # third_category = soup. select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(4) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            # )

            # fourth_rating = soup. select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(5) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            # )

            # fifth_rating = soup. select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(6) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            # )

            # sixth_rating = soup. select(
            #     '#body > div > div.d-flex.row.page-container > div.col.col-main > div:nth-of-type(7) > div > div.row.profile-match-overview-header > div.col-lg-2 > a.profile-match-title.text-uppercase'
            # )


            # if third_rating == []:
            #     if second_rating == []:
            #         data.append({
            #             user: {first_category[0].text : first_rating[0].text}
            #         })
            #     else:
            #         data.append({
            #             user: {
            #                 first_category[0].text : first_rating[0].text,
            #                 second_category[0].text: second_rating[0].text
            #             }
            #         })
            # else:
            #     data.append({
            #         user: {
            #             first_category[0].text : first_rating[0].text,
            #             second_category[0].text: second_rating[0].text,
            #             third_category[0].text: third_rating[0].text,
            #         }
            #     })
            
            data.append({
                user: ratings
            })

        return data

    def dbSave(self):
        rating_data = self.parse_rating()
        print(rating_data)
        # if self.SAVE_COUNT > 5:
        for arr in rating_data:
            for user, rating in arr.items():
                print(user)
                print(rating.get('solo'))
                print(rating.get('duo'))
                print(rating.get('squad'))
                    # RatingData(userName=user, solo=rating.get('solo'), duo=rating.get('duo'), squad=rating.get('squad')).save()
            # self.SAVE_COUNT = 0
        # self.SAVE_COUNT += 1
        # threading.Timer(CRAWLER_TIME + random.randrange(1,5), self.dbSave).start()

if __name__=='__main__':
    p = Paser(0)
    p.dbSave()