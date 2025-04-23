from sklearn.base import BaseEstimator,TransformerMixin
import numpy as np

class Imputer(BaseEstimator,TransformerMixin):

    def __init__(self,strategy='median'):
        self.strategy = strategy
        self.strategy_type = ['mean','median']

    def fit(self,X,y=None):
        self.dt_num_ = X.select_dtypes(include=[np.number])
        self.num_features_ = self.dt_num_.shape[1]
        self.mean = self.dt_num_.mean(axis=0)
        self.median = self.dt_num_.median(axis=0)
        return self
    
    def transform(self, X, y = None):
        self.dt_num_ = X.select_dtypes(include=[np.number])
        
        try :
            assert self.num_features_ == self.dt_num_.shape[1]
        except AssertionError:
            print('No. of feature doesnt match.')

        for c in self.dt_num_.columns:
            if self.strategy == 'mean':
                self.dt_num_[c] = self.dt_num_[c].fillna(self.mean[c])
            else :
                self.dt_num_[c] = self.dt_num_[c].fillna(self.median[c])
        return self.dt_num_