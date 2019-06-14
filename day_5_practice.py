#1. Implement a function integrator using the trapezoid rule.
import numpy as np
def trapezoid(function, interval_start, interval_end, intervals = 10):
    """Default = 10 intervals"""
    #Divide the interval into sub-intervals.
    range_ = interval_end - interval_start
    #Width of each interval:
    dx = range_ / intervals
    #Find all of the x values.
    values = np.linspace(interval_start, interval_end, intervals + 1)
    trap = 0
    for n in range(values - 1):
        trap += (dx * (function(values[n + 1]) + function(values[n]))) / 2
    return trap
    
#2. Implement a function integrator using Simpson's rule.
def simpson(function, interval_start, interval_end):
    """Arguments = function, interval start and interval end."""
    """Integrates a function using Simpson's rule."""
    h = (interval_end - interval_start) / 3
    factor = (function(interval_start) + 3*function((2*interval_start + interval_end) / 3) + 3*function((interval_start + 2*interval_end) / 3) + function(interval_end))
    integral = (3 * h / 8) * factor
    return integral

#3. Implement a root finder using Newton's method.
def newton(function, df, x_init, error):
    """Arguments = function, df, x_init and error."""
    """Finds the roots of the function using Newton's method."""
    delta = dx(function, x_init)
    while delta > error:
        x_init = x_init - function(x_init)/df(x_init)
        delta = dx(function, x_init)
    print("Root is at: ", x_init)
    print("f(x) at root is: ", function(x_init))    
    
def dx(function, x):
    return abs(0 - function(x))

#4. Implement a root finder using the secant method.
def secant(f, x0, x1, epsilon):
    """Assumes that the function is approximately linear in the region of interest."""
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > epsilon and iteration_counter < 100:
        denominator = float(f_x1 - f_x0)/(x1 - x0)
        if denominator != 0:
            x = x1 - float(f_x1)/denominator
        else:
            print("Error! Denominator = 0!")
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
     if abs(f_x1) > epsilon:
         iteration_counter -= 1
     return x, iteration_counter    
        
        
        