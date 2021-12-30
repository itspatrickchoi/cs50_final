import smtplib
from email.mime.text import MIMEText


def send_mail(username, email, score):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '7a2a345edc6159'
    password = '1bdd4db40d52d4'
    message = f"<h3>Welcome! Here are your account details:</h3><ul><li>Your username: {username}</li><li>Your email: {email}</li><li>Your starting score: {score}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Welcome to PC Dash!'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
