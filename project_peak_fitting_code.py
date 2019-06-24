import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#Open the file.
infile = open("152Eu_data.txt", 'r')
#Create an x-axis and y-axis array.
xs = []
ys = []
for n in infile:
    n = n.rstrip("\n")
    n = n.split()
    x = int(n[0])
    xs.append(x)
    y = int(n[1])
    ys.append(y)
infile.close()  
plt.plot(xs, ys)  
slopes = np.gradient(ys)
#Make a dictionary of the heights corresponding to each position.
xydictionary = {}
for n in range(len(xs)):
    key = ys[n]
    value = xs[n]
    xydictionary[key] = value
ys.sort()
highest = ys[8150:]
high_xs = []
for n in highest:
    to_add = xydictionary[n]
    high_xs.append(to_add)     
#Instead, use gradient.
slopes.tolist()
graddict = {}
for n in range(len(ys)):
    key = slopes[n]
    value = xs[n]
    graddict[key] = value
slopes.sort()
highest_slopes = slopes[8160:]
slope_xs = []
for m in highest_slopes:
    addme = graddict[m]
    slope_xs.append(addme)
slope_xs.sort()
peaks_ = [slope_xs[0]]
#Only have one point per peak.
for n in range(len(slope_xs) - 1):
    diff = abs(slope_xs[n] - slope_xs[n + 1])
    if diff > 20:
        peaks_.append(slope_xs[n + 1])
#plt.scatter(peaks_, np.linspace(800, 810, 8), color = 'red')
#Now peak fitting; means/centroids = positions of red dots.
#Width of each curve = 6 * StDev.  Average width = 10.33; average StDev = 1.7.
#Heights can be obtained by observation (approximate)
heights = [1500, 590, 1320, 670, 670, 500, 550, 800]
mean_height = []
for i in range(len(heights)):
    m_h = [peaks_[i], heights[i]]
    mean_height.append(m_h)    
def gaus(x, A, mu, sigma):
    """
    Returns y-value, for each given x, making a Gaussian.
    """
    return A * np.exp(-(x - mu)**2/(2 * sigma**2))
x_array = np.asarray(xs)
master_list = []
for n in mean_height:
    mu = float(n[0])
    height = float(n[1])
    normal_plot = gaus(x_array, height, mu, 1.7)
    master_list.append(normal_plot)
    plt.plot(x_array, normal_plot)
plt.show()
#Fit Gaussians to data and plot.
y_array = np.asarray(ys)
pars, _ = curve_fit(gaus, x_array, y_array)
plt.plot(x, gaus(x, *pars))
plt.show()