#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PRICES_DATA = pd.read_csv("house_prices.csv", parse_dates=['date'])


if __name__ == "__main__":
    house_prices = PRICES_DATA[['price','date']]
    house_prices = house_prices.set_index('date')
    house_prices.index = pd.to_datetime(house_prices.index, format='%Y.%m.%d')
    house_prices = house_prices.resample('M').mean()

    house_prices_plot = house_prices.plot(title="House Price by Month",legend=None)

    fig = house_prices_plot.get_figure()
    fig.savefig("out.png")
