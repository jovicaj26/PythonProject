import unittest
import sys
import pandas as pd
from user import User, UserTable


class TestUserTable(unittest.TestCase):

    def setUp(self):
        self.userTable = UserTable("data2.csv")
        self.user1 = User("Female", 300, 17, 29, 23, True, "F")
        self.user2 = User("Female", 70, 15, 75)

    def tearDown(self):
        self.userTable = None
        self.user1 = None
        self.user2 = None

    def test_set_get_len_user(self):

        print("First user before setting a new one:", self.userTable.get_user(0))

        len_before = len(self.userTable)
        print("User table length before any changes:", len_before)

        self.userTable.set_user(self.user1, 0)
        user1 = self.userTable.get_user(0)
        print("First user after setting a new one: ", user1)

        self.assertIs(self.user1, user1)

        len_after = len(self.userTable)
        print("User table length after assigning new values to the first student:", len_after)

        self.assertEqual(len_before, len_after)

    def test_load_from_table(self):
        df = pd.DataFrame(
            {
                "Sex": [
                    "Female",
                    "Male",
                    "Male",
                    "Male",
                    "Male",
                    "Male"
                ],
                "Duration": [1, 2, 3, 4, 5, 6],
                "MinScore": [25, 25, 25, 25, 25, 25],
                "MaxScore": [100, 100, 100, 100, 100, 100],
                "AvgScore": [50, 50, 50, 50, 50, 50],
                "Passed": [True, True, True, True, True, True],
                "Grade": ["A", "A", "A", "A", "A", "A"]
            }
        )

        self.userTable.load_from_table(df)
        self.assertEqual(len(df), 6)
        print("First user before setting a new one: ", self.userTable[0])
        self.userTable.set_user(self.user1, 0)
        user1 = self.userTable[0]
        print("First user after setting a new one: ", user1)

        self.assertIs(self.user1, user1)

    def test_index_operator(self):

        print("Second user before setting a new one:", self.userTable[1])
        self.userTable.set_user(self.user2, 1)

        user2 = self.userTable[1]
        print("Second user after setting a new one: ", self.userTable[1])

        self.assertIs(self.user2, user2)

    def test_invalid_index_operator(self):

        try:
            self.userTable[sys.maxsize]
        except IndexError:
            print("Invalid index operator. Key is greater than the length of user table.")

    def test_invalid_get_item(self):

        print("Invalid user get. Key is greater than the length of user table.")
        self.assertIsNone(self.userTable.get_user(sys.maxsize))

    def test_invalid_set_item(self):

        print("Invalid user set. Key is greater than the length of user table.")
        self.assertIsNone(self.userTable.set_user(self.user1, sys.maxsize))
