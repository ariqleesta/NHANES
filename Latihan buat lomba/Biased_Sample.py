# import the packages
import numpy as np # for sampling and data generation
import matplotlib.pyplot as plt # for basic plotting commands
import seaborn as sns; sns.set() # for plotting histograms

# Recreate the simulations from the video
mean_non_gym = 155 #lb
sd_non_gym = 5
mean_gym = 185 #lb
sd_gym = 5
gymperc = 0.30
totalpopsize = 40000 #people

# Create the two subgroups
non_gym = np.random.normal(mean_non_gym,sd_non_gym, int(totalpopsize*(1-gymperc)))
gym = np.random.normal(mean_gym, sd_gym, int(totalpopsize*gymperc))

# Combine subgroups
population = np.append(non_gym, gym)

# Set up the figure for plotting
plt.figure(figsize=((10,10)))

# Plot non_gym
plt.subplot(3,1,1) # (num row, num col, index)
sns.distplot(non_gym)
plt.title('Non Gym Goers')
plt.xlim([140,200]) #limit the x axis (plt.ylim for limit the y axis)

# Plot gym
plt.subplot(3,1,2) # (num row, num col, index)
sns.distplot(gym)
plt.title('Gym Goers')
plt.xlim([140,200])

# Plot both groups together
plt.subplot(3,1,3) # (num row, num col, index)
sns.distplot(population)
plt.title('Total Population')
plt.axvline(x = np.mean(population)) # vertical x axis value
plt.xlim([140,200])
plt.show()

# WHAT HAPPENS If we sample from the entire population

# Simulation parameters
numberSamps = 5000
sampSize = 50

# Get the sampling distribution of the mean for all students
mean_distribution = np.empty(numberSamps) #make vector for numberSamp

# Create loop
for i in range(numberSamps):
    random_students = np.random.choice(population, sampSize) #taking sample size of 50 students from population
    mean_distribution[i] = np.mean(random_students)
    
# Set up the figure for plotting
plt.figure(figsize=((10,8)))

# Plotting the total population (again)
plt.subplot(2,1,1) # (num row, num col, index)
sns.distplot(population)
plt.title('Total Population')
plt.axvline(x = np.mean(population)) # vertical x axis value
plt.xlim([140,200])

# Plotting the sampling distribution of the mean
plt.subplot(2,1,2) # (num row, num col, index)
sns.distplot(mean_distribution)
plt.title('Sampling Distribution of the Mean Weight')
plt.axvline(x = np.mean(population)) # vertical x axis value
plt.axvline(x = np.mean(mean_distribution), color = 'black')
plt.xlim([140,200])

plt.show()

# What if we sampling from non-representative population

# Simulation parameters
numberSamps = 5000
sampSize = 50

# Get the sampling distribution of the mean for all students
mean_distribution = np.empty(numberSamps) #make vector for numberSamp

# Create loop
for i in range(numberSamps):
    random_students = np.random.choice(gym, sampSize) #taking sample size of 50 students from population
    mean_distribution[i] = np.mean(random_students)
    
# Set up the figure for plotting
plt.figure(figsize=((10,8)))

# Plotting the total population (again)
plt.subplot(2,1,1) # (num row, num col, index)
sns.distplot(population)
plt.title('Total Population')
plt.axvline(x = np.mean(population)) # vertical x axis value
plt.xlim([140,200])

# Plotting the sampling distribution of the mean
plt.subplot(2,1,2) # (num row, num col, index)
sns.distplot(mean_distribution)
plt.title('Sampling Distribution of the Mean Weight')
plt.axvline(x = np.mean(population)) # vertical x axis value
plt.axvline(x = np.mean(mean_distribution), color = 'black')
plt.xlim([140,200])

plt.show() # The result will be biased, the sampled mean is located far away from population mean
