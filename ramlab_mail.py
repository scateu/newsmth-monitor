# -*- coding:utf8
import smtplib
from email.mime.text import MIMEText
from email.Header import Header

class ramlab_mail():
    """
    Library to sendmail from ramlab_things@126.com
    see sendmail()
    """
    def __init__(self):
        self.email_user = "ramlab_things@126.com"
        self.email_password = "Hallelujah2193@~"
    def sendmail(self,to,subject,message):
        """
        to = 'scateu@gmail.com'
        subject = 'blahblah'
        message = 'blahblah'
        m = ramlab_mail()
        m.sendmail(to='scateu@gmail.com',subject='blah',message='bye.')
        """
        self.smtpserver = smtplib.SMTP("smtp.126.com",25)
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
    m = ramlab_mail()
    m.sendmail(to='scateu@gmail.com',subject=u'中文邮件',message=u'哈哈')
