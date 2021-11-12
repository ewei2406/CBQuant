from CBQ import account

def test_account_creation():
    acc = account.CoinbaseAccount(
        API_KEY=secrets.API_KEY,
        API_SECRET=secrets.API_SECRET,
        API_PASSPHRASE="11111111111")
