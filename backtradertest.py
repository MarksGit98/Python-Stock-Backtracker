import backtrader as bt
import datetime
from strategies import TestStrategy

cerebro = bt.Cerebro()

cerebro.broker.set_cash(1000000)

data = bt.feeds.YahooFinanceCSVData(
    dataname='oracle.csv',
    fromdate=datetime.datetime(2000, 1, 1),
    todate=datetime.datetime(2000, 12, 31),
    reverse=False
)

cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()