from CBQ import account
import os

def test_account_creation():
    API_PASSPHRASE = os.environ['API_PASSPHRASE'].strip('"')
    API_KEY = os.environ['API_KEY'].strip('"')
    API_SECRET = os.environ['API_SECRET'].strip('"')

    acc = account.CoinbaseAccount(
        API_KEY,
        API_SECRET,
        API_PASSPHRASE,
        is_sandbox=True
    )

    assert acc.API_KEY == API_KEY
    assert acc.API_SECRET == API_SECRET
    assert acc.API_PASSPHRASE == API_PASSPHRASE
    assert acc.BASE_PATH == "https://api-public.sandbox.exchange.coinbase.com"