from builtins import IndexError
import pandas as pd


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
        return self.user_list[key]

    def set_user(self, user, key):
        self.user_list[key] = user


class User():

    def __init__(self, sex, duration, minScore, maxScore, avgScore, passed, grade):
        self.sex = sex
        self.duration = duration
        self.min_score = minScore
        self.max_score = maxScore
        self.avg_score = avgScore
        self.passed = passed
        self.grade = grade

    # def get_user(self):
    #     return self

    # def set_user(self, sex, duration, minScore, maxScore, avgScore, passed, grade):
    #     pass

    def __str__(self):
        return str(f'User: Sex={self.sex}, AvgScore={self.avg_score}, Grade={self.grade}, Passed={self.passed}')
