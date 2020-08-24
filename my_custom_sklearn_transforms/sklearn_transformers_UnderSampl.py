
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class RandomUnderSampl(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        print(data.columns)
        

        return data
