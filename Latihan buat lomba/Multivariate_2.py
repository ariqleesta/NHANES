import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
pd.set_option('display.max_columns',100)

da = pd.read_csv("nhanes_2015_2016.csv")
print(da.columns)

# Below we make a scatterplot of arm length against leg length. 
# This means that arm length (BMXARML) is plotted on the vertical axis 
# and leg length (BMXLEG) is plotted on the horizontal axis.

keep= ['BMXARML','BMXLEG']
print(da[keep].head())

sns.regplot(x='BMXLEG', y='BMXARML', data=da, fit_reg=False, scatter_kws={"alpha":0.2})
#scatter_kws={"alpha":0.2} dictionary "alpha" means, 0.2 means transparency
plt.show()

#Another way to avoid overplotting is to make a plot of the "density" of points.
#In the plots below, darker colors indicate where a greater number of points fall

sns.jointplot(x='BMXLEG', y='BMXARML', data=da, kind = "kde").annotate(stats.pearsonr)

#Next we look at two repeated measures of systolic blood pressure, 
#taken a few minutes apart on the same person. 
#These values are very highly correlated, with a correlation coefficient of around 0.96.
jp = sns.jointplot(x="BPXSY1", y="BPXSY2", kind='kde', data=da).annotate(stats.pearsonr)

#Below, we continue to probe the relationship between leg length and arm length, 
#stratifying first by gender, then by gender and ethnicity.
da["RIAGENDRx"]=da.RIAGENDR.replace({1:"Male",2:"Female"})
sns.FacetGrid(da, col='RIAGENDRx').map(plt.scatter, "BMXLEG","BMXARML", alpha=0.4).add_legend()

#correlation between leg length and arm length for male and female
condition1 = da.RIAGENDRx == "Female"
loc1 = da.loc[condition1, ['BMXLEG','BMXARML']].dropna() #remove missing value
corr1 = loc1.corr()
print(corr1)

condition2 = da.RIAGENDRx == "Male"
loc2 = da.loc[condition2, ['BMXLEG','BMXARML']].dropna()
corr2 = loc2.corr()
print(corr2)

# both gender and ethnicity. 
# This results in 2 x 5 = 10 total strata, 
#since there are 2 gender strata and 5 ethnicity strata.

plot2x5 = sns.FacetGrid(da, col='RIDRETH1',row='RIAGENDRx').map(plt.scatter, 'BMXLEG', 'BMXARML', alpha=0.5).add_legend()

# NHANES variables for marital status and education level.
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 
                                       7: "Refused", 9: "Don't know"})
da["DMDMARTLx"] = da.DMDMARTL.replace({1: "Married", 2: "Widowed", 3: "Divorced", 4: "Separated", 5: "Never married",
                                      6: "Living w/partner", 77: "Refused"})
db = da.loc[(da.DMDEDUC2x != "Don't know") & (da.DMDMARTLx != "Refused"), :]

x = pd.crosstab(db.DMDEDUC2x, da.DMDMARTLx)
print(x)

#normalize between row
normrow = x.apply(lambda z: z/z.sum(), axis = 1)
normrow['sumrow'] = normrow.sum(axis = 1)
print(normrow)

#normalize between columns
normcol = x.apply(lambda z: z/z.sum(), axis = 0)
sumcol = normcol.sum(axis = 0)

print(normcol)
print(sumcol)

# The following line does these steps, reading the code from left to right:
# 1 Group the data by every combination of gender, education, and marital status
# 2 Count the number of people in each cell using the 'size' method
# 3 Pivot the marital status results into the columns (using unstack)
# 4 Fill any empty cells with 0
# 5 Normalize the data by row

group = db.groupby(["RIAGENDRx","DMDEDUC2x","DMDMARTLx"]).size().unstack().fillna(0).apply(lambda x: x/x.sum(), axis = 1)
print(group)

# Cond 1: age 40 - 49
cond_1 = db.loc[(db.RIDAGEYR >=40) & (db.RIDAGEYR < 50)] #locate only year 40 - 49
a = cond_1.groupby(["RIAGENDRx","DMDEDUC2x","DMDMARTLx"]).size().unstack().fillna(0).apply(lambda x: x/x.sum(), axis = 1)

# Cond 2: age 50 - 59
cond_2 = db.loc[(db.RIDAGEYR >=40) & (db.RIDAGEYR < 50)] #locate only year 40 - 49
b = cond_2.groupby(["RIAGENDRx","DMDEDUC2x","DMDMARTLx"]).size().unstack().fillna(0).apply(lambda x: x/x.sum(), axis = 1)

print(a.loc[:, ["Married"]].unstack())
print("")
print(b.loc[:, ["Married"]].unstack())

# Fixed categorical and quantitative data (Marital status and age)

plt.figure(figsize=(20,4))
plot_1 = sns.boxplot( x = db.DMDMARTLx, y = db.RIDAGEYR).set(title = "Marital Status vs Age",
                                                             xlabel ="Marital Status", ylabel="Age (year)")
plt.show()

plt.figure(figsize=(20,4))
plot_2 = sns.violinplot( x = db.DMDMARTLx, y = db.RIDAGEYR).set(title = "Marital Status vs Age",
                                                             xlabel ="Marital Status", ylabel="Age (year)")
plt.show()









