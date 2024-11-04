import numpy as np
from scipy import signal
from numpy.fft import fft, ifft, fft2, ifft2

# Create a gaussian target, with the same shape as x
# Should be largest at i=0 and smallest at i=len(x)/2
def create_gaussian_target1D(x, sigma):
    # TODO
    return None

# Return w, linear correlation filter for x and y
# y will be defined by your created gaussian function
def linear_correlation1D(x, sigma, lambda_val):
    # TODO
    return None

# return the index where the correlation filter returns the 
# highest value for z
def detect1D(w, z):
    # TODO
    return None

# Extend your previous function to 2D
def create_gaussian_target(x, sigma):
    # TODO
    return None

# Extend your previous function to 2D
def linear_correlation(x, sigma, lambda_val):
    # TODO
    return None

# Extend your previous function to 2D
def detect(w, z):
    # TODO
    
    return None




# TODO Modify your original correlation filter to account for linear noise type 1
def unblur1(x):
    return x



# TODO Modify your original correlation filter to account for linear noise type 2
def unblur2(x):
     return x
