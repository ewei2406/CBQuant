const WebSocket = require('ws')
const fs = require('fs')

// TICKER DATA
const product = process.argv.slice(2)[0] || "BTC-USD"
console.log(product);

const ticker = new WebSocket('wss://ws-feed.exchange.coinbase.com');

ticker.on('open', () => {
    ticker.send(JSON.stringify({
        "type": "subscribe",
        "channels": [{ "name": "ticker", "product_ids": [product] }]
    }))
})

let tickerWriter = fs.createWriteStream(`./temp/${product}-ticker.csv`)
tickerWriter.write(
    `product,date,price,volume,best_bid,best_ask\n`
)

ticker.on('message', (message) => {
    message = JSON.parse(message)
    // console.log(message)

    if (message.price) {

        let date = new Date(message.time).valueOf()

        tickerWriter.write(
            `${product},${date},${message.price},${message.last_size},${message.best_bid},${message.best_ask}\n`
        )
        console.log(message.price)
    }
})