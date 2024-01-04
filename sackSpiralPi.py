import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import linspace
import math 

f = open("pi.txt", "r")
pi = f.read()

cm_subsection = linspace(0, 1, 10) 
colors = [cm.cool(x) for x in cm_subsection]

fig = plt.figure(figsize=(30,30), facecolor="black")
ax = plt.axes()
ax.set_facecolor("black")

counter = 0
for i in range(len(pi[:50000])):
    if i % 100 == 0:
        print(i)
    for _ in range(int(pi[i])):
        counter += 1
    x = -1*counter**0.5*math.cos(2*math.pi*counter**0.5)
    y = counter**0.5*math.sin(2*math.pi*counter**0.5)
    plt.scatter(x, y, color = colors[int(pi[i])], s = 0.5)
    counter += 1
plt.savefig("6.png")

