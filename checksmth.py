#-*- coding:utf8
import feedparser
import time
import ramlab_mail


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
                    result.append(u'\n'.join([desc,i.link]))
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
    KeyWords = [u'清华',u'南门',u'西北小区',u'西北社区',u'五道口',u'校内',u'照澜院']
    m = ramlab_mail.ramlab_mail()

    while True:
        monitor_string = u'SMTH监控: %s KeyWords:%s'%(BoardName,','.join(KeyWords))

        print monitor_string
        result = check(BoardName,KeyWords)
        if result:
            print u'找到了~'
            msg = u'\n'.join(result)
            print msg
            m.sendmail(to='scateu@gmail.com',subject=monitor_string,message=msg)
        else:
            print u'没啥新的...'
        countdown(10)

if __name__ == "__main__":
    main()
