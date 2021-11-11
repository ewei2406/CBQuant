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
![image](https://user-images.githubusercontent.com/34495421/141376463-0e11b665-52c3-4239-95f1-0db6a4728ef0.png)

### Get the order book for a product pair
```python
from CBQ import visualizations

book = acc.get_book("DOGE-USD")

visualizations.show_book(b, 100, "DOGE-USD")
plt.show()
```
![image](https://user-images.githubusercontent.com/34495421/141377805-fe9177c7-b971-459c-9558-a7dd3bed6731.png)

