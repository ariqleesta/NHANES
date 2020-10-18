import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

random.seed(1234) # For generating random number in particular seed
a = random.random() # Generate random value between 0 - 1
print(a)

random.seed(1111) # Different seed, different random number
b = random.random()
print(b) 

# We can re run exact same seed and obtain the exact same random number

random.seed(1111) # Different seed, different random number
c = random.random()
print(c) 

# Without seed, we cant monitor the value
d = random.random()
e = random.random()
print(d) 
print(e) 

# We can generate random number between intervals

n = 10
for i in range(n):
    f = random.uniform(10,25)
    print(f)
    
# or with list comprehensive
z = [random.uniform(10,25) for i in range(n)]
print(z)

# Creating normal distribution
n = 1000
mean = 20
std = 4
norm_dist = [random.normalvariate(mean,std) for i in range(n)]
sns.distplot(norm_dist)
plt.show()

# Random sampling from a population

# Creating population
mu = 0
sigma = 1
population = [random.normalvariate(mu, sigma) for _ in range(10000)]

# Sampling

SampleA = random.sample(population, 500) #(population,sample size)
SampleB = random.sample(population, 500)

print('mean SampleA: ', np.mean(SampleA))   # Nearly mu = 0
print('std SampleA: ', np.std(SampleA))     # Nearly sigma = 1
print('mean SampleB: ', np.mean(SampleB)) 
print('std SampleB: ', np.std(SampleB)) 

# Calculating the mean for 100 sample of size 1000
means = [np.mean(random.sample(population,1000)) for _ in range(100)]
#print(means)

print('Mean of the sample means is: ', np.mean(means)) # Nearly close to 0

# Calculating the standard deviation for 100 sample of size 1000
stds = [np.std(random.sample(population,1000)) for _ in range(100)]
#print(means)

print('Mean of the sample stds is: ', np.mean(stds)) # Nearly close to 1
