#-*- coding:utf8
"""
 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2013 scateu <scateu@gmail.com>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

"""
import feedparser
import time
import mysmtp
from optparse import OptionParser



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
    parser = OptionParser()
    parser.add_option("-b","--board",dest="BoardName",help="The BoardName to be watched")
    parser.add_option("-k","--keywords",dest="KeyWords",type="string",help="Words to be watched (no space, comma splited)")
    parser.add_option("-m","--mail-to",dest="MailTo",help="Notify e-mail address when found, one email address only.")
    parser.add_option("-i","--interval",dest="Interval",type="int",help="Check interval, default = 10 sec")

    (options,args) = parser.parse_args()

    if not options.BoardName or not options.KeyWords:
        print "args not given"

    try:
        BoardName = options.BoardName
        KeyWords =  [i.decode('utf8') for i in options.KeyWords.split(',')]
    except:
        print "Args Error."
        return

    while True:
        monitor_string = u'SMTH监控: %s KeyWords:%s'%(BoardName,','.join(KeyWords))

        print monitor_string
        result = check(BoardName,KeyWords)
        if result:
            print u'找到了~'
            msg = u'\n\n\n\n\n\n\n*********苦逼分隔线*************\n\n'.join(result)
            print msg
            if options.MailTo:
                m.sendmail(to=options.MailTo,subject=monitor_string,message=msg)
            else:
                print "No Email Address"
        else:
            print u'没啥新的...'
        if options.Interval:
            countdown(options.Interval)
        else:
            countdown(10)

if __name__ == "__main__":
    m = mysmtp.mymail()
    m.email_user = "someone@126.com"
    m.email_password = "somepassword"
    m.email_server = "smtp.126.com"
    main()
