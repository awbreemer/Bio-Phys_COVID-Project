import basic_neuron as bn
import random

class SIR_basic_neuron():
    
    def __init__(self, infected = False, recovered = False, blocked = False):
        self.infected = infected
        self.recovered = recovered
        self.connected_neurons = list()
        self.infection_time_step = 0
        self.blocked = blocked
        

    def is_recovered(self):
        if self.recovered == True:
            return True
        return False
    
    def is_infected(self):
        if self.infected == True:
            return True
        return False
    
    def block_neuron(self):
        self.blocked = True

    def unblock_neuron(self):
        self.blocked = False

    def is_blocked(self):
        return self.blocked
    
    def infect_neuron(self, time_step = None):
        if self.recovered == False and self.infected == False:
            self.infected = True
            self.blocked = True
            if time_step != None:
                self.infection_time_step = time_step

    def recover_neuron(self, time_step = None):
        if self.recovered == False:
            self.recovered = True
            if time_step != None:
                self.recovered_time_step = time_step

    def take_step(self, step):
        if self.infected and self.infection_time_step != step:
            for n in self.connected_neurons:
                if not n.is_infected() and not n.is_recovered() and not n.is_blocked():
                    n.infect_neuron(step)

    def connect_neuron(self, other_neuron):
        if other_neuron not in self.connected_neurons and other_neuron != self:
            self.connected_neurons.append(other_neuron)
            other_neuron.connected_neurons.append(self)

    def random_remove_connection(self):
        remove_neuron = random.randint(0,len(self.connected_neurons)-1)
        other_neruon = self.connected_neurons.pop(remove_neuron)
        other_neruon.connected_neurons.remove(self)




