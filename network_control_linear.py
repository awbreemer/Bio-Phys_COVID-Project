import basic_neuron as bn
import numpy as np
import matplotlib.pyplot as plt

list_len = 100

neuron_list = [bn.neuronV1() for _ in range(list_len)]

raster_record = np.zeros(len(neuron_list))

for n in range(1, len(neuron_list)):
    neuron_list[n].connect_neuron(neuron_list[n-1])

neuron_list[50].gets_infected()

for time in range(500):
    for n in range(len(neuron_list)):
        neuron_list[n].take_step()
        if neuron_list[n].is_infected() and raster_record[n] == 0:
            raster_record[n] = time
    for n in neuron_list:
        n.attempt_infect()
    if time in range(0,10):
        print(raster_record)
raster = plt.plot(range(len(raster_record)), raster_record)


