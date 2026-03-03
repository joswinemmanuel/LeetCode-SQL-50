import pandas as pd

data = [
    [1, None],
    [2, 'Bob'],
    [13, 'John'],
    [6, 'Alex']
]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
    {'student_id': 'Int64', 'student_name': 'object'}
)

data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype(
    {'subject_name': 'object'}
)

data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [
    1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype(
    {'student_id': 'Int64', 'subject_name': 'object'}
)

# def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # cross_joined = pd.merge(
    #     students,
    #     subjects,
    #     how='cross'
    # )
    # examinations = examinations.rename(columns={
    #     'student_id': 'student_id_e',
    #     'subject_name': 'subject_name_e'
    # })
    # left_joined = pd.merge(
    #     cross_joined,
    #     examinations,
    #     how='left',
    #     left_on=['student_id', 'subject_name'],
    #     right_on=['student_id_e', 'subject_name_e'],
    # )
    # return left_joined.groupby(['student_id', 'student_name', 'subject_name'], dropna=False)['student_id_e'].count().reset_index(name='attended_exams')
    


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exam')

    return students.merge(subjects, how='cross').merge(exam_count, how='left', on=['student_id', 'subject_name']).fillna({'attended_exam': 0}).astype({'attended_exam': 'int'}).sort_values(['student_id', 'subject_name'])


print(students_and_examinations(students, subjects, examinations))
