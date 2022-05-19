import pandas as pd


def read_file(name):
    """
    Read csv file. If success return data frame,
    otherwise return None.
    """
    df = None
    try:
        df = pd.read_csv(name)
        print("Success")
    except IOError:
        print("File not accessible.")

    return df


def write_to_file(df, name):
    """
    Write csv file.
    """
    try:
        df.to_csv(name, index=False)
        print("Success")
    except IOError:
        print("File not accessible. Check if the file is open")


def examine_csv(df):
    """
    Print table description.
    """
    print(df["Sex"].describe())
    print(df["Duration"].describe())
    print(df["MinScore"].describe())
    print(df["MaxScore"].describe())


def clear_data(df):
    """
    Clearing 'bad' data.
    """
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
    """
    Remove row if data is different than 'value'.
    """
    removed_items = 0
    for x in df.index:
        if df.loc[x, "Duration"] != value:
            df.drop(x, inplace=True)
            removed_items += 1

    return removed_items


def replace_existing_data(df):
    """
    If data is out of scope (< 0 or > 100)
    replace with 0 or max() respectively.
    """
    updated_items = 0
    # max_replace_with = df["MaxScore"][df["MaxScore"] <= 100].max()
    max_replace_with = df["MaxScore"].max()
    for x in df.index:
        if df.loc[x, "MinScore"] < 0:
            df.loc[x, "MinScore"] = 0
            updated_items += 1
        if df.loc[x, "MaxScore"] > 100:
            df.loc[x, "MaxScore"] = max_replace_with
            updated_items += 1

    return updated_items


def replace_not_existing_data(df):
    """
    If data not exist insert .mean() and .median().
    """
    mean = int(df["MinScore"].mean())
    df["MinScore"].fillna(mean, inplace=True)

    median = int(df["MaxScore"].median())
    df["MaxScore"].fillna(median, inplace=True)

    return mean, median
