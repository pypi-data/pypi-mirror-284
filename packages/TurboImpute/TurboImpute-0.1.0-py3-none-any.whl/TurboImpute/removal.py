import pandas as pd

def drop_missing_rows(dataframe):
    filtered_df = dataframe.dropna(axis=0)
    return filtered_df

def drop_missing_columns(dataframe):
    filtered_df = dataframe.dropna(axis=1)
    return filtered_df
