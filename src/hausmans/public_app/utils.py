from gmail import GMail, Message
from django.conf import settings

def send_email(first_name, last_name, email_address, message):
    message_body = f"First Name: {first_name}\nLast Name: {last_name}\n\nEmail address: {email_address}\n\nMessage:\n{message}"

    gmail = GMail(settings.APPLICATION_GMAIL_ADDRESS, settings.APPLICATION_GMAIL_PASSWORD)
    msg = Message(
        subject="New 'Contact Us' Submission on hausmans.com",
        to=settings.CONTACT_US_RECIPIENT_EMAIL_ADDRESS,
        text=message_body
    )
    gmail.send(msg)
