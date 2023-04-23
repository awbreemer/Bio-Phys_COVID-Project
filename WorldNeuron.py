import geopandas as gpd
import basic_neuron as bn
import math

class Country:

    pop_per_neuron = 1000000 #the number of people per neuron per country

    def __init__(self, iso_a3, population, adjacent_countries, coun_geometry):
        self.iso_a3 = iso_a3
        self.population = population
        self.adjacent_countries = adjacent_countries
        self.geometry = gpd.GeoDataFrame(geometry=[coun_geometry])
        self.neuron_list = []
        self.color = "white"

        self.assign_neurons()
        self.conect_internal_neurons()

    def __str__(self) -> str:
        return f"Name: {self.iso_a3}, Num Neurons: {len(self.neuron_list)}"
    
    def get_num_neurons(self):
        return len(self.neuron_list)    
    
    def get_geometry(self):
        return self.geometry
    
    def get_neuron_list(self):
        return self.neuron_list
    
    def get_adjacent_countries(self):
        return self.adjacent_countries

    def assign_neurons(self):
        num_neurons = math.ceil(self.population / self.pop_per_neuron)
        self.neuron_list = [bn.neuronV1() for _ in range(num_neurons)]
    
    def conect_internal_neurons(self):
        for n in self.neuron_list:
            for ni in self.neuron_list:
                n.connect_neuron(ni)

    def get_color(self):
        return self.color

    def country_step(self):
        for n in self.neuron_list:
            n.take_step()
        self.color = self.calc_color()

    def calc_infected_percent(self):
        count = 0
        for n in self.neuron_list:
            if n.is_infected():
                count += 1
        return count/len(self.neuron_list)
        

    def calc_color(self):
        percent = self.calc_infected_percent()
        if percent <= .1:
            color = "black"
        elif percent <= .2:
            color = "yellow"
        elif percent <= .5:
            color = "orange"
        else:
            color = "red"
        
        return color

    

    
