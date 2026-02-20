import pandas as pd

data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'],
        [90, 'Winston'], [3, 'Jonathan']]
employees = pd.DataFrame(data, columns=['id', 'name']).astype(
    {'id': 'int64', 'name': 'object'})
data = [[3, 1], [11, 2], [90, 3]]
employee_uni = pd.DataFrame(data, columns=['id', 'unique_id']).astype({
    'id': 'int64', 'unique_id': 'int64'})

def replace_employee_id(employee: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, employee_uni, how="left", on="id")
    return merged.loc[:, ["unique_id", "name"]]


print(replace_employee_id(employees, employee_uni))
