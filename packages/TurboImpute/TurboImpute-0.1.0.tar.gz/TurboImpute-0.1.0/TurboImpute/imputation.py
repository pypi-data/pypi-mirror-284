import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import GradientBoostingRegressor

def impute_mean(df, columns=None):
    if columns is None:
        columns = df.columns
    for column in columns:
        df[column] = df[column].fillna(df[column].mean())
    return df

def impute_median(df, columns=None):
    if columns is None:
        columns = df.columns
    for column in columns:
        df[column] = df[column].fillna(df[column].median())
    return df

def impute_mode(df, columns=None):
    if columns is None:
        columns = df.columns
    for column in columns:
        try:
            mode_value = df[column].mode()[0]
            df[column] = df[column].fillna(mode_value)
        except IndexError:
            # Handle case where mode cannot be computed (e.g., all values are unique)
            pass
    return df

def impute_value(df, value, columns=None):
    if columns is None:
        columns = df.columns
    for column in columns:
        df[column] = df[column].fillna(value)
    return df

def impute_ml(df, method='knn', columns=None, **kwargs):
    if method == 'knn':
        return impute_knn(df, columns, **kwargs)
    elif method == 'decisiontree':
        return impute_dt(df, columns, **kwargs)
    elif method == 'gbm':
        return impute_gbm(df, columns, **kwargs)
    else:
        raise ValueError("Method not supported: choose from 'knn', 'decisiontree', 'gbm'")

def impute_knn(df, columns=None, n_neighbors=5):
    if columns is None:
        columns = df.columns
    imputer = KNNImputer(n_neighbors=n_neighbors)
    df[columns] = imputer.fit_transform(df[columns])
    return df

def impute_dt(df, columns=None, **kwargs):
    if columns is None:
        columns = df.columns
    imputer = IterativeImputer(estimator=DecisionTreeRegressor(), **kwargs)
    df[columns] = imputer.fit_transform(df[columns])
    return df

def impute_gbm(df, columns=None, **kwargs):
    if columns is None:
        columns = df.columns
    imputer = IterativeImputer(estimator=GradientBoostingRegressor(), **kwargs)
    df[columns] = imputer.fit_transform(df[columns])
    return df