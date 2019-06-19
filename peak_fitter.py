# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:49:57 2019

@author: Emily
"""

#!/usr/bin/env python3
"""fitting.py -- fits a two overlapping Gaussian peaks
Starting Code:
Mike Moran
mmoran0032@gmail.com
2016-06-28
Benjamin Rose
benjamin.rose@me.com
2017-06-20
Chris Seymour
seymour.16@nd.edu
2019-06-18
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def gaus(x, A, mu, sigma):
    """
    Returns y-value, for each given x, making a Gaussian.
    Parameters
    ----------
    x : numpy.array
        The input values for the Gaussian function. Similar to the x values 
        used in a plotting command.
    A : float
        Maximum value of the Gaussian.
    mu : float
        Location (along x-axis) for the center of the Gaussian. Maybe outside 
        the range of `x`.
    sigma : float
        Width of the Gaussian.
    Return
    ------
    numpy.array
        A y-value (in a Gaussian shape) for each `x` given.
    """
    return A * np.exp(-(x - mu)**2/(2 * sigma**2))

#Get data from 'two_peaks.txt' file.
x = []
y = []
infile = open("two_peaks.txt", "r")
for n in infile:
    n = n.rstrip("\n")
    n = n.split()
    n0 = float(n[0])
    n1 = float(n[1])
    x.append(n0)
    y.append(n1)
x = np.asarray(x)
plt.scatter(x, y)

#Define a function called fitter that fits two Gaussians to the data.
def fitter(x, A0, mu0, sigma0, A1, mu1, sigma1):
    """
    Function to fit to the data. Two Gaussians that... 
    A0 and A1; maxima on y-axis for each peak.
    mu0 and mu1; mean of each peak.
    sigma0 and sigma1; standard deviations of the data sets.
    """
    peak0 = gaus(x, A0, mu0, sigma0)
    peak1 = gaus(x, A1, mu1, sigma1)
    peak0.tolist()
    peak1.tolist()
    return peak0 + peak1

#Fit Gaussians to data and plot.
pars, _ = curve_fit(fitter, x, y)
plt.plot(x, fitter(x, *pars))
plt.show()

