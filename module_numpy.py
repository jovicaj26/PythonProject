import numpy as np


def sort_grades(df):
    grades_array = np.array(df["Grade"])
    print(np.sort(grades_array))
