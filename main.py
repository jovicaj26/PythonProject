import unittest
from module_collections import average_grades_score
from module_collections import count_grades
from exercise7 import examine_csv
from exercise7 import clear_data
from exercise7 import read_file
from exercise7 import write_to_file
from module_tests import TestUserTable
from user import User
from user import UserTable

from module_pandas import add_grade_column
from module_pandas import grade_gender_dependency
from module_pandas import show_negative_minimal_scores
from module_pandas import add_pass_column
from module_numpy import sort_grades

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

        print("Task 7 - Plotting ...")
        df2.plot(x="Sex", y="AvgScore")
        plt.show()
        print("\n")

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

        print("Task 3. Drawing plot...")
        grade_gender_dependency(df2)
        plt.show()
        print("\n")

        print("Task 4. Show all negative minimal scores:")
        show_negative_minimal_scores(df2)
        print("\n")

        print("Task 5. Represent all grades as a sorted numpy array:")
        sort_grades(df2)
        print("\n")

        print("Task 6. Usage of Counter from collection:")
        print("Count the number of each grade.")
        count_grades(df3)
        print("Calculating the average maximum and minimum for each grade")
        average_grades_score(df3)

        print("\n")
        print("Task 7. Classes:")
        users = UserTable("data2.csv")
        print("First user before setting a new one: ", users.user_list[0])
        user1 = User("Male", 300, 17, 29, 23, True, "A")
        users.set_user(user1, 0)
        print("First user after setting a new one: ", users.user_list[0])
        print()

        # add user without avg, pass and grade params
        print("Second user before setting a new one: ", users.user_list[1])
        user2 = User("Female", 70, 15, 75)
        users.set_user(user2, 1)
        print("Second user after setting a new one: ", users.user_list[1])

        print(f"Total number of students: {len(users)}")
        print("\n")

        print("Task 8. Tets")
        testsuite = unittest.TestLoader().loadTestsFromTestCase(TestUserTable)
        for test in testsuite._tests:
            unittest.TextTestRunner(verbosity=2).run(test)
