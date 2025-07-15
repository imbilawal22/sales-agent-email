
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

load_dotenv()

def send_email(to_email, body):
    sg = SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    from_email = Email(os.getenv("EMAIL_ADDRESS"))
    to_email = To(to_email)
    content = Content("text/plain", body)

    mail = Mail(from_email, to_email, "Sales Email", content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
