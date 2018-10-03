def formatResponse(info):
    email = 'SPORT: {0}\nEVENT: {3}\nBET: {4} \nODDS: {1}\nSTAKE: {2}\nBOOK: bet365'.format(*info)
    return email

def sendEmail(info):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()


    fromaddr = "goldenbot21@gmail.com"
    toaddr = "kyrleo1@hotmail.com"
    msg = MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Hello world"

    body = formatResponse(info)
    msg.attach(MIMEText.MIMEText(body, 'plain'))

    server.login(fromaddr, "tseli12345")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()