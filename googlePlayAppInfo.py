#!/usr/bin/env python
#coding=utf-8

import sys
from lxml import html as H
from optparse import OptionParser 
from sqlalchemy import Column, String, create_engine, Integer, or_, text, exists
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
import requests

Base = declarative_base()
engine = create_engine('sqlite:///gpinfo.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

class GPinfo(Base):
	__tablename__ = "gpinfo"
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(100))
	reviews_num = Column(String(100))
	category = Column(String(100))
	score = Column(String(100))
	numDownloads = Column(String(100))
	datePublished = Column(String(100))
	current_version = Column(String(100))
	developers = Column(String(100))
	requires_android = Column(String(100))
	provider = Column(String(100))
	website = Column(String(256))
Base.metadata.create_all(engine)

if len(sys.argv)<2:
	print "Usage: %s [appid]" % sys.argv[0]
	exit(1)

appid =  sys.argv[1]

html = requests.get("https://play.google.com/store/apps/details?id=%s" % appid).text


ht = H.fromstring(html)

xpaths = {
	"name":"//span[@itemprop='name']/text()",
	"reviews_num":"//span[@class='reviews-num']/text()",
	"category":"//span[@itemprop='genre']/text()",
	"score":"//div[@class='score']/text()",
	"numDownloads":"//div[@itemprop='numDownloads']/text()",
	"datePublished":"//div[@itemprop='datePublished']/text()",
	"current_version":"//div[@itemprop='softwareVersion']/text()",
	"developers":"//span[@itemprop='name']/text()",
	"requires_android":"//div[@itemprop='operatingSystems']/text()"
}

result = {

}

for xp in xpaths:
	result[xp] = ht.xpath(xpaths[xp])[0]

y = ht.xpath("//div[@class='details-section-contents']/div[@class='meta-info']")
for x in y:
	if u"提供者" in x.text_content():
		result["provider"] = x.getchildren()[1].text_content()[0]
	if u"开发者" in x.text_content():
		result["website"] = x.getchildren()[1].getchildren()[0].attrib["href"]

# print repr(result)
session.add(GPinfo(**result))
session.commit()