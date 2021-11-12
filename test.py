import matplotlib.animation as animation
from CBQ import account
from CBQ import visualizations
import secrets
import json
import matplotlib.pyplot as plt


acc = account.CoinbaseAccount(
    API_KEY=secrets.API_KEY,
    API_SECRET=secrets.API_SECRET,
    API_PASSPHRASE=secrets.API_PASSPHRASE)

# wallets = acc.get_wallets()
# visualizations.show_pie(wallets)
# plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    r = acc.get_book("DOGE-USD")

    ax1.clear()
    
    visualizations.show_book(r, 40, "DOGE-USD", fig, ax1)

ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()


# book = acc.get_book("DOGE-USD")
# visualizations.show_book(book=book, depth=100, title="DOGE-USD")
# plt.show()
