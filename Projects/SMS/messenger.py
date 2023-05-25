import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello World.",
                     from_='+18889251505',
                     to='+14058303221'
                 )

print(f'Date Created: {message.date_created}, Date Updated: {message.date_updated}')