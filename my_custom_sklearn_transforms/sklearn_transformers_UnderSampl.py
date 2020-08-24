
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

        # nivelar los casos a  527  Df
        df_class_0 = data[data.iloc[:,-1] == 'Aceptado']
        df_class_1 = data[data.iloc[:,-1] == 'Sospechoso']

        OBJETIVO_count = data.iloc[:,-1].value_counts()


        df_class_0_under = df_class_0.sample(count_class_1)
        df_test_under = pd.concat([df_class_0_under, df_class_1], axis=0)

        print('Random under-sampling:')
        print(df_test_under.iloc[:,-1].value_counts())

        return df_test_under
