import numpy as np
import basic_neuron as bn
import math
import WorldNeuron as wn
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
for i, country in world.iterrows():
    print(f"The code is {country['iso_a3']} and the name is {country['name']}")

#n3 = bn.neuronV1()


""" nlist = [n1,n3]
if n1 not in nlist:
    print("True")
else:
    print("False") """



""" #n1.connect_neuron(n2)
n1.connect_neuron(n2)
print("n1 connected neurons:")
print(n1.connected_neurons)
print("n2 connected neurons")
print(n2.connected_neurons)
print("n1 mem loc is:")
print(hex(id(n1)))

if n1 in n1.connected_neurons:
    print("Im in") """


""" if n2.connected_neurons[0] is n1:
    print("Connected")
else:
    print(n2.connected_neurons) """


