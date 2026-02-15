import pandas as pd

data = [
    ['0', 'Y', 'N'],
    ['1', 'Y', 'Y'],
    ['2', 'N', 'Y'],
    ['3', 'Y', 'Y'],
    ['4', 'N', 'N']
]

products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
    {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'}
)


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = products['low_fats'].eq('Y') & products['recyclable'].eq('Y')
    return products.loc[mask, ['product_id']]

print(find_products(products))
