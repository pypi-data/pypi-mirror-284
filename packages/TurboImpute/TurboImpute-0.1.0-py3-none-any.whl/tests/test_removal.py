import unittest
import pandas as pd
from TurboImpute import removal

class TestRemovalMethods(unittest.TestCase):

    def setUp(self): 
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [None, 3, 4, None, 6],
            'C': ['a', 'b', 'c', 'd', 'e']
        })

    def test_drop_missing_rows(self):
        df_dropped = removal.drop_missing_rows(self.df)
        self.assertEqual(len(df_dropped), 2) 

    def test_drop_missing_columns(self):
        df_dropped = removal.drop_missing_columns(self.df)
        self.assertEqual(len(df_dropped.columns), 1)

if __name__ == '__main__':
    unittest.main()