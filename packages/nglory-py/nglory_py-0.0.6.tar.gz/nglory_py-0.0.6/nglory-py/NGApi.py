import requests

class NGApi:
    token = ""
    _URL = "https://publicapi.nationsglory.fr/"
    headers = {}

    _endpoints = {
        "Country": "country/",
        "Notations": "notations?",
        "User": "user/",
        "Market": "hdv/../list",
        'ServerCount': "playercount",
        "Planning" : "planning",
        "NGIslands" : "ngisland/list"
    }

    def __init__(self, token):
        self.token = token

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def getToken(self):
        return self.token

    def getEndpoint(self, key):
        return self._endpoints[key]

    def ngEndpoint(self, end_point):
        return self._URL + end_point


    def getResponse(self, end_point):
        return requests.get(self.ngEndpoint(end_point), headers=self.headers)
