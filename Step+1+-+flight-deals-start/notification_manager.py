from twilio.rest import Client

account_sid = "AC3461b488eda6e20a07bcc8d2b267fffa"
auth_token = "0c4aab5f2f0e5de61791601525dd82ea"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_whatsapp_message(self, text_message):
        message = self.client.messages.create(
            body={text_message},
            from_="whatsapp:+14155238886",
            to="whatsapp:+6282213861808",
        )

        print(message.status)