import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 
import imageio
import os
import numpy as np

f = open("tau.txt", "r")
tau = f.read()

cm_subsectionTau = linspace(0.3, 1, 10) 
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
array = [[x + y^size for x in range(size)] for y in range(size)]
for row in range(len(array)):
    for col in range(len(array[0])):
        if int(tau[counter]) != 0:
            if array[row][col]%int(tau[counter]):
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
plt.savefig("alsdfjdklsafjds")





# for i in range(10000):
#     tauNum = np.log(int(tau[i])+counter)
#     for j in range(10):
#         plotterTau[0]
#     plotterTau[0].append(tauNum*math.cos(2*math.pi*int(tau[i])))
#     plotterTau[1].append(tauNum*math.sin(2*math.pi*int(tau[i])))
#     colorCoorsTau.append(colorsTau[int(tau[i])])
#     sizesTau.append(int(tau[i])*10)
    # if tauNum != 0:
    #     plotterTau[0].append((tauNum+counter**0.5)*math.cos(2*math.pi*counter**(1/tauNum)))
    #     plotterTau[1].append((tauNum+counter**0.5)*math.sin(2*math.pi*counter**(1/tauNum)))
    # colorCoorsTau.append(colorsTau[tauNum])
    # for num in range(10):
    #     if num == tauNum:
    #         sizesTauCalc[num].append(sizesTauCalc[num][i] * 2)
    #     else:
    #         if sizesTauCalc[num][i] >= minSize:
    #             sizesTauCalc[num].append(sizesTauCalc[num][i] * 0.7)
    #         else:
    #             sizesTauCalc[num].append(sizesTauCalc[num][i] * 1)
    # sizesTau.append(sizesTauCalc[tauNum][i+1])