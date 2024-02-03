import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

with open('scimark\SOR_log_sheng2080.txt') as file:
    lines = file.readlines()
    data = np.array([float(line.strip()) for i, line in enumerate(lines) if i % 2 == 1])
plt.boxplot(data)
#sns.boxplot(x=data, color='lightgreen')
plt.title('Distribution of Running Times')
plt.xlabel('Dataset')
plt.ylabel('Running Time (seconds)')

# Show the plot
plt.show()


running_times = np.random.uniform(3, 25, size=100)

plt.figure(figsize=(10, 6))
sns.histplot(data, bins=20, kde=True, color='blue')
plt.title('Distribution of Running Times')
plt.xlabel('Running Time (seconds)')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10, 6))
sns.kdeplot(data, color='orange', fill=True)
plt.title('Kernel Density Plot of Running Times')
plt.xlabel('Running Time (seconds)')
plt.ylabel('Density')
plt.show()