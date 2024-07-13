import pandas as pd
import pytest
import warnings
from TurboImpute.imputation import impute_mean, impute_median, impute_mode, impute_value, impute_knn, impute_dt, impute_gbm

@pytest.fixture
def setup_data():
    data = {
        'A': [1, 2, None, 4, 5],
        'B': [5, None, 7, 8, 9],
        'C': [None, 12, 13, 14, 15]
    }
    return pd.DataFrame(data)

class TestImputationMethods:

    def test_impute_mean(self, setup_data):
        df = impute_mean(setup_data.copy())
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0

    def test_impute_median(self, setup_data):
        df = impute_median(setup_data.copy())
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0

    def test_impute_mode(self, setup_data):
        df = impute_mode(setup_data.copy())
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0

    def test_impute_value(self, setup_data):
        df = impute_value(setup_data.copy(), value=0)
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0

    def test_impute_knn(self, setup_data):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            df = impute_knn(setup_data.copy())
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0

    def test_impute_dt(self, setup_data):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            warnings.filterwarnings("ignore", category=UserWarning)
            df = impute_dt(setup_data.copy())
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0

    def test_impute_gbm(self, setup_data):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            warnings.filterwarnings("ignore", category=UserWarning)
            df = impute_gbm(setup_data.copy())
        assert df['A'].isnull().sum() == 0
        assert df['B'].isnull().sum() == 0
        assert df['C'].isnull().sum() == 0