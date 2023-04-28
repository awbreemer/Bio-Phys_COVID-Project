import geopandas as gpd
import basic_neuron as bn
import math
import numpy as np

class Country:

    pop_per_neuron = 1000000 #the number of people per neuron per country

    def __init__(self, iso_a3, population, adjacent_countries, coun_geometry):
        self.iso_a3 = iso_a3
        self.population = population
        self.adjacent_countries = adjacent_countries
        self.geometry = gpd.GeoDataFrame(geometry=[coun_geometry])
        self.neuron_list = []
        self.color = "white"

        #self.assign_neurons()
        self.create_neuron_matrix()
    

    def __str__(self) -> str:
        return f"Name: {self.iso_a3}, Num Neurons: {len(self.neuron_list)}"
    
    def get_num_neurons(self):
        return len(self.neuron_list)    
    
    def get_geometry(self):
        return self.geometry
    
    def get_iso_a3(self):
        return self.iso_a3
    
    def get_infection_matrix(self):
        infectivity_matrix = [[0.0 for _ in range(self.side_length)] for _ in range(self.side_length)]
        for x in range(self.side_length):
            for y in range(self.side_length):
                infectivity_matrix[x][y] = self.neuron_matrix[x][y].get_infectivity()
        return infectivity_matrix
    
    def get_neuron_list(self):
        return self.neuron_list
    
    def get_adjacent_countries(self):
        return self.adjacent_countries

    def assign_neurons(self):
        num_neurons = math.ceil(self.population / self.pop_per_neuron)
        self.neuron_list = [bn.neuronV1() for _ in range(num_neurons)]

    def create_neuron_matrix(self):
        #model each country as a square 2d matrix with 4 connections per neuron:
        #area of the matrix will be close to the population of the country / 1m
        frac_population = np.sqrt(self.population / self.pop_per_neuron) 
        self.side_length = int(np.ceil(frac_population))
        #print(f"The type of object that self.side_length is {type(self.side_length)}")
        self.neuron_matrix = [[bn.neuronV1() for _ in range(self.side_length)] for _ in range(self.side_length)]
        self.connect_internal_neurons_matrix()
        self.create_neuron_list()
    
    def conect_internal_neurons(self):
        for n in self.neuron_list:
            for ni in self.neuron_list:
                n.connect_neuron(ni)

    def connect_internal_neurons_matrix(self):
        for x in range(self.side_length):
            for y in range(self.side_length):
                if x != 0:
                    self.neuron_matrix[x][y].connect_neuron(self.neuron_matrix[x-1][y])
                if x != self.side_length - 1:
                    self.neuron_matrix[x][y].connect_neuron(self.neuron_matrix[x+1][y])
                if y != 0:
                    self.neuron_matrix[x][y].connect_neuron(self.neuron_matrix[x][y-1])
                if y != self.side_length - 1:
                    self.neuron_matrix[x][y].connect_neuron(self.neuron_matrix[x][y+1])

    def create_neuron_list(self):
        for x in range(self.side_length):
             for y in range(self.side_length):
                 self.neuron_list.append(self.neuron_matrix[x][y])  
    
    def get_neuron_matrix(self):
        return self.neuron_matrix

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
        if percent <= .01:
            color = "green"
        elif percent <= .02:
            color = "yellow"
        elif percent <= .05:
            color = "orange"
        elif percent <= .1:
            color = "red"
        else:
            color = "black"
        
        return color

    

    
