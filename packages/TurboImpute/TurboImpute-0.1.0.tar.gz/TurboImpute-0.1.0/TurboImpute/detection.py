import pandas as pd

def identify_missing(df):
    return df.isnull()

def missing_summary(df):
    total_missing = df.isnull().sum()
    percent_missing = (total_missing / len(df)) * 100
    summary = pd.DataFrame({
        'Total': total_missing,
        'Percent': percent_missing
    })
    return summary