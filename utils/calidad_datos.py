
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
import time
import seaborn as sns
import os

#calidad de datos
def calidad_datos(data):
    tipos = pd.DataFrame({'tipo': data.dtypes},index=data.columns)
    na = pd.DataFrame({'nulos': data.isna().sum()}, index=data.columns)
    na_prop = pd.DataFrame({'porc_nulos':data.isna().sum()/data.shape[0]}, index=data.columns)
    ceros = pd.DataFrame({'ceros':[data.loc[data[col]==0,col].shape[0] for col in data.columns]}, index= data.columns)
    ceros_prop = pd.DataFrame({'porc_ceros':[data.loc[data[col]==0,col].shape[0]/data.shape[0] for col in data.columns]}, index= data.columns)
    summary = data.describe(include='all').T

    summary['dist_IQR'] = summary['75%'] - summary['25%']
    summary['limit_inf'] = summary['25%'] - summary['dist_IQR']*1.5
    summary['limit_sup'] = summary['75%'] + summary['dist_IQR']*1.5

    summary['outliers'] = data.apply(lambda x: sum(np.where((x<summary['limit_inf'][x.name]) | (x>summary['limit_sup'][x.name]),1 ,0)) if x.name in summary['limit_inf'].dropna().index else 0)


    return pd.concat([tipos, na, na_prop, ceros, ceros_prop, summary], axis=1).sort_values('tipo')