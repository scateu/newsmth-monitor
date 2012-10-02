#-*- coding:utf8
import feedparser
BoardName = 'SecondDigi'
KeyWords = [u'iPhone',u'黑莓',u'Blackberry']

def check(BoardName,KeyWords,interval=60,mailto='scateu@gmail.com'):
    URL = 'http://www.newsmth.net/nForum/rss/board-'+BoardName
    feed = feedparser.parse(URL)
    for i in feed.entries:
        for k in KeyWords:
            if (i.title.lower().find(k.lower()) != -1) or (i.description.lower().find(k.lower()) != -1):
                print i.title
                print i.description.replace('<br />','\n').replace('&nbsp;',' ')
                print i.link
