from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X["VEHICLE_AGE"] = 2026 - X["VEHICLE_YEAR"]
        return X

    def get_feature_names_out(self, input_features=None):
        return list(input_features) + ["VEHICLE_AGE"]