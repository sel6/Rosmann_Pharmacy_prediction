import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.insert(1, '../scripts')
from cleaning import DataCleaner as dc


class Tester(unittest.TestCase):
    def __init__(self):
      pass

    def test_remove_cols(self):
        df = pd.DataFrame({'col1': [1, 2, 1], 'col2': [3, 4, 3]})
        df = dc.remove_cols(df)
        self.assertEqual(df.shape, (2, 1))
