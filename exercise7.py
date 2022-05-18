import pandas as pd


def read_file(name):
    df = None
    try:
        df = pd.read_csv(name)
        print("Success")
    except IOError:
        print("File not accessible.")

    return df


def write_to_file(df, name):
    try:
        df.to_csv(name, index=False)
        print("Success")
    except IOError:
        print("File not accessible. Check if the file is open")


def examine_csv(df):
    # create statistics
    print(df["Sex"].describe())
    print(df["Duration"].describe())
    print(df["MinScore"].describe())
    print(df["MaxScore"].describe())
    print()
    print(df[["Sex", "Duration"]].groupby("Sex").mean())
    print(df.groupby("Duration").mean())


def clear_data(df):
    print(f"Number of removed data: {remove_row_if_diff(df, 60)}")
    print(f"Number of replaced data: {replace_existing_data(df)}")
    mean, median = replace_not_existing_data(df)
    print("Not existing data are replaced with:", end="")
    print(f" mean: {mean} and median: {median}")

    print("Deleting rows with not existing data ...")
    df.dropna(subset=['Sex'], inplace=True)

    print("Removing duplicates from table ...")
    df.drop_duplicates(inplace=True)


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
