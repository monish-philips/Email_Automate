import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContentHtml, recepientsMailList):
    # create message object
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    # msg.attach(MIMEText(mailContentText, 'plain'))
    msg.attach(MIMEText(mailContentHtml, 'html'))

    # create file attachments
    # for aPath in attachmentFpaths:
    #     # check if file exists
    #     part = MIMEBase('application', "octet-stream")
    #     part.set_payload(open(aPath, "rb").read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition',
    #                     'attachment; filename="{0}"'.format(os.path.basename(aPath)))
    #     msg.attach(part)

    # Send message object as email using smptplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    s.quit()

    # check if errors occured and handle them accordingly
    if not len(sendErrs.keys()) == 0:
        raise Exception("Errors occurred while sending email", sendErrs)


# mail server parameters
smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname = '30monish@gmail.com'
mailPwd = 'lzqkhheamvnxgrum'
fromEmail = '30monish@gmail.com'

# mail body, recepients, attachment files
mailSubject = "test subject"
mailContentHtml = "Hi, this is a test mail. <br/> This is a <b>test</b> mail from python script using an awesome library called <b>smtplib</b>"
recepientsMailList = ["3011mnm@gmail.com"]
# attachmentFpaths = ["smtp.png", "poster.png"]
sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
          mailSubject, mailContentHtml, recepientsMailList)

print("execution complete...")