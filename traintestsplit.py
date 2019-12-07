import pandas as pd

def train_test_split_time(df, time_col, label_col, train_percent = 0.66):
    '''
    train test split based on a date or time column
    '''
    split_index = min(df.index) + round(len(df)*train_percent)
    print(df[time_col].min())
    print(df.loc[:split_index][time_col].max())
    
    print(df.loc[split_index:][time_col].min())
    print(df.loc[split_index:][time_col].max())
    df['index_col'] = df.index
    df = df.sort_values([time_col, 'index_col'])
    df = df.drop(columns=['index_col'])
    train_df, test_df = df.loc[:split_index], df.loc[split_index:]
    X_train, y_train = train_df.drop(columns=[label_col, time_col]), train_df[label_col]
    X_test, y_test = test_df.drop(columns=[label_col, time_col]), test_df[label_col]
    return X_train, y_train, X_test, y_test
