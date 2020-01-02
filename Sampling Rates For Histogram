import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from matplotlib.widgets import Slider

%matplotlib notebook

colort = ('r','g','b','y')
n = 1000

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 1000)
x2 = np.random.gamma(2, 1.5, 1000)
#x3 = np.random.exponential(2, 1000)+7
#x4 = np.random.uniform(14,20, 1000)
x3 = x1
x4 = x1



def update(curr):
    gspec = gridspec.GridSpec(3, 2)

    if curr == n: 
        a.event_source.stop()
                     
    h1t = plt.subplot(gspec[0, 0])
    h2t = plt.subplot(gspec[1, 0])
    h1b = plt.subplot(gspec[2, 0])
    h2b = plt.subplot(gspec[:, 1])
    
    h1t.axis([-5,5,0,0.6])
    h2t.axis([-5,5,0,0.6])
    h1b.axis([-5,5,0,0.6])
    h2b.axis([-5,5,0,0.6])
    
    bins = np.arange(-4, 4, 0.5)    
    h1t.hist(x1[:curr], density=True, bins=bins, alpha=0.5,color='r')
    h2t.hist(x2[:curr], density=True, bins=bins, alpha=0.5,color='g')
    h1b.hist(x3[:curr], density=True, bins=bins, alpha=0.5,color='b')
    h2b.hist(x4[:curr], density=True, bins=bins, alpha=0.5,color='y')
    
    h1t.text(-1, 0.5, 'x1 Normal')
    h2t.text(-1, 0.5, 'x2 Gamma')
    h1b.text(-1, 0.5, 'x3 Exponential')
    h2b.text(-1, 0.5, 'x4 Uniform')
    
    return
    
fig = plt.figure('Sampleing Rates For Histogram', figsize=(7, 5))

a = animation.FuncAnimation(fig, update, interval=1)

