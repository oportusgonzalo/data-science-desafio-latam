#%matplotlib inline
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import warnings

from calidad_datos import calidad_datos
from graficos import cross_plot

plt.style.use('seaborn') # gráficos estilo seaborn
plt.rcParams["figure.figsize"] = (8, 6) # Tamaño gráficos
plt.rcParams["figure.dpi"] = 70 # resolución gráficos
warnings.filterwarnings('ignore')