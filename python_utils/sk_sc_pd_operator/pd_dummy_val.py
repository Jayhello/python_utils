# coding:utf-8


import pandas as pd


def pd_dummy_val_1():
    raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
                'sex': ['male', 'female', 'male', 'female', 'female']}

    df = pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'sex'])
    print df

    # Create a set of dummy variables from the sex variable
    df_sex = pd.get_dummies(df['sex'])
    # Join the dummy variables to the main dataframe
    df_new = pd.concat([df, df_sex], axis=1)
    print df_new


def pd_dummy_val_2():
    raw_data = {"work_hour": [9, 9, 9, 9, 9, 9, 6],
                "day": ["mon", "tus", "wend", "thur", "fri", "sta", "sun"]}

    df = pd.DataFrame(raw_data, columns=['work_hour', 'day'])

    print df

    df_day = pd.get_dummies(df['day'])

    df_new = pd.concat([df, df_day], axis=1)

    print df_new

if __name__ == '__main__':
    # pd_dummy_val_1()
    pd_dummy_val_2()
    pass
