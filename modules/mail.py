import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


fromEmail = 'trial.samoyard@gmail.com'
fromEmailPassword = "QmxhY2twZWFybDI3"
toEmail = 'qodim.is30@gmail.com'


def sendEmail(image):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Security Update'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'Raspberry pi security camera update'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('Smart security cam found object')
    msgAlternative.attach(msgText)

    msgText = MIMEText('<img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)

    msgImage = MIMEImage(image)
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    tes = "QmxhY2twZWFybDI3"
    tes = tes.encode('ascii')
    p = base64.b64decode(tes)
    p = p.decode('ascii')

    smtp.login(fromEmail, p)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()
