from twilio.rest import TwilioRestClient

accountId = ''
authToken = ''

twilioCli = TwilioRestClient(accountId,authToken)

fromnum = ''
num = ''

def send(message):
    e = twilioCli.messages.create(body=message,from_=fromnum,to=num)   

def main():
    send('fkjdl')

if __name__ == "__main__":
    main()
