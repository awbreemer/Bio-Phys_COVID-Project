import numpy as np
import random as rand

class neuronV1():

    infectivity_steps = [.05, .1, .2, .4, .15, .1, .05, .01]
    time_to_be_suseptible = 50

    def __init__(self, infection_step = 0, infectivity = 0, infected = False, recovered = False):
        self.infection_step = infection_step
        self.infectivity = infectivity
        self.infected = infected
        self.recovered = recovered
        self.steps_since_infected= 0
        self.connected_neurons = list()

    def __str__(self) -> str:
        return str(self.infectivity)

    def infected_step(self):
        try:
            self.infectivity = self.infectivity_steps[self.infection_step+1]
        except:
            self.infectivity = 0
            self.infected = False
            self.recovered = True
        self.attempt_infect()
        self.infection_step += 1

    def take_step(self):
        
        if self.recovered == True:
            if self.steps_since_infected >= self.time_to_be_suseptible:
                self.recovered = False
                self.steps_since_infected = 0
            else:
                self.steps_since_infected += 1
        if self.is_infected():
            self.infected_step()

    def is_infected(self):
        return self.infected
    
    def get_first_loc_val(self):
        return self.location[0]
    
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
    
    def get_infection_step(self):
        return self.infection_step
    
    def add_neuron_connect_test(self, neuron):
        self.connected_neurons.append(neuron)

    def connect_neuron(self, other_neuron):
        if other_neuron not in self.connected_neurons and other_neuron != self:
            self.connected_neurons.append(other_neuron)
            other_neuron.connected_neurons.append(self)

    def attempt_infect(self):
        for n in self.connected_neurons:
            if rand.random() < self.infectivity:
                n.gets_infected()

    
