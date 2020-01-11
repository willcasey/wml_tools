import pandas as pd
import numpy as np

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



def cv_over_time(df, time_col, cv_cnt=10, train_split=0.66, overlap_p = 0.25, rolling=False):
    """
    create cross validation splits over time.
    option to set it to rolling windows
    option to have overlapping windows

    """
    df = df.sort_values(time_col)
    prev_in = 0
    cv_indices = []
    splits = np.round(np.linspace(0, len(df), cv_cnt))
    if rolling:
        for i in splits[1:]:
            train_in = df.loc[0: np.round(((i -prev_in)*train_split) + prev_in)].index
            test_in = df.loc[np.round(((i -prev_in)*train_split) + prev_in) + 1: i].index
            prev_in = i
            cv_indices.append((train_in, test_in))
    else:
        for i in splits[1:]:
            train_in = df.loc[(prev_in - np.round(prev_in*overlap_p)): np.round(((i -prev_in)*train_split) + prev_in)].index
            test_in = df.loc[np.round(((i -prev_in)*train_split) + prev_in) + 1: i].index
            prev_in = i
            cv_indices.append((train_in, test_in))
    return cv_indices
