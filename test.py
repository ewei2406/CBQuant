from CBQ import account
import secrets
import json


acc = account.CoinbaseAccount(
    API_KEY=secrets.API_KEY, 
    API_SECRET=secrets.API_SECRET,
    API_PASSPHRASE=secrets.API_PASSPHRASE)


res = acc.get_wallets()
print(res)
