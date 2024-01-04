import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 
import imageio
import os

f = open("pi.txt", "r")
pi = f.read()
print(len(pi))

cm_subsection = linspace(0, 0.5, 10) 
colors = [cm.cool(x) for x in cm_subsection]

fig = plt.figure(figsize=(30,30), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotter = [[],[]]
colorCoors = []
for i in range(len(pi[:20000])):
    piNum = int(pi[i])
    plotter[0].append((piNum+counter**0.5)*math.cos(2*math.pi*counter**0.5))
    plotter[1].append((piNum+counter**0.5)*math.sin(2*math.pi*counter**0.5))
    colorCoors.append(colors[piNum])
    # plt.scatter(plotter[0], plotter[1], color = colorCoors, s = 1)
    # plt.xlim((-100, 100))
    # plt.ylim((-100, 100))
    # plt.xticks([], [])
    # plt.yticks([], [])
    # plt.tight_layout()
    #plt.savefig(f"gif/{counter}.png")
    # plt.draw()
    # plt.pause(0.01)
    # plt.clf()
    counter += 1
ax.set_facecolor("black")
plt.scatter(plotter[0], plotter[1], color = colorCoors, s = 18)
plt.xticks([], [])
plt.yticks([], [])
plt.tight_layout()
plt.savefig("deathStarMorepng")