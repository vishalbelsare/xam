import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd

from xam.tsa import FrequencyAverageForecaster


df = pd.read_csv('data/bike-station.csv')

series = pd.Series(
    data=df['bikes'].tolist(),
    index=pd.to_datetime(df['moment'], format='%Y-%m-%d %H:%M:%S')
)

forecaster = FrequencyAverageForecaster(lambda d: f'{d.weekday()}-{d.hour}')
forecaster.fit(series)
forecasts = forecaster.predict(series.index)

forecaster.predict(series.index)

series[-300:].plot()
forecasts[-300:].plot(drawstyle='steps-post')

plt.show()
