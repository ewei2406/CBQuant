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

    def create_request(self, method, path, add_headers=None, body=""):

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

        if add_headers:
            headers.update(add_headers)

        fullpath = self.BASE_PATH + path

        if method == "GET":
            r = requests.get(fullpath, headers=headers)
        else:
            r = requests.get(fullpath, headers=headers, data=body)
        return r

    def get_wallets(self):
        res = self.create_request(
            'GET', '/accounts')


        res = json.loads(res.content)
        account = []

        for acc in res:
            bal = float(acc["balance"])
            if bal > 0:
                account.append({
                    "amount": bal,
                    "label": acc["currency"]
                })

        for curr in account:
            if curr['label'] != 'USD':
                res = self.create_request(
                    'GET', f"/products/{curr['label']}-USD/ticker")
                curr['price'] = float(json.loads(res.content)['price'])

                print(f"Price of {curr['label']}: {curr['price']}")
            else:
                curr['price'] = 1

            usd = curr['price'] * curr['amount']

            curr['usd'] = usd

        total = sum([c["usd"] for c in account])

        for curr in account:
            curr["percentage"] = curr["usd"] / total
        
        return account

    def get_book(self, pair):
        r = self.create_request("GET", f"/products/{pair}/book?level=2")
        return r


if __name__ == "__main__":
    import secrets

    acc = CoinbaseAccount(
        API_KEY=secrets.API_KEY,
        API_SECRET=secrets.API_SECRET,
        API_PASSPHRASE=secrets.API_PASSPHRASE)

    r = acc.get_book("DOGE-USD")
    print(r.content)
