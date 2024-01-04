import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 
import imageio
import os

f = open("pi.txt", "r")
pi = f.read()

f = open("tau.txt", "r")
tau = f.read()

cm_subsectionPi = linspace(0, 0.5, 10) 
colorsPi = [cm.cool(x) for x in cm_subsectionPi]

cm_subsectionTau = linspace(0.3, 1, 10) 
colorsTau = [cm.spring(x) for x in cm_subsectionTau]

fig = plt.figure(figsize=(30,30), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotterPi = [[],[]]
colorCoorsPi = []
plotterTau = [[],[]]
colorCoorsTau = []
for i in range(20000):
    piNum = int(pi[i])
    plotterPi[0].append((piNum+counter**0.5)*math.cos(2*math.pi*counter**0.5))
    plotterPi[1].append((piNum+counter**0.5)*math.sin(2*math.pi*counter**0.5))
    colorCoorsPi.append(colorsPi[piNum])
    tauNum = int(tau[i])
    plotterTau[0].append((tauNum+counter**0.5)*math.cos(2*math.pi*counter**0.5))
    plotterTau[1].append((tauNum+counter**0.5)*math.sin(2*math.pi*counter**0.5))
    colorCoorsTau.append(colorsTau[tauNum])
    counter += 1
ax.set_facecolor("black")
plt.scatter(plotterPi[0], plotterPi[1], color = colorCoorsPi, s = 18)
plt.scatter(plotterTau[0], plotterTau[1], color = colorCoorsTau, s = 18)
plt.xticks([], [])
plt.yticks([], [])
plt.tight_layout()
plt.savefig("deathStarTau")