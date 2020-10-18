#----------------------------- ARIQ SENANG ARIQ BAHAGIA HEHEHEHEH ----------------------#
#----------------------------- WELCOME INDIR, SCOTT, BEL--------------------------------#

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

da = pd.read_csv("nhanes_2015_2016.csv")


# Value counts for DMDMARTL
print(da.DMDMARTL.value_counts(),"\n") #\n untuk ngasih space antar data

# Rename the index
da['DMDMARTLx'] = da.DMDMARTL.replace({1:"Married", 2:"Widowed", 3:"Divorce", 4:"Seperated", 5:"Never married", 6:"Living with partner", 77:"Refused"})
da['RIAGENDRx'] = da.RIAGENDR.replace({1: "Men", 2: "Women"})
print(da.DMDMARTLx.value_counts())
print(da.DMDMARTLx.value_counts().sum())

# Insert missing value
da['DMDMARTLx'] = da.DMDMARTLx.fillna('Missing')
print(da.DMDMARTLx.value_counts())

print(da.DMDMARTLx.value_counts().sum())

# Group by men and women for DMDMARTL
dx = da.groupby(["RIAGENDRx"])["DMDMARTLx"].value_counts()
print(dx)


# Seperate between age 30 and 40
da['agegrp'] = pd.cut(da.RIDAGEYR,[30, 40])

# Table for DMDMARTLx for all people for all people between 30 - 40 dx = da.loc[~da.DMDMARTLx.isin(["Refused","Missing"])] dx = dx.groupby("agegrp")["DMDMARTLx"].value_counts() print(dx)

# Table for DMDMARTLx for men and women between 30 - 40
dx = da.loc[~da.DMDMARTLx.isin(["Refused","Missing"])]
dx = dx.groupby(["agegrp","RIAGENDRx"])["DMDMARTLx"].value_counts()
print(dx)

# restricting to the female population
df = da.loc[~da.RIAGENDRx.isin(["Men"])] #eliminates "Men"
df = df.loc[~da.DMDMARTLx.isin(["Refused","Missing"])] #eliminates refused and missing value
df["agegrp*"] = pd.cut(df.RIDAGEYR,[10,20,30,40,50,60,70,80]) #cut ages within 10 years
df = df.groupby(["agegrp*","RIAGENDRx"])["DMDMARTLx"].value_counts()
df = df.unstack()
df = df.apply(lambda x: x/x.sum(), axis=1)
print(df)

# restricting to the male population
dm = da.loc[~da.RIAGENDRx.isin(["Women"])] #eliminates "Women"
dm = dm.loc[~da.DMDMARTLx.isin(["Refused","Missing"])] #eliminates refused and missing value
dm["agegrp*"] = pd.cut(dm.RIDAGEYR,[10,20,30,40,50,60,70,80]) #cut ages within 10 years
dm = dm.groupby(["agegrp*","RIAGENDRx"])["DMDMARTLx"].value_counts()
dm = dm.unstack()
dm = dm.apply(lambda x: x/x.sum(), axis=1)
print(dm)
