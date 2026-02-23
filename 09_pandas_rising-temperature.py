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


# def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
#     weather['prev_date'] = weather['recordDate'] - pd.Timedelta(days=1)

#     merged = pd.merge(
#         weather,
#         weather,
#         left_on='prev_date',
#         right_on='recordDate',
#         suffixes=('_today', '_yesterday')
#     )

#     result = merged[
#         merged['temperature_today'] > merged['temperature_yesterday']
#     ][['id_today']]

#     return result.rename(columns={'id_today': 'Id'})

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')
    weather['prev_date'] = weather['recordDate'].shift(1)
    weather['prev_temperature'] = weather['temperature'].shift(1)
    result = weather[
        (weather['recordDate'] - pd.Timedelta(days=1) == weather['prev_date'])
        &
        (weather['temperature'] > weather['prev_temperature'])
    ][['id']]
    return result.rename(columns={'id': 'Id'})


print(rising_temperature(weather))
