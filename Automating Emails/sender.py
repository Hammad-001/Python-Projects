import smtplib, ssl ,getpass

port = 465
password = getpass.getpass("Type Your Password: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login("fordevpurpose1@gmail.com", password)

