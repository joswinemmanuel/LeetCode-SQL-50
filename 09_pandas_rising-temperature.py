import pandas as pd

data = [
    [1, '2015-01-01', 10],
    [2, '2015-01-02', 25],
    [3, '2015-01-03', 20],
    [4, '2015-01-04', 30]

]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype(
    {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'}
)


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['prev_date'] = weather['recordDate'] - pd.Timedelta(days=1)
    print(weather)
    merged = pd.merge(
        weather,
        weather,
        left_on='prev_date',
        right_on='recordDate',
        suffixes=('_today', '_yesterday')
    )
    
    return merged


print(rising_temperature(weather))
