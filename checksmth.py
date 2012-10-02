#-*- coding:utf8
import feedparser
import time


CheckedLinks = []
def check(BoardName,KeyWords):
    global CheckedLinks
    result = []
    URL = 'http://www.newsmth.net/nForum/rss/board-'+BoardName
    feed = feedparser.parse(URL)
    for i in feed.entries:
        for k in KeyWords:
            if (i.title.lower().find(k.lower()) != -1) or (i.description.lower().find(k.lower()) != -1):
                desc = i.description.replace('<br />','\n').replace('&nbsp;',' ')
#                print i.title
#                print desc
#                print i.link
                if i.link not in CheckedLinks:
                    result.append('\n'.join([desc,i.link]))
                    CheckedLinks.append(i.link)
    return result

def countdown(sec=10):
    print u'Sleep...',
    while sec >= 0:
        print sec,
        time.sleep(1)
        sec -= 1
    print

def main():
    BoardName = 'HouseRent'
    KeyWords = [u'清华']
    while True:
        if check(BoardName,KeyWords):
            print u'找到了~'
        else:
            print u'啥都没...'
        countdown(10)

if __name__ == "__main__":
    main()
