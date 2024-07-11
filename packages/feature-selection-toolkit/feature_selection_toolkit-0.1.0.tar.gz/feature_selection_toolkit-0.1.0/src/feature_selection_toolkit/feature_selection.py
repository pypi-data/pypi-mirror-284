import numpy as np
import pandas as pd
from itertools import combinations
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, accuracy_score, r2_score
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, RandomForestRegressor, GradientBoostingRegressor
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.feature_selection import chi2, f_classif, RFE
from sklearn.linear_model import Lasso, Ridge
from joblib import Parallel, delayed
from matplotlib import pyplot as plt
import statsmodels.api as sm

np.set_printoptions(suppress=True)
pd.set_option('display.float_format', lambda x: '%.4f' % x)

class FeatureSelection:
    
    classifiers = [
        ('GaussianNB', GaussianNB()),
        ('BernoulliNB', BernoulliNB()),
        ('LogisticRegression', LogisticRegression(max_iter=10000)),
        ('RandomForestClassifier', RandomForestClassifier()),
        ('GradientBoostingClassifier', GradientBoostingClassifier()),
        ('KNeighborsClassifier', KNeighborsClassifier(n_neighbors=5)),
        ('DecisionTreeClassifier', DecisionTreeClassifier())
    ]

    regressors = [
        ('LinearRegression', LinearRegression()),
        ('RandomForestRegressor', RandomForestRegressor()),
        ('GradientBoostingRegressor', GradientBoostingRegressor()),
        ('KNeighborsRegressor', KNeighborsRegressor(n_neighbors=5)),
        ('DecisionTreeRegressor', DecisionTreeRegressor())
    ]

    _estimator = None
    _predictions = None

    def __init__(self, X, y, estimator=RandomForestRegressor()):
        """
        FeatureSelection sınıfı, farklı özellik seçimi yöntemlerini kullanarak
        veri setindeki en anlamlı özellikleri seçmeyi sağlar.

        Parameters:
        ------------
        `X` : `array-like`
            Bağımsız değişkenler (features).

        `y` : `array-like`
            Bağımlı değişken (target).

        `estimator` : `estimator object`, default=`RandomForestRegressor`
            Kullanılacak tahmin modeli.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        """

        self.X = X
        self.y = y
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)
        self.set_estimator(estimator)
        
    def set_estimator(self, estimator):
        """
        Tahmin modelini ayarlar.

        Parameters:
        ------------
        `estimator` : `estimator object`
            Kullanılacak tahmin modeli.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> fs.set_estimator(estimator=RandomForestRegressor())
        """
        self._estimator = estimator
        self.set_predictions()

    def set_predictions(self):
        """
        Tahminleri ayarlar.

        Notes:
        ------
        Tahmin modeli eğitilir ve test verisi üzerinde tahminler yapılır.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> fs.set_predictions()
        """
        try:
            self._estimator.fit(self.X_train, self.y_train)
            self._predictions = self._estimator.predict(self.X_test)
        except Exception as e:
            raise ValueError(f"Error setting predictions: {e}")

    def filter_method(self, method='chi2'):
        """
        Filtre yöntemlerini kullanarak özellik seçimi yapar.

        Parameters:
        ------------
        `method` : `str`
            Kullanılacak filtre yöntemi. 'chi2' veya 'anova' olabilir.

        Returns:
        --------
        `scores` : `array`
            Özelliklerin skorları.
        `p_values` : `array`
            Özelliklerin p-değerleri.

        Notes:
        ------
        Filtre yöntemleri, bağımsız olarak her bir özelliğin bağımlı değişkenle olan ilişkisini değerlendirir.
        Kullanım örnekleri arasında ANOVA ve Chi-squared testleri bulunur.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> scores, p_values = fs.filter_method(method='chi2')
        >>> print(scores)
        >>> print(p_values)
        """
        try:
            if method == 'chi2':
                scores, p_values = chi2(self.X, self.y)
            elif method == 'anova':
                scores, p_values = f_classif(self.X, self.y)
            else:
                raise ValueError("Unknown filter method. Please choose 'chi2' or 'anova'.")
        except Exception as e:
            raise ValueError(f"Error in filter_method: {e}")
        return scores, p_values

    def forward_selection(self, significance_level=0.05):
        """
        Forward selection yöntemi ile özellik seçimi yapar.

        Parameters:
        ----------
        `significance_level` : `float`
            Özelliklerin modele dahil edilmesi için gereken anlamlılık seviyesi.

        Returns:
        --------
        `selected_features` : `list`
            Seçilen özelliklerin isimleri.

        Notes:
        -------
        Forward selection, model oluştururken en anlamlı olan özellikleri iteratif olarak ekler.
        Bu yöntem özellikle başlangıçta çok fazla özelliğin olmadığı durumlarda kullanışlıdır.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> from sklearn.linear_model import LinearRegression
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y, LinearRegression())
        >>> selected_features = fs.forward_selection(significance_level=0.05)
        >>> print(selected_features)
        """
        try:
            columns = list(self.X.columns)
            selected_columns = []
            remaining_columns = columns.copy()

            with tqdm(total=len(columns), desc="Forward Selection Progress") as pbar:
                while remaining_columns:
                    min_pval = float('inf')
                    best_column = None

                    for column in remaining_columns:
                        current_columns = selected_columns + [column]
                        predict = self._estimator.fit(self.X_train[current_columns], self.y_train).predict(self.X_test[current_columns])
                        model = sm.OLS(predict, sm.add_constant(self.X_test[current_columns])).fit()
                        pval = model.pvalues.iloc[-1]

                        if pval < min_pval:
                            min_pval = pval
                            best_column = column

                    if min_pval < significance_level:
                        selected_columns.append(best_column)
                        remaining_columns.remove(best_column)
                    else:
                        pbar.update(1)
                        break

                    pbar.update(1)

        except Exception as e:
            raise ValueError(f"Error in forward_selection: {e}")

        return selected_columns

    def backward_elimination(self, significance_level=0.05):
        """
        Backward elimination yöntemi ile özellik seçimi yapar.

        Parameters:
        ------------
        `significance_level` : `float`
            Özelliklerin modelden çıkarılması için gereken anlamlılık seviyesi.

        Returns:
        --------
        `selected_features` : `list`
            Seçilen özelliklerin isimleri.

        Notes:
        -------
        Backward elimination, tüm özelliklerle başlayıp, en az anlamlı olanları iteratif olarak çıkarır.
        Bu yöntem, özellikle başlangıçta çok fazla özelliğin olduğu durumlarda etkilidir.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> selected_features = fs.backward_elimination(significance_level=0.05)
        >>> print(selected_features)
        """
        try:
            features = list(self.X.columns)
            with tqdm(total=len(features), desc="Backward Elimination Progress") as pbar:
                while len(features) > 0:
                    X_opt = self.X_test[features]
                    predictions = self._estimator.fit(self.X_train[features], self.y_train).predict(self.X_test[features])
                    model = sm.OLS(predictions, sm.add_constant(X_opt)).fit()
                    max_p_value = model.pvalues.max()

                    if max_p_value > significance_level:
                        excluded_feature = model.pvalues.idxmax()
                        if excluded_feature in features:
                            features.remove(excluded_feature)
                            pbar.update(1)
                        else:
                            pbar.update(1)
                            break
                    else:
                        pbar.update(1)
                        break
                pbar.update(1)
        except Exception as e:
            raise ValueError(f"Error in backward_elimination: {e}")

        return features

    def recursive_feature_elimination(self, estimator=RandomForestClassifier(), n_features_to_select=1):
        """
        Recursive feature elimination (RFE) yöntemi ile özellik seçimi yapar.

        Parameters:
        ------------
        `estimator` : `estimator object`
            Kullanılacak tahmin modeli.
        `n_features_to_select` : `int`
            Seçilecek özellik sayısı.

        Returns:
        --------
        `support` : `array-like`
            Seçilen özelliklerin destek vektörü.

        Notes:
        Recursive feature elimination, belirli bir tahmin modeli kullanarak iteratif olarak özellikleri çıkarır.
        Bu yöntem, özellikle modelin performansını iyileştirmek için kullanılır.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> support = fs.recursive_feature_elimination(estimator=RandomForestClassifier(), n_features_to_select=2)
        >>> print(support)
        """
        try:
            selector = RFE(estimator, n_features_to_select=n_features_to_select, step=1)
            for _ in tqdm(range(self.X.shape[1]), desc="RFE Progress"):
                self._estimator.fit(self.X_train, self.y_train)
                selector.fit(self.X_test, self.y_test)
            result = pd.DataFrame(data=[list(selector.ranking_), list(self.X_test.columns)], index=['ranking', 'features']).T
        except Exception as e:
            raise ValueError(f"Error in recursive_feature_elimination: {e}")

        return result.set_index('features')['ranking'].sort_index(ascending=False)

    def embedded_method(self, method='lasso', alpha=1.0):
        """
        Gömülü yöntemleri kullanarak özellik seçimi yapar.

        Parameters:
        ------------
        `method` : `str`
            Kullanılacak gömülü yöntem. `'lasso'`, `'ridge'`, `'decision_tree'`, `'random_forest'` olabilir.
        `alpha` : `float`
            Regularizasyon parametresi.

        Returns:
        --------
        `coefficients `: `array`
            Özelliklerin katsayıları veya önem dereceleri.

        Notes:
        -------
        Gömülü yöntemler, modelin eğitim sürecinde özellik seçimini gerçekleştirir.
        Lasso, Ridge gibi yöntemler, özellikle yüksek boyutlu veri setlerinde etkilidir.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> coefficients = fs.embedded_method(method='lasso', alpha=0.01)
        >>> print(coefficients)
        """
        try:
            if method == 'lasso':
                model = Lasso(alpha=alpha)
            elif method == 'ridge':
                model = Ridge(alpha=alpha)
            elif method == 'decision_tree':
                model = DecisionTreeClassifier()
            elif method == 'random_forest':
                model = RandomForestClassifier()
            else:
                raise ValueError("Unknown embedded method. Please choose 'lasso', 'ridge', 'decision_tree', or 'random_forest'.")

            for _ in tqdm(range(self.X.shape[1]), desc="Embedded Method Progress"):
                model.fit(self.X, self.y)

            if hasattr(model, 'coef_'):
                return model.coef_
            else:
                return model.feature_importances_
        except Exception as e:
            raise ValueError(f"Error in embedded_method: {e}")

    def scored_columns(self, problem_type='classification', test_size=0.33, random_state=42, r_start_on=1):
        """
        Brute Force yöntemi ile en optimal kolonları bulur.

        Bu fonksiyon, verilen bağımsız değişken seti üzerinde tüm olası kolon kombinasyonlarını deneyerek
        en iyi performans gösteren kolon kombinasyonlarını ve modeli belirler.

        Parameters
        ----------
        `problem_type` : `str`, {'classification', 'regression'}
            Problemin türü: 'classification' (sınıflandırma) veya 'regression' (regresyon).
        `test_size`: `float`, default=0.33
            Test verisi oranı.
        `random_state` : `int`, default=42
            Rastgelelik için sabit değer.
        `r_start_on` : `int`, default=1
            Kombinasyonların başlaması gereken minimum kolon sayısı.

        Returns
        -------
        `list`
            En iyi performans gösteren kolon kombinasyonları ve modellerin listesi.

        Examples
        --------
        >>> from sklearn.datasets import load_iris
        >>> data = load_iris()
        >>> X = pd.DataFrame(data.data, columns=data.feature_names)
        >>> y = pd.Series(data.target)
        >>> fs = FeatureSelection(X, y)
        >>> best_scores = fs.scored_columns(problem_type='classification')
        >>> print(best_scores)
        """
        try:
            if problem_type not in ['classification', 'regression']:
                raise ValueError("Invalid problem type! Please use 'classification' or 'regression'.")

            if problem_type == 'classification':
                models = self.classifiers
                metric = accuracy_score
            elif problem_type == 'regression':
                models = self.regressors
                metric = r2_score
            
            scores = {}
            invalid_models = []

            print(f'{self.get_possible_combinations_count(columns=self.X.columns, start_from=r_start_on)} column combinations will be processed...')
            
            for r in tqdm(range(r_start_on, len(self.X.columns) + 1), desc="Brute Force Progress"):
                for columns in tqdm(self.get_combinations(self.X.columns, r), total=self.binom(len(self.X.columns), r), desc=f'Processing for column combination (n={len(self.X.columns)}|r={r})'):
                    x_train, x_test, y_train, y_test = train_test_split(self.X[list(columns)], self.y, test_size=test_size, random_state=random_state)

                    for model_name, model in models:
                        try:
                            model.fit(x_train, y_train)
                            y_pred = model.predict(x_test)
                            scores[(model_name, columns)] = (metric.__name__, metric(y_test, y_pred))
                        except Exception as e:
                            invalid_models.append((model_name, columns, str(e)))

            print(f'Invalid models: {list(set(invalid_models))}')
            print('All Done!')
            return self.find_best_score(scores)
        except Exception as e:
            raise ValueError(f"Error in scored_columns: {e}")

    @staticmethod
    def binom(n, r):
        return np.math.factorial(n) / (np.math.factorial(r) * np.math.factorial(n - r))

    @staticmethod
    def get_possible_combinations_count(columns, start_from=1):
        result = 0
        for r in range(start_from, len(columns) + 1):
            result += FeatureSelection.binom(len(columns), r)
        return result

    @staticmethod
    def get_combinations(columns, r):
        return list(combinations(columns, r))

    @staticmethod
    def find_best_score(scores):
        sorted_scores = sorted(scores.items(), key=lambda x: x[1][1], reverse=False)
        return sorted_scores


