import os
from twilio.rest import Client

account_sid = 'ACfb7be0944c6ac943c3d884fa14f6cb08'
auth_token = 'be2b5a982d1be29b79f4841201c50856'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8201049456804", 
    from_="+14076413470",
    body="보내고자하는 텍스트를 적어주세요")

print(message.sid)