import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from helpers import download_csv

_US_STATES_DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
_INFLUENZA_DATA_URL = 'https://data.cdc.gov/api/views/ks3g-spdg/rows.csv?accessType=DOWNLOAD'
_WORLD_DATA_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


def q1():
    pass


def q2():
    us_states_df = pd.read_csv('us_states_data.csv')
    # us_states_df = download_csv(_US_STATES_DATA_URL)

    # DataFrame for Minnesota cases; convert to Time Series
    minnesota_mask = us_states_df['state'] == 'Minnesota'
    minnesota = us_states_df[minnesota_mask]
    minnesota.index = pd.to_datetime(minnesota['date'])

    # Replace dates with numeric counter for use in regression model training
    minnesota_numeric = minnesota.assign(date=range(len(minnesota)))

    # Linear Regression
    pre_floyd = minnesota_numeric.loc[:'2020-05-25']
    pre_floyd_x, pre_floyd_y = pre_floyd[['date']], pre_floyd['cases']

    model = LinearRegression(fit_intercept=False)
    model.fit(pre_floyd_x, pre_floyd_y)
    pred = model.predict(minnesota_numeric[['date']])

    pred_df = pd.DataFrame({'predictions': pred})
    pred_df.index = minnesota.index

    fig, ax = plt.subplots(1)
    minnesota['cases'].plot(ax=ax, ylim=0)
    pred_df.plot(ax=ax, ylim=0)
    ax.set_title('Minnesota Cases')

    fig.savefig('minnesota_cases.png')


def q3():
    pass


def q4():
    pass


def q5():
    pass


def main():
    q1()
    q2()
    q3()
    q4()
    q5()


if __name__ == '__main__':
    main()
