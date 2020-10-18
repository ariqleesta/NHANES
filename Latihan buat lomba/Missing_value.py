import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
pd.set_option('display.max_columns', 100)


da = pd.read_csv('nhanes_2015_2016.csv')

print(da.head())
print(da.DMDMARTL.value_counts())
da['DMDMARTLx'] = da.DMDMARTL.replace({1:'Maried', 2:"Widowed", 3:"Divorced", 4:"Separated",  5:"Never married", 6:"Living with partner", 77:"Refused", 99: "Don't know"})
da['DMDMARTLx'] = da.DMDMARTLx.fillna('Missing')

print(da.RIAGENDR.value_counts())
da['RIAGENDRx'] = da.RIAGENDR.replace({1: 'Male', 2: 'Female'})
da['RIAGENDRx'] = da.RIAGENDRx.fillna('Missing')

dx = da.groupby(["RIAGENDRx"])["DMDMARTLx"].value_counts()
print(dx)

sns.boxplot(dx)
plt.title('Marital Status by Gender')
plt.show()
