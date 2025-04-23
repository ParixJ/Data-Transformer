import numpy as np
import pandas as pd

def bin_data(X,bins_,labels_):

    return pd.cut(X,bins=bins_,labels=labels_)

def bucketize_data(X,n_bins_,labels_):

    return pd.qcut(X,q=n_bins_,labels=labels_)

def data_log_transform(X):

    return np.log1p(X)

def data_sqrt_transform(X):

    return np.sqrt(X)