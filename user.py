from operator import index
from unicodedata import numeric
import pandas as pd


class UserTable:
    def __init__(self, data_table):
        self.data_table = data_table

    def __len__(self):
        return len(self.data_table.index.value_counts())

    def __getitem__(self, key):
        return self.data_table[key]


class User:
    def __init__(self, data_table):
        self.sex = data_table["Sex"]
        self.duration = data_table["Duration"]
        self.min_score = data_table["MinScore"]
        self.max_score = data_table["MaxScore"]
        # self.passed = data_table["Pass"]
        # self.grade = data_table["Grade"]
        # self.avg_score = data_table["AvgScore"]

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def get_min_score(self):
        return self.min_score

    def set_min_score(self, min_score):
        self.min_score = min_score

    def get_max_score(self):
        return self.max_score

    def set_max_score(self, max_score):
        self.max_score = max_score

    # def get_passed(self):
    #     return self.passed

    # def set_passed(self, passed):
    #     self.passed = passed

    # def get_grade(self):
    #     return self.grade

    # def set_grade(self, grade):
    #     self.grade = grade

    # def get_avg_score(self):
    #     return self.avg_score

    # def set_avg_score(self, avg_score):
    #     self.avg_score = avg_score

    def __str__(self):
        return str(f'User: Sex={self.sex}, AvgScore={self.avg_score}, Grade={self.grade}, Passed={self.passed}')


if __name__ == "__main__":
    dt = pd.read_csv('dirtydata.csv')
    # print(dt)
    users = UserTable(dt)
    # print(f"Total number of students: {len(users)}")
    # print(User({"Sex": "Male", "AvgScore": "89", "Grade": "B"}))
