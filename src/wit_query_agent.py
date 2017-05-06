import sys
from wit import Wit

access_token = sys.argv[1]

def send(request, response):
    print(response['text'])

actions = {
    'send': send,
}

client = Wit(access_token=access_token, actions=actions)
resp = client.message(sys.argv[2])

print('Yay, got Wit.ai response: ' + str(resp))
