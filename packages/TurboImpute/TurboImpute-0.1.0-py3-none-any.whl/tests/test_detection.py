import unittest
import pandas as pd
from TurboImpute import detection

class TestDetectionMethods(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [None, 3, 4, None, 6],
            'C': ['a', 'b', None, 'c', 'd']
        })

    def test_identify_missing(self):
        result = detection.identify_missing(self.df)
        self.assertTrue(result['A'].any())
        self.assertTrue(result['B'].any())

    def test_missing_summary(self):
        summary = detection.missing_summary(self.df)
        self.assertEqual(summary.loc['A', 'Total'], 1)
        self.assertAlmostEqual(summary.loc['B', 'Percent'], 40.0)

if __name__ == '__main__':
    unittest.main()