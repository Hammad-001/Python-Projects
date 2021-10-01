import smtplib, ssl ,getpass

def SendMail(message, Receipient, Sender=None, Password=None, Port=None):
    port = 465 if Port == None else Port
    password = getpass.getpass("Type Your Password: ") if Password == None else Password
    sender = "YourDevEmail@gmail.com" if Sender == None else Sender
    receiver_List = isinstance(Receipient, (list, tuple))
    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
            server.login(sender, password)
            if receiver_List:
                for receiver in Receipient:
                    server.sendmail(sender, receiver, message)
            else:
                server.sendmail(sender, Receipient, message)
        return True
    except Exception as e:
        print("MAIL IS NOT SENT BECAUSE:", e)
        return False
