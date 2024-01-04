import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 

f = open("pi.txt", "r")
pi = f.read()

f = open("tau.txt", "r")
tau = f.read()

cm_subsectionPi = linspace(0, 0.5, 10) 
colorsPi = [cm.cool(x) for x in cm_subsectionPi]

cm_subsectionTau = linspace(0.3, 1, 10) 
colorsTau = [cm.spring(x) for x in cm_subsectionTau]

fig = plt.figure(figsize=(25,25), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotterPi = [[[0],[0]] for _ in range(10)]
directionPi = [[0] for _ in range(10)]
actuallyPlotPi = [[] for _ in range(10)]

plotterTau = [[[0],[0]] for _ in range(10)]
directionTau = [[0] for _ in range(10)]
actuallyPlotTau = [[] for _ in range(10)]


for i in range(100000-1):
    for index in range(10):
        if index != 0:
            if int(pi[i]) == index:
                directionPi[index].append(directionPi[index][i]+math.pi/(2*int(pi[i])))
                actuallyPlotPi[index].append(1)
            else:
                directionPi[index].append(directionPi[index][i])
                actuallyPlotPi[index].append(0)
            plotterPi[index][0].append(plotterPi[index][0][i]+math.cos(directionPi[index][i+1]))
            plotterPi[index][1].append(plotterPi[index][1][i]+math.sin(directionPi[index][i+1]))
    
    for index in range(10):
        if index != 0:
            if int(tau[i]) == index:
                directionTau[index].append(directionTau[index][i]+math.pi/(2*int(tau[i])))
                actuallyPlotTau[index].append(1)
            else:
                directionTau[index].append(directionTau[index][i])
                actuallyPlotTau[index].append(0)
            plotterTau[index][0].append(plotterTau[index][0][i]+math.cos(directionTau[index][i+1]))
            plotterTau[index][1].append(plotterTau[index][1][i]+math.sin(directionTau[index][i+1]))

for line in range(len(plotterPi)):
    xCoors = [plotterPi[line][0][index] for index in range(len(actuallyPlotPi[line])) if actuallyPlotPi[line][index] == 1]
    yCoors = [plotterPi[line][1][index] for index in range(len(actuallyPlotPi[line])) if actuallyPlotPi[line][index] == 1]
    plt.scatter(xCoors, yCoors, color = colorsPi[line], s= 0.1)

for line in range(len(plotterTau)):
    xCoors = [plotterTau[line][0][index] for index in range(len(actuallyPlotTau[line])) if actuallyPlotTau[line][index] == 1]
    yCoors = [plotterTau[line][1][index] for index in range(len(actuallyPlotTau[line])) if actuallyPlotTau[line][index] == 1]
    plt.scatter(xCoors, yCoors, color = colorsTau[line], s= 0.1)

plt.xticks([], [])
plt.yticks([], [])
plt.tight_layout()
plt.savefig("colorfulGoopWithTau20.png")
plt.show()
