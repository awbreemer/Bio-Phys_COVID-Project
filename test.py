import numpy as np
import basic_neuron as bn

n1 = bn.neuronV1()
n2 = bn.neuronV1()
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

a = np.array([[1,2],[3,4]])
b = np.empty((2,2))
print(a)
print(b)
c = np.array([a,b])
print(c)
