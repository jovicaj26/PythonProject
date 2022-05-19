from operator import index
from turtle import setx
from unicodedata import numeric
import pandas as pd


class UserTable():
    def __init__(self, filename):
        self.data_table = pd.read_csv(filename)
        self.load_from_table(self.data_table)

    def __len__(self):
        return len(self.data_table.index.value_counts())

    def __getitem__(self, key):
        return self.data_table[key]  # TODO - key is dt index

    def load_from_table(self, data_table):
        user_list = list()
        for i in data_table.index:
            user = User(data_table.loc[i])
            user_list.append(user)
            print(user)


class User():
    def __init__(self, sex, duration, minScore, maxScore, avgScore, passed, grade):
        self.sex = sex
        self.duration = duration
        self.min_score = minScore
        self.max_score = maxScore
        self.avg_score = avgScore
        self.passed = passed
        self.grade = grade

# get/set for row
    def get_user(self):
        pass
        # return self.sex

    def set_user(self, x):
        pass

    def __str__(self):
        return str(f'User: Sex={self.sex}, AvgScore={self.avg_score}, Grade={self.grade}, Passed={self.passed}')
