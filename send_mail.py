import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '9ea11babd46d93'
    password = '64d1e25964de25'

    message = f"<h3>New feedback submition</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'robertfedus22@gmail.com'
    receiver_email = 'email1@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())