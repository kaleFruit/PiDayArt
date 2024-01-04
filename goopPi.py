import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math

f = open("pi.txt", "r")
pi = f.read()
pi.splitlines()
print(len(pi))
cm_subsection = linspace(0, 1, 10)
colors = [cm.cool(x) for x in cm_subsection]
fig = plt.figure(figsize=(15, 15), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotter = [[[0], [0]] for _ in range(10)]
direction = [[0] for _ in range(10)]
actuallyPlot = [[] for _ in range(10)]
for i in range(len(pi[:])):
    for index in range(10):
        if index != 0:
            if int(pi[i]) == index:
                direction[index].append(
                    direction[index][i] + math.pi / (2 * int(pi[i]))
                )
                actuallyPlot[index].append(1)
            else:
                direction[index].append(direction[index][i])
                actuallyPlot[index].append(0)
            plotter[index][0].append(
                plotter[index][0][i] + math.cos(direction[index][i + 1])
            )
            plotter[index][1].append(
                plotter[index][1][i] + math.sin(direction[index][i + 1])
            )

for line in range(len(plotter)):
    xCoors = [
        plotter[line][0][index]
        for index in range(len(actuallyPlot[line]))
        if actuallyPlot[line][index] == 1
    ]
    yCoors = [
        plotter[line][1][index]
        for index in range(len(actuallyPlot[line]))
        if actuallyPlot[line][index] == 1
    ]
    plt.scatter(xCoors, yCoors, color=colors[line], s=0.1)
plt.xticks([], [])
plt.yticks([], [])
plt.tight_layout()
plt.savefig("colorfulGoopWithEEE.png")
plt.show()
