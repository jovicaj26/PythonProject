import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def examine_csv(df):

    # create statistics
    print(df["Sex"].describe())
    print(df["Duration"].describe())
    print(df["MinScore"].describe())
    print(df["MaxScore"].describe())
    print()
    print(df[["Sex", "Duration"]].groupby("Sex").mean())
    print(df.groupby("Duration").mean())


def remove_row_if_diff(df, value):
    removed_items = 0
    for x in df.index:
        if df.loc[x, "Duration"] != value:
            df.drop(x, inplace=True)
            removed_items += 1

    return removed_items


def replace_existing_data(df):
    updated_items = 0
    for x in df.index:
        if df.loc[x, "MinScore"] < 0:
            df.loc[x, "MinScore"] = 0
            updated_items += 1
        if df.loc[x, "MaxScore"] > 100:
            df.loc[x, "MaxScore"] = df["MaxScore"].max()
            updated_items += 1

    return updated_items


def replace_not_existing_data(df):
    mean = int(df["MinScore"].mean())
    df["MinScore"].fillna(mean, inplace=True)

    median = int(df["MaxScore"].median())
    df["MaxScore"].fillna(median, inplace=True)

    return mean, median


def read_file(name):
    df = None
    try:
        df = pd.read_csv(name)
    except IOError:
        print("File not accessible.")

    return df


def add_grade_column(df):
    grade = []
    for x in df.index:
        if df.loc[x, "Pass"] is True:
            avg = df.loc[x, "AvgScore"]
            if avg > 50:
                grade.append("A")
            elif avg > 40 and avg <= 50:
                grade.append("B")
            elif avg > 30 and avg <= 40:
                grade.append("C")
            elif avg <= 30:
                grade.append("D")
        else:
            grade.append("F")

    df2 = df["Grade"] = grade
    return df2


def show_negative_minimal_scores(df):

    df = df[df["Grade"] == "F"]
    sh = df[df["Grade"] == "F"].shape
    num = sh[0]
    return df, num


if __name__ == '__main__':

    print("Task 1:")
    df = read_file("dirtydata.csv")
    if df is not None:
        examine_csv(df)
        print()

        print("Task 2:")
        print(f"Number of removed data: {remove_row_if_diff(df, 60)}")
        print(f"Number of replaced data: {replace_existing_data(df)}")
        mean, median = replace_not_existing_data(df)
        print("Not existing data are replaced with:", end="")
        print(f" mean: {mean} and median: {median}")

        print("Deleting rows with not existing data ...")
        df.dropna(subset=['Sex'], inplace=True)

        print("Removing duplicates from table ...")
        df.drop_duplicates(inplace=True)
        print()

        print("Task 3:")
        print("Save data to data.csv.")
        df.to_csv("data.csv", index=False)
        print()

    print("Task 4:")
    df2 = read_file("data.csv")
    if df2 is not None:
        df2["AvgScore"] = (df2["MinScore"] + df2["MaxScore"]) / 2
        print("Part of the new table:")
        print(df2)

        print("Task 5:")
        print(df2["Sex"].value_counts())
        print()

        print("Task 6:")
        print(df2[["Sex", "MinScore"]].groupby("Sex").mean())
        print()
        print(df2[["Sex", "MaxScore"]].groupby("Sex").mean())
        print()

        print("Task 7:")
        df2.plot(x="Sex", y="AvgScore")
        plt.show()
        print()

        print("===================================")
        print("========== Final project ==========")
        print("===================================")
        print()
        print("Task 1. Adding 'Pass' column ...")
        df2["Pass"] = df2["MinScore"] >= 15
        print("Part of the new table:")
        print(df2)
        print()

        print("Task 2. Adding 'Grade' column ...")
        add_grade_column(df2)
        print(df2)
        print()

        # df2.to_csv("data1.csv", index=False)

        # print("Task 3. Draw a plot:")
        # df2.plot(x = "Sex", y = "Grade")
        # plt.show()

        # print("Task 4. Show all negative minimal scores:")
        # df2, num = show_negative_minimal_scores(df2)
        # print(df2)
        # print(f"Number of negative minimum scores is: {num}")

        # print("Task 5. Usage of numpy:")
        # print("Sorting according to AvgScore:")
