def add_pass_column(df):
    """
    Add Pass column, with value [True, False], depend of value
    from colum MinScore.
    """
    df["Pass"] = df["MinScore"] >= 15


def get_grade(avg, passed):
    """
    Calculate grade according to average score and passed boolean
    """
    if passed:
        if avg > 60:
            return "A"
        elif 50 < avg <= 60:
            return "B"
        elif 40 < avg <= 50:
            return "C"
        else:
            return "D"
    else:
        return "F"


def add_grade_column(df):
    """
    Add Grade column, with value [A, B, C, D, F], depend of value
    from columns Pass and AvgScore.
    """
    grade = []
    for x in df.index:
        grade.append(get_grade(df.loc[x, "AvgScore"], df.loc[x, "Pass"]))

    df2 = df["Grade"] = grade
    return df2


def grade_gender_dependency(df):
    df[["Sex", "Grade"]].value_counts().plot(kind="bar")


def show_negative_minimal_scores(df):
    """
    Calculate and return number of negative minimum scores
    and data frame containing only rows with 'F'.
    """
    sh = df[df["Grade"] == "F"].shape
    num = sh[0]
    print(df[df["Grade"] == "F"])
    print(f"Number of negative grades is: {num}")
