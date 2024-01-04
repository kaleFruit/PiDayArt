import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 

f = open("pi.txt", "r")
pi = f.read()

cm_subsection = linspace(0, 1, 10) 
colors = [cm.cool(x) for x in cm_subsection]

fig = plt.figure(figsize=(25,25), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotter = [[[0],[0]] for _ in range(10)]
direction = [0 for _ in range(10)]
for i in range(len(pi[:10000])):
    for index in range(len(plotter)):
        if int(pi[i]) == index:
            direction[index] += 1
        if direction[index] % 4 == 0:
            plotter[index][0].append(plotter[index][0][i]+ 1)
            plotter[index][1].append(plotter[index][1][i])
        elif direction[index] % 4 == 1:
            plotter[index][1].append(plotter[index][1][i]+ 1)
            plotter[index][0].append(plotter[index][0][i])
        elif direction[index] %4 == 2:
            plotter[index][0].append(plotter[index][0][i]- 1)
            plotter[index][1].append(plotter[index][1][i])
        else:
            plotter[index][1].append(plotter[index][1][i]- 1)
            plotter[index][0].append(plotter[index][0][i])

for index in range(len(plotter)):
    plt.plot(plotter[index][0], plotter[index][1], color = colors[index])
plt.savefig("spirallyANGLESANOTHER.png")
plt.show()
