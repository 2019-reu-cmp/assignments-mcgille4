import numpy as np
#Get the data from the file.
infile = open('more_sunspots.txt', 'r')
xs = []
ys = []
for n in infile:
    n = n.rstrip('\n')
    n = n.split()
    xs.append(float(n[0]))
    ys.append(float(n[1]))
infile.close() 
xs_new = np.asarray(xs)
ys_new = np.asarray(ys)  
import matplotlib.pyplot as plt
#Plot a scatter plot.
plt.plot(xs_new, ys_new, color = 'white', marker = 'o', mec = 'blue', mfc = 'blue', markersize = 4)
plt.xticks(np.arange(0, 3143, 500))
plt.yticks(np.arange(0, 275, 50))
#Now plot the moving average.
#For every 5 months, find the average and plot it.
moving_average = []
for i in range(len(ys) - 5):
    values = ys[i:i+5]
    total = sum(values)
    ave = total / 5 
    moving_average.append(ave)
plt.plot(xs[:-5], moving_average, color = 'red', linewidth = 2)    
plt.show()
#Now plot a histogram.
plt.hist(ys_new, color = 'green', edgecolor = 'black', linewidth = 1.2)
plt.xlabel("Number of Sunspots")
plt.ylabel("Frequency")
plt.plot()

