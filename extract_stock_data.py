# Import Packages
import pandas as pd
import yfinance as yf

# interval ('1h', '1d'), period ('max', '1y', '1mo')
# *tickers = ('DHER.DE','O5H.DE', 'DB1.DE')
# **params = (start_date=YYYY-MM-DD, end_date=)
def ext_stock_ohlcv(interval, period, *tickers, **params):

    tickers = pd.DataFrame(tickers, columns=['ticker'])
    # Make n requests and concatenate the results before storing the data
    ohlcv_data = []
    tickers = tickers.ticker.astype(str)
    for ticker in tickers:
            try:
                yf_ticker = yf.Ticker(ticker)
                data = yf_ticker.history(period = period, interval = interval, rounding = True)
                if not data.empty:
                    data['ticker'] = ticker
                    ohlcv_data += [data]
            except:
                print('error on: ' + ticker)

    # Store data
    return pd.concat(ohlcv_data)

# ext_stock_ohlcv('1h', '1y', 'DHER.DE','O5H.DE', 'DB1.DE')
stock_data = ext_stock_ohlcv('1d', 'max', 'DHER.DE','O5H.DE', 'DB1.DE')