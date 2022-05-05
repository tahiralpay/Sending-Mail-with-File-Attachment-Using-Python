"""
                       KASIM 2020 TALPAY                  
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

    username = "tahiralpay98@gmail.com"
    password = "161101045"
    mail_adress_to_send = "tahiralpay.mdbf16@iste.edu.tr"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    
    def send_mail( send_from, send_to, subject, text, file, isTls=True):
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = "".join(send_to)
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject
        msg.attach( MIMEText(text) )
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
        msg.attach(part)  
        server.sendmail(send_from, send_to, msg.as_string())
   
    send_from = ""
    subject = "UYARI"
    text = """
    Hareket Algılandı.
    """

    fileName = "/home/pi/Desktop/foto.jpg"
    send_mail(send_from, mail_adress_to_send, subject, text, fileName, isTls = True)
    print("mail foto başarıyla gönderildi")
    server.quit()
