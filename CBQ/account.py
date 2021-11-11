import time
import json
import base64
import requests
import hmac
import hashlib


class CoinbaseAccount:
    def __init__(self, API_KEY, API_SECRET, API_PASSPHRASE):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.API_PASSPHRASE = API_PASSPHRASE
        self.BASE_PATH = "https://api.exchange.coinbase.com"

    def create_request(self, method, path, body=""):

        timestamp = str(int(time.time()))

        if method == "GET":
            body = ""
        else:
            body = json.dumps(body)

        message = timestamp + method + path + body

        message = message.encode('utf-8')
        hmac_key = base64.b64decode(self.API_SECRET)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')

        headers = {
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.API_KEY,
            'CB-ACCESS-PASSPHRASE': self.API_PASSPHRASE,
            'Content-Type': 'application/json'
        }

        fullpath = self.BASE_PATH + path

        if method == "GET":
            r = requests.get(fullpath, headers=headers)
        else:
            r = requests.get(fullpath, headers=headers, data=body)
        return r

