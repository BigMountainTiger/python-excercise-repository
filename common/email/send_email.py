import os
import smtplib
from email.message import EmailMessage

sender = os.environ['sender']
sender_pwd = os.environ['sender_pwd']
recipient = os.environ['recipient']

html_content = """
<html>
  <body>
    <h1>Hello, World!</h1>
    <p>This is an <b>HTML</b> email sent from a Python script.</p>
    <p>It includes a link to a website: <a href="https://example.com">Example.com</a></p>
  </body>
</html>
"""

msg = EmailMessage()
# msg.set_content(html_content)
msg.add_alternative(html_content, subtype="html")
msg['Subject'] = 'Subject of the Email'
msg['From'] = sender
msg['To'] = recipient

print('sending email ...')

smtp_server = 'smtp.gmail.com'
with smtplib.SMTP_SSL(smtp_server, 465) as smtp:
    smtp.login(sender, sender_pwd)
    smtp.send_message(msg)

    print("Email sent successfully!")
