# CBQuant

Coinbase Quantitative Trading library

## Setup
Install requirements
```bash
pip install -r requirements.txt
```
Import the library
```python
import CBQ
```

## Usage
### Create an Coinbase Account object using API credentials
```python
from CBQ import account

acc = account.CoinbaseAccount(
    API_KEY=YOUR_API_KEY,
    API_SECRET=YOUR_API_SECRET,
    API_PASSPHRASE=YOUR_API_PASSPHRASE)
```
### Show the distribution of capital for all wallets in a portfolio
```python
from CBQ import visualizations

wallets = acc.get_wallets()

visualizations.show_pie(wallets)
plt.show()
```
<img src="images/Portfolio_Pie.png" alt="drawing" width="500"/>

### Get the order book for a product pair
```python
from CBQ import visualizations

book = acc.get_book("DOGE-USD")

visualizations.show_book(b, 100, "DOGE-USD")
plt.show()
```
<img src="images/DOGE_USD_Book.png" alt="drawing" width="500"/>

---

## Testing
Using `pytest`
```python
pytest CBQ
```
