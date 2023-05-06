import SIR_basic_neuron as SIR
import numpy as np
import random
import matplotlib.pyplot as plt

def detect_half_infected(neuron_list):
    count = 0
    for n in neuron_list:
        if n.is_infected():
            count += 1
    if count >= len(neuron_list)/2:
        return True
    return False

number_of_neurons = 1000
p = np.logspace(0.0,1.0,20) # probability of random connection

def set_connections(number_of_neurons, p):

    neuron_list = [SIR.SIR_basic_neuron() for _ in range(number_of_neurons)]


    # Connect to immeditate neighbor
    for i, n in enumerate(neuron_list):
        if i == 0:
            n.connect_neuron(neuron_list[len(neuron_list)-1])
        else:
            n.connect_neuron(neuron_list[i-1])

    #connect to one further
    for i, n in enumerate(neuron_list):
        if i == 0:
            n.connect_neuron(neuron_list[len(neuron_list)-2])
        elif i == 1:
            n.connect_neuron(neuron_list[len(neuron_list)-1])
        else:
            n.connect_neuron(neuron_list[i-2])

    # add random connections
    for i, n in enumerate(neuron_list):
        compare_num = random.random()
        if compare_num < p:
            neuron_to_connect = random.randint(0, number_of_neurons-1)
            n.random_remove_connection()
            neuron_list[neuron_to_connect]
            n.connect_neuron(neuron_list[neuron_to_connect])

    return neuron_list

def count_num_infected(neuron_list):
    count = 0
    for n in neuron_list:
        if n.is_infected():
            count += 1
    return count



half_way_stop_steps = [0 for _ in range(len(p))]
for i, cur_p in enumerate(p):
    neuron_list = set_connections(number_of_neurons, cur_p)
    neuron_list[int(np.ceil(len(neuron_list)/2))].infect_neuron()
    step = 1
    while(not detect_half_infected(neuron_list) and step < 100):
        for n in neuron_list:
            n.take_step(step)
        print(f"Current step is {step}")
        print(f"The number of infected neurons is {count_num_infected(neuron_list)}")
        step += 1
    half_way_stop_steps[i] = step

print(f"p is {p}")
print(f"half way stops is {half_way_stop_steps}")




