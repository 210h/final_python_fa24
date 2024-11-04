import numpy as np
from filter import *

# This is for you to make sure your code works 
# Feel free to modify this however you wish :)
def main():
    x = np.zeros(100)
    x[:10] = np.arange(10) # create test signal
    
    w = linear_correlation1D(x, 2, 0)

    i = 50
    z = np.roll(x, i) # test detection space

    detected = detect1D(w, z)
    print(f"detected x at {detected}, actual position: {i}")

if __name__ == '__main__':
    main()