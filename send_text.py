#Explain--from module import .py /twilio/rest
from twilio.rest import TwilioRestClient
#Explain--from module twilio import folder rest
#from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC572dd1d0908c56ac5e530e13fde94bdc"
auth_token  = "4b05dc76dec902711963c2ebd082afbf"
client = TwilioRestClient(account_sid, auth_token)
#client = rest.TwilioRestClient(account_sid, auth_token)

 
message = client.messages.create(body="Send by Twilio - Python. Julian",
    to="+573123089218",    # Replace with your phone number
    from_="+14155992671") # Replace with your Twilio number
print message.sid
