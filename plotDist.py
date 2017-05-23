from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import sys
from itertools import groupby
from collections import Counter
import decimal 

#positive
filename = sys.argv[1]
file = open(filename,'r')
data = file.readlines()
array = []
for element in data:
	element = element.replace('\n', '')
	array.append(int(element))

#negative
filename = sys.argv[2]
file = open(filename, 'r')
data = file.readlines()
array2 = []
for element in data:
	element = element.replace('\n', '')
	array2.append(int(element))


#positive control
density = gaussian_kde(array)
bins = np.linspace(-10,1000,1010)
xs = bins
density.covariance_factor = lambda : .5
density._compute_covariance()

#negative control
density2 = gaussian_kde(array2)
bins2 = np.linspace(-10,1000,1010)
xs2 = bins2
density2.covariance_factor = lambda : .5
density2._compute_covariance()

#Calculates posterior probabilities 
posterior = []
positive = density(xs)
negative = density2(xs2)
for i in range(len(density(xs))):
	post = (positive[i]*0.6)/((positive[i]*0.6) + negative[i]*0.4)
	posterior.append(post)

#posterior
density3 = gaussian_kde(posterior)
bins3 = np.linspace(-10,10,100)
xs3 = bins3
density3.covariance_factor = lambda : .5
density3._compute_covariance()

#view graph
plt.plot(xs,density(xs), '')
#plt.plot(xs,density(xs), '', xs2,density2(xs2), '')
plt.show()





