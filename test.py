from CBQ import account
import secrets


acc = account.CoinbaseAccount(
    API_KEY=secrets.API_KEY, 
    API_SECRET=secrets.API_SECRET,
    API_PASSPHRASE=secrets.API_PASSPHRASE)


