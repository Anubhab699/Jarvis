import os
import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC143bcbd3d6cd7df067e16aff7936bbe2']
auth_token = os.environ['363ad54bccc7f0383dd4650dedd1e13d']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+15558675310',
                        from_='+15017122661'
                    )

print(call.sid)