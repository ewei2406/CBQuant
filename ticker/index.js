const WebSocket = require('ws')
const fs = require('fs')

// TICKER DATA

const ticker = new WebSocket('wss://ws-feed.exchange.coinbase.com');

ticker.on('open', () => {
    ticker.send(JSON.stringify({
        "type": "subscribe",
        "channels": [{ "name": "ticker", "product_ids": ["BTC-USD"] }]
    }))
})

let tickerWriter = fs.createWriteStream('./data/ticker.csv')
tickerWriter.write(
    `price, date, volume, best_bid, best_ask\n`
)

ticker.on('message', (message) => {
    message = JSON.parse(message)
    // console.log(message)

    if (message.price) {

        let date = new Date(message.time).valueOf()

        tickerWriter.write(
            `${date}, ${message.price},${message.last_size},${message.best_bid},${message.best_ask}\n`
        )
        console.log(message.price)
    }
})