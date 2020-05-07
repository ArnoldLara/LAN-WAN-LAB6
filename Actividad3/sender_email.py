import smtplib, ssl

port = 587  # For startTLS
smtp_server = "smtp.gmail.com"
sender_email = "lanwan202010@gmail.com"  # Enter your address
password = "linux_Pass"



def envio_email(receiver_email_attr, gluc_attr, temp_attr, spo2_attr):
    receiver_email = receiver_email_attr
    gluc = gluc_attr
    temp = temp_attr
    spo2 = spo2_attr
    # message = """\
    # Subject: Alerta de signos vitales
    #
    # This message is sent from Python."""

    SUBJECT = 'Alerta de signos vitales'
    TEXT=gluc+'\n'+temp+'\n'+spo2

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)


    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        print(server.login(sender_email, password))
        print("Correo electronico enviado satifactoriamente")
    return 'OK'
