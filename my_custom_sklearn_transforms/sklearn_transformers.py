from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')
    

class RandomUnderSampl(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # separar en las dos clases "aprovado y sospechoso "
        count_class_0, count_class_1 = data.OBJETIVO.value_counts()

        # nivelar los casos a  527  Df
        df_class_0 = data[data['OBJETIVO'] == 'Aceptado']
        df_class_1 = data[data['OBJETIVO'] == 'Sospechoso']

        OBJETIVO_count = data.OBJETIVO.value_counts()


        df_class_0_under = df_class_0.sample(count_class_1)
        df_test_under = pd.concat([df_class_0_under, df_class_1], axis=0)

        print('Random under-sampling:')
        print(df_test_under.OBJETIVO.value_counts())

        return df_test_under
