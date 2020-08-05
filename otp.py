import random
from twilio.rest import Client
otp=random.randint(10000,100000)

account_sid='ACf316d0803364c78eff7c5a01e198d0da'
auth_token='c1c4f84b798da46647f85c88f051ee88'
client=Client(account_sid,auth_token)
client.messages.create(from_='+12057934385',to='+918825859851',body=str(otp))
aaa=int(input())
print('enter generated otp')
if(otp == aaa):
    print("permission granted")
else:
    print("access denied")   

