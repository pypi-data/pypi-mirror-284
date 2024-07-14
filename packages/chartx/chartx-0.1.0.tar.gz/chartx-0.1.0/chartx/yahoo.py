import pandas as pd
from pandas_datareader import data as pdr
import yfinance

yfinance.pdr_override()


def price(ticker: str):
    return pdr.get_data_yahoo(ticker)
