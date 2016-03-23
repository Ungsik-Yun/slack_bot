import requests
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import xmltodict
import os
import re
import random


@listen_to("!뉴스 (.*)", re.IGNORECASE)
def search_news(msg, q):
    url = "https://openapi.naver.com/v1/search/news.xml?query="
    url += '"' + q + '"'
    headers = {
        'X-Naver-Client-Id': os.environ['naver_client_id'],
        'X-Naver-Client-Secret': os.environ['naver_client_secret']
    }

    r = requests.get(url, headers=headers)
    result = r.text
    parsed = xmltodict.parse(result)

    for i in parsed['rss']['channel']['item']:
        msg.reply(i['title'])
        msg.reply(i['description'])
        msg.reply(i['link'])
        # msg.reply(i['originallink'])


@listen_to("!지식인 (.*)", re.IGNORECASE)
def search_news(msg, q):
    url = "https://openapi.naver.com/v1/search/kin.xml?query="
    url += '"' + q + '"'
    headers = {
        'X-Naver-Client-Id': os.environ['naver_client_id'],
        'X-Naver-Client-Secret': os.environ['naver_client_secret']
    }

    r = requests.get(url, headers=headers)
    result = r.text
    parsed = xmltodict.parse(result)

    for i in parsed['rss']['channel']['item']:
        msg.reply(i['title'])
        msg.reply(i['description'])
        msg.reply(i['link'])
        # msg.reply(i['originallink'])
