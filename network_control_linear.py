import basic_neuron as bn
import numpy as np
import matplotlib.pyplot as plt

list_len = 10

neuron_list = [bn.neuronV1() for _ in range(list_len)]

raster_record = np.empty((1,list_len))

for n in range(1, len(neuron_list)):
    neuron_list[n].assign_location(1,n)
    neuron_list[n].connect_neuron(neuron_list[n-1])

neuron_list[0].assign_location(1,0)

neuron_list[5].gets_infected()



for time in range(500):
    cur_neur_status = np.zeros(list_len)
    for i, n in enumerate(neuron_list):
        n.take_step()
        cur_neur_status[i] = n.get_infectivity()
    raster_record = np.vstack((raster_record,cur_neur_status))



plt.contourf(raster_record)
plt.colorbar()
plt.show()
          

