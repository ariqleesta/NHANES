import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load nhanes data from directory
# Look at the variable explorer panes
da = pd.read_csv('nhanes_2015_2016.csv')

# Know the indexes first
print(da.columns)

# Frequency tables for DMDEDUC2 Variable for non missing education status
print(da.DMDEDUC2.value_counts())

# Sum DMDEDUC2 value counts
SumDMDEDUC2 = sum(da.DMDEDUC2.value_counts()) 
print(SumDMDEDUC2)

# or
SumDMDEDUC2 = da.DMDEDUC2.value_counts().sum()
print(SumDMDEDUC2)

# Size of the data
print(da.shape)
Sumda = da.shape[0]

# Determine missing value
MissDMDEDUC2 = Sumda - SumDMDEDUC2
print(MissDMDEDUC2)

# or
MissDMDEDUC2 = pd.isnull(da.DMDEDUC2).sum()
print(MissDMDEDUC2)

# Replacing integer code of DMDEDUC2 with  text label
da['DMDEDUC2x'] = da.DMDEDUC2.replace({1: "<9", 2:"9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know"})
print(da.DMDEDUC2x.value_counts())

# Frequency tables for RIAGENDR Variable for education status
print(da.RIAGENDR.value_counts())

# Replacing integer code of RIAGENDR with male and female
da['RIAGENDRx'] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
print(da.RIAGENDRx.value_counts())

# Make a proportion each DMDEDUC2x 
x = da.DMDEDUC2x.value_counts()
x = x/x.sum()
print(x) # total dari x = 1 not include missing value

# Insert missing value in the proportion
da['DMDEDUC2x'] = da.DMDEDUC2x.fillna('Missing')
x = da.DMDEDUC2x.value_counts()
x = x/x.sum()
print(x)

# NUMERICAL SUMMARIES
# Numerical summaries for Body Mass Variable, include missing body mass using dropna()
print(da.BMXWT.dropna().describe())

# Numerical Individual Summaries
x = da.BMXWT.dropna()  # Extract all non-missing values of BMXWT into a variable called 'x'
print('Mean is: ', x.mean()) # Pandas method
print('Mean is: ', np.mean(x)) # Numpy function

print('Median is: ', x.median()) #Pandas method
print('Median is: ', np.percentile(x, 50))  # 50th percentile, same as the median
print('3rd percentile is: ', np.percentile(x, 75))  # 75th percentile
print('3rd percentile is: ', x.quantile(0.75)) # Pandas method for quantiles, equivalent to 75th percentile

# We look frequency of Systolic or Diastolic Blood Pressure
# Systolic blood pressure measurement (BPXSY1) (BPXSY2)
# Diastolic blood pressure measurement (BPXDI1) (BPXDI2)
# "1" indicates that this is the first of three systolic blood presure measurements taken on a subject.

# A person is generally considered to have pre-hypertension 
# when their systolic blood pressure is between 120 and 139, 
# or their diastolic blood pressure is between 80 and 89.

# Pre-hypertensive based on systolic blood pressure.
print (np.mean((da.BPXSY1 >= 120) & (da.BPXSY2 <= 139))) # "&" means "and"

# Pre-hypertensive based on diastolic blood pressure.
print (np.mean((da.BPXDI1 >= 80) & (da.BPXDI2 <= 89)))

# Proportion of NHANES subjects who are pre-hypertensive based on either systolic or diastolic blood pressure.
a = (da.BPXSY1 >= 120) & (da.BPXSY2 <= 139)
b = (da.BPXDI1 >= 80) & (da.BPXDI2 <= 89)
print(np.mean(a | b)) # "|" means "or"

# Mean difference between the first two systolic or diastolic blood pressure measurements.
# For "white coat anxiety", in which a subject's bood pressure may be slightly elevated if they are nervous when interacting with health care providers.
print(np.mean((da.BPXSY1)-(da.BPXSY2)))
print(np.mean((da.BPXDI1)-(da.BPXDI2)))

# GRAPHICAL SUMMARIES
# Plot body mass histogram and PDF
sns.distplot(da.BMXWT.dropna())
plt.show()

# Plot Blood Pressure Boxplot and Histogram
bp = sns.boxplot(data = da.loc[:, ["BPXSY1", "BPXSY2","BPXDI1", "BPXDI2"]])
bp.set_ylabel("Blood Pressure in mm/Hg")

# Boxplot of BPXSY1 of each age group
da['agegrp'] = pd.cut(da.RIDAGEYR,[18, 30, 40 , 50 , 60, 70, 80]) # Create age stratas based on cut points
plt.figure(figsize=(12,5)) #make the figure wider 12 cm wide and 45 cm height
sns.boxplot(x = 'agegrp', y = 'BPXSY1', data = da)

# Boxplot of BPXSY1 of each age group for men and women
da['agegrp'] = pd.cut(da.RIDAGEYR,[18, 30, 40 , 50 , 60, 70, 80]) # Create age stratas based on cut points
plt.figure(figsize=(12,5)) #make the figure wider 12 cm wide and 45 cm height
sns.boxplot(x = 'agegrp', y = 'BPXSY1', hue = 'RIAGENDRx', data =da)

# Differenciate boxplot into male and female with distinct ages
da['agegrp'] = pd.cut(da.RIDAGEYR,[18, 30, 40 , 50 , 60, 70, 80]) # Create age stratas based on cut points
plt.figure(figsize=(12,5)) #make the figure wider 12 cm wide and 45 cm height
sns.boxplot(x = 'RIAGENDRx', y = 'BPXSY1', hue = 'agegrp', data =da)

# Value count the Education Attaintment based on their age group
print(da.groupby("agegrp")["DMDEDUC2x"].value_counts())

# Pivoting DMDEDUC2x into collumns
# Interpret the value into proportion of probability

dx = da.loc[~da.DMDEDUC2x.isin(["Don't know","Missing"])] #Eliminates "Don't know" and "Missing" data
dx = dx.groupby(["agegrp", "RIAGENDRx"])["DMDEDUC2x"].value_counts() #grouping education into gender and distinct ages
dx = dx.unstack() #Restructure the results from long to wide
dx = dx.apply(lambda x: x/x.sum(),axis=1) #Normalize within each stratum to get proportions
print(dx.to_string(float_format="%.3f"))
