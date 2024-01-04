import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 
import imageio
import os
import numpy as np

f = open("tau.txt", "r")
tau = f.read()
f = open("pi.txt", "r")
pi = f.read()
cm_subsectionTau = linspace(0.3, 1, 20) 
colorsTau = [cm.spring(x) for x in cm_subsectionTau]

fig = plt.figure(figsize=(30,30), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")
#PASCALS TRIANGLE IN TAU

counter = 0
minSize = 15
plotterTau = [[],[]]
colorCoorsTau = []
sizesTauCalc = [[minSize] for _ in range(100)]
sizesTau = []
size = 300
array = [[x & y for x in range(size)] for y in range(size)]
for row in range(len(array)):
    for col in range(len(array[0])):
        if int(tau[counter]) != 0:
            if array[row][col]%int(tau[counter]) == 0:
                plotterTau[0].append(row)
                plotterTau[1].append(col)
                colorCoorsTau.append(colorsTau[int(tau[counter])])
        counter += 1
ax.set_facecolor("black")
plt.scatter(plotterTau[0], plotterTau[1], color = colorCoorsTau, s = 20)
plt.xticks([], [])
plt.yticks([], [])
plt.tight_layout()
print("done")
plt.savefig("tauTests/h")

size = 250
array = [[] for _ in range(size)]
for i in range(size):
    for j in range(size):
        array[i].append(int(tau[i])^int(tau[j]))

# plotterTau = [[],[]]
# colorCoorsTau = []
# counter = 0
# prevTheta = 0 
# for row in range(len(array)):
#     for col in range(len(array[0])):
#         if int(tau[counter])!= 0:
#             newTheta = prevTheta + math.pi/(2*int(tau[counter]))
#         else:
#             newTheta = prevTheta
#         plotterTau[0].append((array[row][col]+counter**0.3)*math.cos(newTheta))
#         plotterTau[1].append((array[row][col]+counter**0.3)*math.sin(newTheta))
#         colorCoorsTau.append(colorsTau[array[row][col]])
#         prevTheta = newTheta
#         counter += 1


# ax.set_facecolor("black")
# plt.scatter(plotterTau[0], plotterTau[1], color = colorCoorsTau, s = 5)
# plt.xticks([], [])
# plt.yticks([], [])
# plt.tight_layout()
# print("done")
# plt.savefig("tauTests/9898")