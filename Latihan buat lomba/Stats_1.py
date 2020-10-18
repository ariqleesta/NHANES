import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 100)

path = "nhanes_2015_2016.csv"

#importing csv from path
df = pd.read_csv(path)
print(df.head()) #in jupyter u dont have to print, just df.head()

#how many columns
counts = 0
x = df.columns
for i in x:
    counts = counts + 1
print(x)
print('how many columns? ', counts)
    


# Lets only consider the feature (or variable) 'BPXSY2'
bp = df['BPXSY2']
print(bp)


# What is the mean of 'BPXSY2'?
bp = bp.dropna()

bp_mean = np.mean(bp)
print('mean: ',bp_mean)

bp_median = bp.median()
print('median: ',bp_median)

bp_max = bp.max()
print('max: ',bp_max)

bp_min = bp.min()
print('max: ',bp_min)

bp_std = bp.std()
print('std: ',bp_std)

bp_var = bp.var()
print('var: ',bp_var)

bp_iqr = stats.iqr(bp)
print('iqr: ',bp_iqr)

bp_descriptive_stats = bp.describe()
print(bp_descriptive_stats)

# Using the fact that 'bp' is a pd.Series object, can use the pd.Series method diff()
# call this method by: pd.Series.diff()
diff_by_series_method = bp.diff() 
# note that this returns a pd.Series object, that is, it had an index associated with it
print(diff_by_series_method.values) # only want to see the values, not the index and values

# Now use the numpy library instead to find the same values
# np.diff(array)
diff_by_np_method = np.diff(bp)
print(diff_by_np_method)
# note that this returns an 'numpy.ndarray', which has no index associated with it, and therefore ignores
# the nan we get by the Series method

# We could also implement this ourselves with some looping
diff_by_me = [] # create an empty list
for i in range(len(bp.values)-1): # iterate through the index values of bp
    diff = bp.values[i+1] - bp.values[i] # find the difference between an element and the previous element
    diff_by_me.append(diff) # append to out list
print(np.array(diff_by_me)) # format as an np.array

a = bp
sns.distplot(a = bp).set(title='Blood Pressure Systolic 2', xlabel=('Blood Pressure in mm/Hg'), ylabel=('Frequency'))
plt.show()

# Make a boxplot of our 'bp' data using the seaborn library. Make sure it has a title and labels!
sns.boxplot(bp).set(title='Blood Pressure Systolic 2', xlabel=('Blood Pressure in mm/Hg'), ylabel=('Frequency'))
plt.show()
