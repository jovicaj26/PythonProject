def add_pass_column(df):
    df["Pass"] = df["MinScore"] >= 15


def add_grade_column(df):
    grade = []
    for x in df.index:
        if df.loc[x, "Pass"]:
            avg = df.loc[x, "AvgScore"]
            if avg > 60:
                grade.append("A")
            elif 50 < avg <= 60:
                grade.append("B")
            elif 40 < avg <= 50:
                grade.append("C")
            elif avg <= 40:
                grade.append("D")
        else:
            grade.append("F")

    df2 = df["Grade"] = grade
    return df2


def grade_gender_dependency(df):
    df[["Sex", "Grade"]].value_counts().plot(kind="bar")


def show_negative_minimal_scores(df):

    df = df[df["Grade"] == "F"]
    sh = df[df["Grade"] == "F"].shape
    num = sh[0]
    return df, num