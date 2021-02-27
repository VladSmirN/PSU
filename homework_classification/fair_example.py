# такой скрипт нужно отправить ответом!!! В нём не нужно учить модельку.
# моделька поставляется вместе со скриптом, и загружается через pickle
# важно!!!! не подаётся колонка с фильмами!!!
# разрешено numpy, pandas, sklearn (мне влом ставить либы)
import pandas as pd
import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("in_file")
parser.add_argument("out_file")
args = parser.parse_args()

data = pd.read_csv(args.in_file)


def prepaer_df(df):
    columns = ['time', 'sex', 'child_offence', 'vegan', 'dvach', 'gender', 'rest', 'games', 'series', 'books', 'antisemetism', 'subject', 'crimea', 'putin', 'english', 'old_days']
    oldColumns = df.columns
    df = df.rename(columns=dict(zip(oldColumns, columns)) )
    df.time = pd.to_datetime(df.time)
    df.loc[df.sex == 'Мальчик' ,['sex']] = 0
    df.loc[df.sex == 'Девочка' ,['sex']] = 1
    df.loc[df.rest == 'Сычевать' ,['rest']] = 1
    df.loc[df.rest == 'Гулять' ,['rest']] = 0
    df = pd.get_dummies(df, drop_first=True,columns=['child_offence', 'dvach', 'gender', 'antisemetism', 'subject', 'crimea' ])
    df['putin_good'] = 0
    df.loc[(df.putin == 'Политик, лидер и боец') | (df.putin == 'Молодец'),['putin_good']]=1
    df['rebel'] = 1
    df.loc[(df.putin == 'Политик, лидер и боец') | (df.putin == 'Молодец'),['rebel']]=0
    df  =df.drop(columns=['putin'])
    df['month'] = df['time'].dt.month
    df['dayofweek'] = df['time'].dt.dayofweek
    df['day'] = df['time'].dt.day
    df['hour'] = df['time'].dt.hour
    df.loc[df['english'] == 'Оригатоё гайзаймас', ['english']] = 0
    df.loc[df['english'] == 'Чуть лучше, чем ничего', ['english']] = 1
    df.loc[df['english'] == 'Нормально', ['english']] = 2
    df.loc[df['english'] == 'Хорошо', ['english']] = 3
    df.loc[df['english'] == 'Отлично', ['english']] = 4
    df.loc[df['english'] == 'НЭЙТИВ ИНГЛИШ СПИКЕР', ['english']] = 5
    df.loc[df['old_days'] == 'Нет', ['old_days']] = 0
    df.loc[df['old_days'] != 'Нет', ['old_days']] = 1
    return df

data= prepaer_df(data)
feature = data.drop(columns=['time'])
input = open('model.pkl', 'rb')
clf = pickle.load(input)
input.close()

predictions = clf.predict(feature)
predictions_df = pd.DataFrame(data=predictions,  columns=["res" ])

# тут зачехлить свою магию обратно
predictions_df.to_csv(args.out_file)





