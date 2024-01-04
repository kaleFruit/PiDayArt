import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 

f = open("pi.txt", "r")
pi = f.read()

f = open("tau.txt", "r")
tau = f.read()

cm_subsectionPi = linspace(0, 1, 10) 
colorsPi = [cm.cool(x) for x in cm_subsectionPi]

cm_subsectionTau = linspace(0.3, 1, 10) 
colorsTau = [cm.spring(x) for x in cm_subsectionTau]

fig = plt.figure(figsize=(25,25), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotterPi = [[[0],[0]] for _ in range(10)]
directionPi = [0 for _ in range(10)]

plotterTau = [[[0],[0]] for _ in range(10)]
directionTau = [0 for _ in range(10)]


for i in range(100000-1):
    for index in range(len(plotterPi)):
        if int(pi[i]) == index:
            directionPi[index] += 1
        if directionPi[index] % 4 == 0:
            plotterPi[index][0].append(plotterPi[index][0][i]+ 1)
            plotterPi[index][1].append(plotterPi[index][1][i])
        elif directionPi[index] % 4 == 1:
            plotterPi[index][1].append(plotterPi[index][1][i]+ 1)
            plotterPi[index][0].append(plotterPi[index][0][i])
        elif directionPi[index] %4 == 2:
            plotterPi[index][0].append(plotterPi[index][0][i]- 1)
            plotterPi[index][1].append(plotterPi[index][1][i])
        else:
            plotterPi[index][1].append(plotterPi[index][1][i]- 1)
            plotterPi[index][0].append(plotterPi[index][0][i])
    
    for index in range(len(plotterTau)):
        if int(tau[i]) == index:
            directionTau[index] += 1
        if directionTau[index] % 4 == 0:
            plotterTau[index][0].append(plotterTau[index][0][i]+ 1)
            plotterTau[index][1].append(plotterTau[index][1][i])
        elif directionTau[index] % 4 == 1:
            plotterTau[index][1].append(plotterTau[index][1][i]+ 1)
            plotterTau[index][0].append(plotterTau[index][0][i])
        elif directionTau[index] %4 == 2:
            plotterTau[index][0].append(plotterTau[index][0][i]- 1)
            plotterTau[index][1].append(plotterTau[index][1][i])
        else:
            plotterTau[index][1].append(plotterTau[index][1][i]- 1)
            plotterTau[index][0].append(plotterTau[index][0][i])

for index in range(len(plotterTau)):
    plt.plot(plotterTau[index][0], plotterTau[index][1], color = colorsTau[index])

# for index in range(len(plotterPi)):
#     plt.plot(plotterPi[index][0], plotterPi[index][1], color = colorsPi[index])

plt.savefig("spiralAnglesWithTau.png")
plt.show()
