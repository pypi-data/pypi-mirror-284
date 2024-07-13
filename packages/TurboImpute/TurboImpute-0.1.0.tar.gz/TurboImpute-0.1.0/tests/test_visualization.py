import unittest
import pandas as pd
from unittest.mock import patch
import logging
from TurboImpute import visualization

class TestVisualizationMethods(unittest.TestCase):

    def setUp(self): 
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [None, 3, 4, None, 6],
            'C': ['a', 'b', None, 'c', 'd']
        })

    @patch('logging.Logger.info')
    def test_visualize_missing(self, mock_info):
        visualization.visualize_missing(self.df)
        mock_info.assert_called()

if __name__ == '__main__':
    unittest.main()