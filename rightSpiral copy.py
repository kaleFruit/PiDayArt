import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 

f = open("pi.txt", "r")
pi = f.read()
digits = 10000
cm_subsection = linspace(0, 1, digits) 
colors = [cm.cool(x) for x in cm_subsection]

fig = plt.figure(figsize=(25,25), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
plotter = [[0],[0]]
direction = [0]
for i in range(len(pi[:digits])):
    if int(pi[i]) != 0:
        direction.append(direction[i]+math.pi/(2*int(pi[i])))
    else:
        direction.append(direction[i])
    plotter[0].append(plotter[0][i]+math.cos(direction[i+1]))
    plotter[1].append(plotter[1][i]+math.sin(direction[i+1]))

# for i in range(digits):
#     plt.scatter(plotter[0][i], plotter[1][i], color = colors[i])
plt.plot(plotter[0], plotter[1], color="white")
plt.savefig("fkajsdlfakksdlf.png")
plt.show()
