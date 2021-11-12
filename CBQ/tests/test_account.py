from CBQ import account
import os

SANDBOX_API_PASSPHRASE = os.environ['SANDBOX_API_PASSPHRASE']
SANDBOX_API_KEY = os.environ['SANDBOX_API_KEY']
SANDBOX_API_SECRET = os.environ['SANDBOX_API_SECRET']

def test_account_creation():
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

def test_get_wallets():
    acc = account.CoinbaseAccount(
        SANDBOX_API_KEY,
        SANDBOX_API_SECRET,
        SANDBOX_API_PASSPHRASE,
        is_sandbox=True
    )

    portfolio = acc.get_wallets()
    assert len(portfolio)
    assert "amount" in portfolio[0]
    assert "label" in portfolio[0]
    assert "price" in portfolio[0]
    assert "usd" in portfolio[0]
    assert "percentage" in portfolio[0]

def test_get_book():
    acc = account.CoinbaseAccount(
        SANDBOX_API_KEY,
        SANDBOX_API_SECRET,
        SANDBOX_API_PASSPHRASE,
        is_sandbox=True
    )

    book = acc.get_book("BTC-USD")

    assert "bids" in book
    assert "asks" in book