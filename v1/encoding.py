import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin

class Categorical_Encoder(TransformerMixin):
    def __init__(self,encoding_='ordinal'):
        self.encoding_ = encoding_

    def fit(self,X,y=None):
        self.cat = X.unique()
        self.indices = {val:i for i,val in enumerate(self.cat)}
        idt = np.identity(len(self.cat))
        self.onehot_ = {self.cat[i]:idt[i] for i in range(len(self.cat))}
        return self
    
    def transform(self,X,y=None):
        pd.set_option('future.no_silent_downcasting', True)

        if self.encoding_ == 'ordinal':
            X_ = X.replace(self.indices.keys(),self.indices.values())

        elif self.encoding_ == 'onehot':
            X_ = X.map(self.onehot_)
        
        return X_