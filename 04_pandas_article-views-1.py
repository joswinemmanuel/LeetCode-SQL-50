import pandas as pd

data = [
    [1, 3, 5, '2019-08-01'],
    [1, 3, 6, '2019-08-02'],
    [2, 7, 7, '2019-08-01'],
    [2, 7, 6, '2019-08-02'],
    [4, 7, 1, '2019-07-22'],
    [3, 4, 4, '2019-07-21'],
    [3, 4, 4, '2019-07-21']
]

views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
    {'article_id': 'Int64', 'author_id': 'Int64',
        'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'}
)


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = views['author_id'].eq(views['viewer_id'])
    return views.loc[mask, ['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates().sort_values(by='id')


print(article_views(views))
