import requests


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        params = {
            "corpid": "wwbf5bbb0bc23e75c1",
            "corpsecret": "j9EAgkj73oWg2tZ-vdsJipfUdXIVWTAuCQIEMZU5rMI"
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params=params)
        return r.json()['access_token']

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
