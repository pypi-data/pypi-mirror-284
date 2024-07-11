import unittest
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression, LinearRegression
from feature_selection_toolkit.feature_selection import FeatureSelection

class TestFeatureSelection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = load_iris()
        cls.X = pd.DataFrame(data.data, columns=data.feature_names)
        cls.y = pd.Series(data.target)
        cls.classification_estimator = LogisticRegression(max_iter=10000)
        cls.regression_estimator = LinearRegression()
        cls.fs_classification = FeatureSelection(cls.X, cls.y, estimator=cls.classification_estimator)
        cls.fs_regression = FeatureSelection(cls.X, cls.y, estimator=cls.regression_estimator)

    def test_filter_method_chi2(self):
        scores, p_values = self.fs_classification.filter_method(method='chi2')
        self.assertEqual(len(scores), self.X.shape[1])
        self.assertEqual(len(p_values), self.X.shape[1])

    def test_forward_selection(self):
        selected_features = self.fs_classification.forward_selection(significance_level=0.05)
        self.assertTrue(len(selected_features) > 0)

    def test_backward_elimination(self):
        selected_features = self.fs_classification.backward_elimination(significance_level=0.05)
        self.assertTrue(len(selected_features) > 0)

    def test_recursive_feature_elimination(self):
        support = self.fs_classification.recursive_feature_elimination(estimator=self.classification_estimator, n_features_to_select=2)
        self.assertTrue(support.sum() > 0)

    def test_embedded_method_lasso(self):
        coefficients = self.fs_regression.embedded_method(method='lasso', alpha=0.01)
        self.assertEqual(len(coefficients), self.X.shape[1])

    def test_scored_columns(self):
        best_scores = self.fs_classification.scored_columns(problem_type='classification')
        self.assertTrue(len(best_scores) > 0)

if __name__ == '__main__':
    unittest.main()

