import random
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as ss
import statistics
import time

def rejection_method(fun, n, xmin, xmax):
    """
    Generating n random variables from probability density function fun on the inerval [xmin, xmamx]
    fun - propability density function defined as python function,
    n - number of need variables
    xmin - start of the interval,
    xmax - end of the inerval.
    """
    if xmin > xmax:
        raise ValueError("Value of xmax should be larger than value of xmin.")
    x = np.linspace(xmin, xmax, 1000)
    y = fun(x)
    ymin = y.min()
    ymax = y.max()

    variables = []
    while len(variables) < n:
            x = random.uniform(xmin, xmax)
            y = random.uniform(ymin, ymax)

            if y < fun(x):
                variables.append(x)

    return variables

def f(x):
    """PDF"""
    return 3.0/2.0 * np.sin(x) * np.cos(x) * np.cos(x)

def rejection_method_plot():
    variables = rejection_method(f, 100000, 0, math.pi)

    plt.hist(variables, 50, density = 1)
    plt.title("Frequency histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    x = np.linspace(0, math.pi, 1000)
    plt.plot(x, f(x))
    plt.legend(["PDF", "Histogram"])
    plt.show()

def rejection_method_average_time_plot():
    times = []
    for i in range(100):
        start = time.time()
        rejection_method(f, 100000, 0, math.pi)
        end = time.time()
        times.append(end - start)

    plt.hist(times)
    plt.grid()
    plt.title("Histogram of time to generate 100 000 random variables using python loops")
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency")
    plt.show()

def optimization(f, xmin, xmax, m, n):
    """
    Optimised function to generate random variables from pdf: f(x): 3/2 * sin(x) * (cos(x))^2
    on the inerval [0, pi] using numpy functions.
    f - propability density function defined as python function,
    n - number of need variables
    xmin - start of the interval,
    xmax - end of the inerval.
    m - maximum of function f to generate more variables than n, chosen by trial and error
    method to obtained defined more than n variables
    """

    M = int(n * m * (xmax-xmin))
    x = np.linspace(xmin, xmax, 1000)

    u1 = np.random.uniform(xmin, xmax, M)
    u2 = np.random.uniform(0.0, f(x).max(), M)

    variables = np.where(u2 <= f(u1), u1, -1)
    accepted = np.extract(variables>=0.0, variables)
    accepted = accepted[0:n]

    return accepted

def compare_histogram():
    before_optimization = rejection_method(f, 100000, 0, math.pi)
    after_optimization = optimization(f, 0, math.pi, 0.6, 100000)
    print(before_optimization)
    x = np.linspace(0, math.pi, 1000)
    plt.hist(after_optimization, 50, density=1)
    plt.hist(before_optimization, 50, density=1)
    plt.plot(x, f(x))
    plt.title("Compare histograms")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.legend([ 'PDF', 'before optimization', 'after optimisation'])
    plt.grid()
    plt.show()

def optimization_average_time_plot():
    times = []
    for i in range(100):
        start = time.time()
        optimization(f, 0, math.pi, 0.6, 100000)
        end = time.time()
        times.append(end - start)

    plt.hist(times)
    plt.grid()
    plt.title("Histogram of time to generate 100 000 random variables using numpy arrays")
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency")
    plt.show()

def compare_time_of_calculation():
    samples = [1000, 5000, 10000, 50000, 100000]
    times_before_optimization = []
    times_after_optimization = []
    for item in samples:
        time_before_optimization = []
        time_after_optimization = []
        for i in range(100):
            start = time.time()
            before_optimization = rejection_method(f, item, 0, math.pi)
            end = time.time()
            time_before_optimization.append(end - start)

            start = time.time()
            after_optimization = optimization(f, 0, math.pi, 0.6, item)
            end = time.time()
            time_after_optimization.append(end - start)
        times_before_optimization.append(statistics.mean(time_before_optimization))
        times_after_optimization.append(statistics.mean(time_after_optimization))


    plt.plot(samples, times_before_optimization, '.')
    plt.plot(samples, times_after_optimization, '.')
    plt.title("Compare average time of generating random variables")
    plt.xlabel("Number N of generating random variables")
    plt.ylabel("Średni czas w sekundach")
    plt.legend(["before optimization","after optimization"])
    plt.show()

rejection_method_plot()
rejection_method_average_time_plot()
compare_histogram()
optimization_average_time_plot()
compare_time_of_calculation()