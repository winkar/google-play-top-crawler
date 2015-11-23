#!/usr/bin/env python


import sys
from lxml import html as H
from optparse import OptionParser 

if len(sys.argv)<2:
	print "Usage: %s [appid]" % sys.argv[0]
	exit(1)

appid =  sys.argv[1]

import requests

html = requests.get("https://play.google.com/store/apps/details?id=%s" % appid).text


ht = H.fromstring(html)

xpaths = {
	"name":"//span[@itemprop='name']/text()",
#	"rating-count":"//span[@class='rating-count']/text()",
	"category":"//span[@itemprop='genre']/text()",
	"score":"//div[@class='score']/text()",
	"numDownloads":"//div[@itemprop='numDownloads']/text()",
	"datePublished":"//div[@itemprop='datePublished']/text()"
}


for xp in xpaths:
	print xp, ht.xpath(xpaths[xp])[0]
