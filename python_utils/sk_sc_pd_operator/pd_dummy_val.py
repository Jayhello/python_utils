# coding:utf-8


import pandas as pd


def pd_dummy_val_1():
    raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
                'sex': ['male', 'female', 'male', 'female', 'female']}

    df = pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'sex'])
    print df

    #    first_name last_name     sex
    # 0      Jason    Miller    male
    # 1      Molly  Jacobson  female
    # 2       Tina       Ali    male
    # 3       Jake    Milner  female
    # 4        Amy     Cooze  female

    # Create a set of dummy variables from the sex variable
    df_sex = pd.get_dummies(df['sex'])
    # Join the dummy variables to the main dataframe
    df_new = pd.concat([df, df_sex], axis=1)
    print df_new
    #   first_name last_name     sex  female  male
    # 0      Jason    Miller    male     0.0   1.0
    # 1      Molly  Jacobson  female     1.0   0.0
    # 2       Tina       Ali    male     0.0   1.0
    # 3       Jake    Milner  female     1.0   0.0
    # 4        Amy     Cooze  female     1.0   0.0

def pd_dummy_val_2():
    raw_data = {"work_hour": [9, 9, 9, 9, 9, 9, 6],
                "day": ["mon", "tus", "wend", "thur", "fri", "sta", "sun"]}

    df = pd.DataFrame(raw_data, columns=['work_hour', 'day'])

    print df
    #     work_hour   day
    # 0          9   mon
    # 1          9   tus
    # 2          9  wend
    # 3          9  thur
    # 4          9   fri
    # 5          9   sta
    # 6          6   sun

    df_day = pd.get_dummies(df['day'])

    df_new = pd.concat([df, df_day], axis=1)

    print df_new
    #     work_hour   day  fri  mon  sta  sun  thur  tus  wend
    # 0          9   mon  0.0  1.0  0.0  0.0   0.0  0.0   0.0
    # 1          9   tus  0.0  0.0  0.0  0.0   0.0  1.0   0.0
    # 2          9  wend  0.0  0.0  0.0  0.0   0.0  0.0   1.0
    # 3          9  thur  0.0  0.0  0.0  0.0   1.0  0.0   0.0
    # 4          9   fri  1.0  0.0  0.0  0.0   0.0  0.0   0.0
    # 5          9   sta  0.0  0.0  1.0  0.0   0.0  0.0   0.0
    # 6          6   sun  0.0  0.0  0.0  1.0   0.0  0.0   0.0

if __name__ == '__main__':
    pd_dummy_val_1()
    # pd_dummy_val_2()
    pass
