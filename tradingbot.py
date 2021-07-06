import click, json
import robin_stocks as rh

@click.group()
def main():
    login()

def login():
    content = open('config.json').read()
    config = json.loads(content)
    rh.login(config["username"], config["password"])

@main.command(help='Get a stock quote for one or more symbols')
@click.argument('symbols', nargs=-1)
def quote(symbols):
    quotes = rh.get_quotes(symbols)

    for quote in quotes:
        print(f"{quote['symbol']} | Ask: {quote['ask_price']} | Bid: {quote['bid_price']}")

@main.command(help='Gets quotes for all stocks in your watchlist')
def watchList():
    print("Getting quotes from watchlist")
    with open('watchlist') as f:
        symbols = f.read().splitlines()
    
    quotes = rh.get_quotes(symbols)
    for quote in quotes:
        print(quote)

@main.command(help="Buy quantity of stock by symbol")
@click.argument('quantity', type=click.INT)
@click.argument('symbol', type=click.STRING)
@click.option('--limit', type=click.FLOAT)
def buy(quantity, symbol, limit):
    if limit is not None:
        click.echo(click.style(f"Buying {quantity} of {symbol} at {limit}", fg="green", bold=True))
        result = rh.order_buy_limit(symbol, quantity, limit)
    else:
        click.echo(click.style(f"Buying {quantity} of {symbol} at {limit}", fg="green", bold=True))
        result = rh.order_buy_market(symbol, quantity)
    
    print(result)

@main.command(help="Sell quantity of stock by symbol")
@click.argument('quantity', type=click.INT)
@click.argument('symbol', type=click.STRING)
@click.option('--limit', type=click.FLOAT)
def sell(quantity, symbol, limit):
    if limit is not None:
        click.echo(click.style(f"Selling {quantity} of {symbol} at {limit}", fg="red", bold=True))
        result = rh.order_sell_limit(symbol, quantity, limit)
    else:
        click.echo(click.style(f"Selling {quantity} of {symbol} at {limit}", fg="red", bold=True))
        result = rh.order_sell_market(symbol, quantity)
    
    print(result)


if __name__ == "__main__":
    main()