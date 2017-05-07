class responseParser():

    def __init__(self, response):
        self.response = response

    def get(self, key):
        return self.response['entities'][key][0]['value'],  self.response['entities'][key][0]['confidence']

    def has(self, key):
        return key in self.response['entities'].keys() and self.response['entities'][key][0]['confidence'] > 0.50
