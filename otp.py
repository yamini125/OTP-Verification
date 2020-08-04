import random
from twilio.rest import Client
otp=random.randint(10000,100000)

account_sid='ACf316d0803364c78eff7c5a01e198d0da'
auth_token='b9872cb4310a9f7b1b960f1759b02e02'
client=Client(account_sid,auth_token)
client.messages.create(from_='+12057934385',to='+918825859851',body=str(otp))
aaa=int(input())
print('enter generated otp')
if(otp == aaa):
    print("permission granted")
else:
    print("access denied")   

