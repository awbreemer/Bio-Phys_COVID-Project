## This model will feature an matrix of neurons, that will be connected to their neighbors on each side.
import numpy as np
import basic_neuron as bn
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import random

side_length = 100 # the number of neurons on each side of the matrix
time_steps = 200
neuron_matrix = [[bn.neuronV1() for _ in range(side_length)] for _ in range(side_length)]
inf_x, inf_y = 50,50


#set up connections
for x in range(side_length):
    for y in range(side_length):
        if x != 0:
            neuron_matrix[x][y].connect_neuron(neuron_matrix[x-1][y])
        if x != side_length - 1:
            neuron_matrix[x][y].connect_neuron(neuron_matrix[x+1][y])
        if y != 0:
            neuron_matrix[x][y].connect_neuron(neuron_matrix[x][y-1])
        if y != side_length - 1:
            neuron_matrix[x][y].connect_neuron(neuron_matrix[x][y+1])

fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    ax.contourf(data_stack[i], cmap = 'plasma')

def add_random_connect(p, neur_matrix):
    for x in range(side_length):
        for y in range(side_length):
            if random.random() < p:
                neur_matrix[x][y].connect_neuron(neur_matrix[random.randint(0,side_length-1)][random.randint(0,side_length-1)])

add_random_connect(.1, neuron_matrix)

neuron_matrix[inf_x][inf_y].gets_infected()

data_stack = [[[0.0 for _ in range(side_length)] for _ in range(side_length)]]

for t in range(time_steps):
    cur_level_infectiousness = [[0.0 for _ in range(side_length)] for _ in range(side_length)]
    for x in range(side_length):
        for y in range(side_length):
            neuron_matrix[x][y].take_step()
            cur_level_infectiousness[x][y] =  neuron_matrix[x][y].get_infectivity()
    data_stack.append(cur_level_infectiousness)

ani = animation.FuncAnimation(fig, animate, time_steps, interval = 50, blit = False)
plt.show()

ani.save("./InitialAnimation1.gif", writer='imagemagick', fps=60)
print(os.getcwd())