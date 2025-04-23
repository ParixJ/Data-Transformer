from sklearn.base import TransformerMixin
import numpy as np

class StandardScaler(TransformerMixin):

    def __init__(self):
        pass

    def fit(self,X,y=None):
        self.dt_num_ = X.select_dtypes(include=[np.number])
        self.shape_in_ = self.dt_num_.shape
        self.cname = self.dt_num_.columns
        self.mean = self.dt_num_.mean()
        self.median = self.dt_num_.median()
        self.std = self.dt_num_.std()
        return self
    
    def transform(self,X,y=None):
        self.dt_num_ = X.select_dtypes(include=[np.number])
        
        try :
            assert self.shape_in_ == self.dt_num_.shape

        except AssertionError:
            print(f'Shapes {self.shape_in_} and {self.dt_num_.shape} doesnt match')

        a = np.subtract(self.dt_num_ ,self.mean)
        return np.divide(a,self.std)
    
class MinMaxScaler(TransformerMixin):

    def __init__(self):
        pass

    def fit(self,X,y=None):
        self.dt_num_ = X.select_dtypes(include=[np.number])
        self.shape_in_ = self.dt_num_.shape
        self.cname = self.dt_num_.columns
        self.min_ = self.dt_num_.min()
        self.max_ = self.dt_num_.max()
        return self
    
    def transform(self,X,y=None):
        self.dt_num_ = X.select_dtypes(include=[np.number])
        
        try :
            assert self.shape_in_ == self.dt_num_.shape

        except AssertionError:
            print(f'Shapes {self.shape_in_} and {self.dt_num_.shape} doesnt match')

        num_ = np.subtract(self.dt_num_ , self.min_)
        den_ = np.subtract(self.max_,self.min_)
        return np.divide(num_,den_)