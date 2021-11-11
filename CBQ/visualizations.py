import matplotlib.pyplot as plt
import pandas as pd


def show_pie(account, fig1=None, ax1=None):

    if not fig1 and ax1:
        fig1, ax1 = plt.subplots()

    labels = [
        f"{c['amount']:.1f} ${c['label']}\n{c['price']:3.2f}:1\n${c['usd']:.1f}" for c in account]

    ax1.pie([c['usd'] for c in account],
            labels=labels,
            autopct='%1.1f%%')

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.set_facecolor('white')

    fig1.suptitle(f"Total Value: ${sum([c['usd'] for c in account]):<.2f}")

    return fig1, ax1


def show_book(book, depth=50, fig1=None, ax1=None):

    if not fig1 and ax1:
        fig1, ax1 = plt.subplots()

    bids = pd.DataFrame(book['bids'])

    bids = bids.astype(float)
    bids = bids.sort_values(by=[0], ascending=False)
    bids["cumulative_coins"] = bids[1].cumsum()
    bids["cumulative_orders"] = bids[2].cumsum()
    bids_f = bids.head(depth)

    ax1.fill_between(x=bids_f[0],
                    y1=bids_f["cumulative_coins"],
                    step="post",
                    color="green",
                    alpha=0.2)

    # ax1.step(x=bids_f[0], y=bids_f["cumulative_coins"],
    #         where="post", color="green")

    asks = pd.DataFrame(book['asks'])
    asks = asks.astype(float)
    asks = asks.sort_values(by=[0], ascending=True)
    asks["cumulative_coins"] = asks[1].cumsum()
    asks["cumulative_orders"] = asks[2].cumsum()
    asks_f = asks.head(depth)

    # ax1.step(x=asks_f[0], y=asks_f["cumulative_coins"],
    #         where="pre", color="red")

    ax1.fill_between(x=asks_f[0],
                    y1=asks_f["cumulative_coins"],
                    step="pre",
                    color="red",
                    alpha=0.2)

    ax1.margins(x=0, y=0)

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    plt.yticks([])

    return fig1, ax1
