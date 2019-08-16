import pandas as pd
from sklearn import preprocessing

def standardize(dataframe):
    names = dataframe.columns
    scaler = preprocessing.StandardScaler()
    scaled_df = scaler.fit_transform(dataframe)
    return pd.DataFrame(scaled_df, columns=names)

def MaxMinScaler(dataframe):
    names = dataframe.columns
    scaler = preprocessing.MinMaxScaler()
    scaled_df = scaler.fit_transform(dataframe)
    return pd.DataFrame(scaled_df, columns=names)

def Normalizer(dataframe):
    names = dataframe.columns
    scaler = preprocessing.Normalizer()
    scaled_df = scaler.fit_transform(dataframe)
    return pd.DataFrame(scaled_df, columns=names)