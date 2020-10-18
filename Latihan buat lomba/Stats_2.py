# Normal dist empirical rules (68 , 95 , 99.7 rules)

import warnings
warnings.filterwarnings('ignore')
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

random.seed(1738)

# Set parameters
mu = 7 # Hours of sleep
sigma = 1.7 # Standard deviation of hours of sleep

# Creating population
Observation = [random.normalvariate(mu, sigma) for i in range(100000)]

# Plotting observation
sns.distplot(Observation,color = 'green')

# For 68% (mean +- std)
plt.axvline(np.mean(Observation) + np.std(Observation), color = 'red')
plt.axvline(np.mean(Observation) - np.std(Observation), color = 'red')

# For 95% (mean +- 2*std)
plt.axvline(np.mean(Observation) + 2*np.std(Observation), color = 'blue')
plt.axvline(np.mean(Observation) - 2*np.std(Observation), color = 'blue')

# For 99.7% (mean +- 3*std)
plt.axvline(np.mean(Observation) + 3*np.std(Observation), color = 'yellow')
plt.axvline(np.mean(Observation) - 3*np.std(Observation), color = 'yellow')

plt.show()

# Descriptive statistic summaries

desc = pd.Series(Observation).describe()
print(desc)

# Sampling with size of 100

SampleA = random.sample(Observation, 100)
SampleB = random.sample(Observation, 100)
SampleC = random.sample(Observation, 100)

# Plotting sample
fig, ax = plt.subplots() # without (row,col,index), will overlay
sns.distplot(SampleA, ax = ax)
sns.distplot(SampleB, ax = ax)
sns.distplot(SampleC, ax = ax)

plt.show()

# Re plot the population
sns.distplot(Observation)

plt.axvline(np.mean(Observation) + np.std(Observation), 0, .59, color = "g")
plt.axvline(np.mean(Observation) - np.std(Observation), 0, .59, color = "g")

plt.axvline(np.mean(Observation) + (np.std(Observation) * 2), 0, .15, color = "y")
plt.axvline(np.mean(Observation) - (np.std(Observation) * 2), 0, .15, color = "y")

plt.show()

# Creating CDF
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt

ecdf = ECDF(Observation)

print(ecdf.x) # interval of hours of sleep
print(ecdf.y) # interval of probability

plt.plot(ecdf.x,ecdf.y)

plt.axhline(y = 0.025, color = 'y', linestyle='-')
plt.axvline(x = np.mean(Observation) - (2 * np.std(Observation)), color = 'y', linestyle='-')

plt.axhline(y = 0.975, color = 'y', linestyle='-')
plt.axvline(x = np.mean(Observation) + (2 * np.std(Observation)), color = 'y', linestyle='-')

plt.show()
