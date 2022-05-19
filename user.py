from builtins import IndexError
import pandas as pd
from module_pandas import get_grade


class UserTable():
    user_list = []

    def __init__(self, filename):
        self.dt = pd.read_csv(filename)
        self.load_from_table(self.dt)

    def __len__(self):
        return len(self.dt.index.value_counts())

    def __getitem__(self, key):
        self.key = self.user_list.index
        if self.key < 0 or self.key > len(self.user_list):
            raise IndexError

        return key

    def load_from_table(self, dt):
        for i in dt.index:
            sex, duration, minScore, maxScore, avgScore, passed, grade = dt.loc[i]
            user = User(sex, duration, minScore,
                        maxScore, avgScore, passed, grade)
            self.user_list.append(user)

    def get_user(self, key):
        if key < len(self.user_list) - 1:
            return self.user_list[key]
        else:
            return None

    def set_user(self, user, key):
        if key < len(self.user_list) - 1:
            self.user_list[key] = user
        else:
            return None

class User():

    def __init__(self, sex, duration, minScore, maxScore, avgScore=None, passed=None, grade=None):
        self.sex = sex
        self.duration = duration
        self.min_score = minScore if minScore > 0 else 0
        self.max_score = maxScore if maxScore <= 100 else 100
        if avgScore is not None and passed is not None and grade is not None:
            self.avg_score = avgScore
            self.passed = passed
            self.grade = grade
        else:
            self.avg_score = (self.min_score + self.max_score) / 2
            self.passed = False if self.min_score < 15 else True
            self.grade = get_grade(self.avg_score, self.passed)

    # def get_user(self):
    #     return self

    # def set_user(self, sex, duration, minScore, maxScore, avgScore, passed, grade):
    #     pass

    def __str__(self):
        return str(f'User: Sex={self.sex}, AvgScore={self.avg_score}, Grade={self.grade}, Passed={self.passed}')
