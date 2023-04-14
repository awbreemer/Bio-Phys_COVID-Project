import numpy as np
import random as rand

class neuronV1():

    infectivity_steps = [.2, .5, .7, .6, .4, .3, .2, .1]
    connected_neurons = []

    def __init__(self, infection_step = 0, infectivity = 0, infected = False, recovered = False):
        self.infection_step = infection_step
        self.infectivity = infectivity
        self.infected = infected
        self.recovered = recovered

    def infected_step(self):
        self.infectivity = self.infectivity_steps[self.infection_step+1]
        if self.infection_step >= len(self.infectivity_steps):
            self.infected = False

    def take_step(self):
        if self.infected:
            self.infected_step()

    def is_infected(self):
        return self.infected
    
    def is_recovered(self):
        return self.recovered
    
    def get_infectivity(self):
        return self.infectivity
    
    def gets_infected(self):
        if not self.recovered:
            self.infected = True
            self.infectivity = self.infectivity_steps[0]
            self.infection_step = 1

    def assign_location(self, loc, yLoc = None):
        if yLoc == None:
            self.location = loc
        else:
            self.location = [loc, yLoc]

    def get_location(self):
        return self.location
    
    def get_connected_neurons(self):
        return self.connected_neurons

    def connect_neuron(self, other_neuron):
        if other_neuron not in self.connected_neurons:
            self.connected_neurons.append(other_neuron)
        if self not in other_neuron.get_connected_neurons():
            other_neuron.connected_neurons.append(self)

    def attempt_infect(self):
        for n in self.connected_neurons:
            if rand.random() < self.infectivity:
                if not n.is_recovered():
                    n.gets_infected()

    
