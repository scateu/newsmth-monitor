# -*- coding:utf8
"""
 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2012 Romain Lespinasse <romain.lespinasse@gmail.com>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

"""
import smtplib
from email.mime.text import MIMEText
from email.Header import Header

class mymail():
    """
    Library to sendmail 
    see sendmail()
    """
    def __init__(self):
        self.email_user = None
        self.email_password = None
        self.email_server = "smtp.126.com"
        self.email_smtp_port = 25
    def sendmail(self,to,subject,message):
        self.smtpserver = smtplib.SMTP(self.email_server,self.email_smtp_port)
        self.smtpserver.ehlo()
        self.smtpserver.starttls()
        self.smtpserver.ehlo
        self.smtpserver.login(self.email_user, self.email_password)
        msg = MIMEText(message,'plain',_charset="UTF-8")
        msg['To'] = to
        msg['From'] = self.email_user
        msg['Subject'] = Header(subject,"UTF-8")
        self.smtpserver.sendmail(msg['From'],msg['To'],msg.as_string())
        print 'email sent.'
        self.smtpserver.close()

if __name__ == "__main__":
    m = mymail()
    m.email_user = "blahblah@126.com"
    m.email_password = "somepassword"
    m.email_server = "smtp.126.com"
    m.email_smtp_port = 25
    m.sendmail(to='scateu@gmail.com',subject=u'中文邮件',message=u'哈哈')
