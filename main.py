from module_collections import average_grades_score
from module_collections import count_grades
from exercise7 import examine_csv
from exercise7 import clear_data
from exercise7 import read_file
from exercise7 import write_to_file
# from user import User
# from user import UserTable

from module_pandas import add_grade_column
from module_pandas import grade_gender_dependency
from module_pandas import show_negative_minimal_scores
from module_pandas import add_pass_column

import matplotlib.pyplot as plt


if __name__ == '__main__':

    print("Task 1 - Importing csv file:")
    df = read_file("dirtydata.csv")

    if df is not None:
        print(df)
        # examine_csv(df)
        print("\n")

        print("Task 2 - Cleaning 'bad' data:")
        clear_data(df)
        print("\n")

        print("Task 3 - Saving data to data.csv:")
        write_to_file(df, "data.csv")
        print("\n")

    df2 = read_file("data.csv")

    if df2 is not None:
        print("Task 4 - Added AvgScore column")
        df2["AvgScore"] = (df2["MinScore"] + df2["MaxScore"]) / 2
        print("Part of the new table:")
        print(df2)
        print("\n")

        print("Task 5 - Number of Females and Males:")
        print(df2["Sex"].value_counts())
        print("\n")

        print("Task 6 - Average Min and Max scores:")
        print(df2[["Sex", "MinScore"]].groupby("Sex").mean())
        print()
        print(df2[["Sex", "MaxScore"]].groupby("Sex").mean())
        print("\n")

        # print("Task 7 - Plotting ...")
        # df2.plot(x="Sex", y="AvgScore")
        # plt.show()
        # print("\n")

    # END OF M7 EXERCISE
    #  START OF PROJECT

    print("===================================")
    print("========== Final project ==========")
    print("===================================")
    print()

    if df2 is not None:
        print("Task 1. Adding 'Pass' column ...")
        add_pass_column(df2)
        print("Part of the new table:")
        print(df2)
        print("\n")

        print("Task 2. Adding 'Grade' column ...")
        add_grade_column(df2)
        print("Part of the new table:")
        print(df2)
        print("\n")

        print("Saving new data to data2.csv:")
        write_to_file(df2, "data2.csv")
        print("\n")
        df3 = df2
        # print("Task 3. Drawing plot...")
        # grade_gender_dependency(df2)
        # plt.show()
        # print("\n")

        print("Task 4. Show all negative minimal scores:")
        df2, num = show_negative_minimal_scores(df2)
        print(df2)
        print(f"Number of negative grades is: {num}")
        print("\n")

        # print("Task 5. Usage of numpy:")
        # print("Sorting according to AvgScore:")

        print("Task 6. Usage of Counter from collection:")
        print("Count the number of each grade.")

        count_grades(df3)
        average_grades_score(df3)

        # users = UserTable("dirtydata.csv", [])
        # print(users.items)
        # print(f"Total number of students: {len(users)}")
        # print(User({"Sex": "Male", "AvgScore": "89", "Grade": "B"}))
