from CBQ import account
import os

def test_account_creation():
    SANDBOX_API_PASSPHRASE = os.environ['SANDBOX_API_PASSPHRASE']
    SANDBOX_API_KEY = os.environ['SANDBOX_API_KEY']
    SANDBOX_API_SECRET = os.environ['SANDBOX_API_SECRET']

    acc = account.CoinbaseAccount(
        SANDBOX_API_KEY,
        SANDBOX_API_SECRET,
        SANDBOX_API_PASSPHRASE,
        is_sandbox=True
    )

    assert acc.API_KEY == SANDBOX_API_KEY
    assert acc.API_SECRET == SANDBOX_API_SECRET
    assert acc.API_PASSPHRASE == SANDBOX_API_PASSPHRASE
    assert acc.BASE_PATH == "https://api-public.sandbox.exchange.coinbase.com"
