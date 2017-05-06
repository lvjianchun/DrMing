from wit import Wit

class wit_query_agent():

    def __init__(self, access_token=None):
        self.access_token = access_token
        if self.access_token is None:
            access_token =  "DPYDYGBHRU4VMFCP4XR2YPYEFNS2YYJ4"
        self.client = Wit(access_token=access_token, actions={})
        pass

    def send(self, text):
        resp = self.client.message(text)
        print(str(resp))
        return resp



