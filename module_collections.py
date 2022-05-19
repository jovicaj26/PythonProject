import collections
from collections import Counter


def count_grades(df):
    c = Counter(df["Grade"])
    print(c.most_common(5))


# Calculate the average maximum and average minimum for each grade.
def average_grades_score(df):
    grades = "ABCDF"
    for grade in grades:
        dx = df[df["Grade"] == str(grade)]
        df2 = dx[["MinScore", "MaxScore"]].mean()
        print(f"Grade {grade} average MinScore is: {df2['MinScore']}")
        print(f"Grade {grade} average MaxScore is: {df2['MaxScore']}")
