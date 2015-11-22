#!/usr/bin/env python
#coding=utf-8

categories = [
    "BOOKS_AND_REFERENCE",#Books & Reference
    "BUSINESS",#Business
    "COMICS",#Comics
    "COMMUNICATION",#Communication
    "EDUCATION",#Education
    "ENTERTAINMENT",#Entertainment
    "FINANCE",#Finance
    "GAME",#Games
    "HEALTH_AND_FITNESS",#Health & Fitness
    "LIBRARIES_AND_DEMO",#Libraries & Demo
    "LIFESTYLE",#Lifestyle
    "APP_WALLPAPER",#Live Wallpaper
    "MEDIA_AND_VIDEO",#Media & Video
    "MEDICAL",#Medical
    "MUSIC_AND_AUDIO",#Music & Audio
    "NEWS_AND_MAGAZINES",#News & Magazines
    "PERSONALIZATION",#Personalization
    "PHOTOGRAPHY",#Photography
    "PRODUCTIVITY",#Productivity
    "SHOPPING",#Shopping
    "SOCIAL",#Social
    "SPORTS",#Sports
    "TOOLS",#Tools
    "TRANSPORTATION",#Transportation
    "TRAVEL_AND_LOCAL",#Travel & Local
    "WEATHER",#Weather
    "APP_WIDGETS",#Widgets
]


import requests
from lxml import html as H 
from urlparse import urlparse,parse_qs



for cat in categories:
    data = {
        "start" : 0,
        "number": 60,
        "token" : "v9gtze_L-6ptX6_OE4C603pikN8:1447050625753"
    }

    for i in range(0,500,60):
        data["start"] = i
        html = requests.post("https://play.google.com/store/apps/category/%s/collection/topselling_free" % (cat), data=data).text
        tree = H.fromstring(html)

        r = tree.xpath(r"//a[@class='title']")
	for ele in r:
		qs = parse_qs(urlparse(ele.get('href')).query)
		apkid = qs["id"]
		number = ele.text.split()[0].strip().rstrip(".")

		print apkid, number

