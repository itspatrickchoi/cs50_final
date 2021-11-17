import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '7a2a345edc6159'
    password = '1bdd4db40d52d4'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Final Project'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
