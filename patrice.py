import numpy as np
import matplotlib.pyplot as plt 
import scipy as sc

def patrice(x):
	return -x+4+x*sc.exp(-x)

print patrice(0)
