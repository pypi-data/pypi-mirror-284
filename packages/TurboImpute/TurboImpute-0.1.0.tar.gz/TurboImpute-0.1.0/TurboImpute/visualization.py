import matplotlib.pyplot as plt
import logging

def visualize_missing(df):
    for column in df.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(8, 6))
        df[column].plot(kind='box')
        plt.title(f'Boxplot for {column}')
        plt.xlabel(column)
        plt.ylabel('Value')
        plt.show()
        logging.info(f'Boxplot for {column} generated.')

if __name__ == '__main__':
    # Example usage
    import pandas as pd
    df = pd.DataFrame({
        'A': [1, 2, None, 4, 5],
        'B': [None, 3, 4, None, 6],
        'C': ['a', 'b', None, 'c', 'd']
    })
    visualize_missing(df)
