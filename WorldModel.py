import geopandas as gpd
import basic_neuron as bn
from shapely.geometry import MultiPolygon
import matplotlib.pyplot as plt
import WorldNeuron as wn
import random
import matplotlib.animation as animation

p_traveling_across_boarder = .1 #the probability of a neuron having a connection to a neigboring country
p_traveling_other_international = .02 #the probability of a neuron having a connection to any country
steps = 200



world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


country_list = {}



for i, row in world.iterrows():
    neighbors = world[world.geometry.touches(row['geometry'])]['iso_a3'].tolist()
    country_list[row['iso_a3']] = wn.Country(row['iso_a3'], row['pop_est'], neighbors, row['geometry'])

connection_options = list(country_list.values())


# connect neurons to other boardering countries
for country in country_list.values():
    neurons_to_connect_boarder = []
    neurons_to_connect_international = []

    for n in country.get_neuron_list():

        rand_num = random.random()
        if  rand_num < p_traveling_other_international:
            neurons_to_connect_international.append(n)
        elif rand_num < p_traveling_across_boarder:
            neurons_to_connect_boarder.append(n)
    
    for n in neurons_to_connect_boarder:
        connectedCountries = country.get_adjacent_countries()
        try:
            select_country = random.choice(connectedCountries)
            select_connection_point = random.choice(select_country.get_neuron_list())
            n.connect_neuron(select_connection_point)
        except:
            pass


    for n in neurons_to_connect_international:
        select_country = random.choice(connection_options)
        select_connection_point = random.choice(select_country.get_neuron_list())
        n.connect_neuron(select_connection_point)




starting_counrty_list = country_list['CHN'].get_neuron_list()
starting_counrty_list[0].gets_infected()

color_list = []

for i in range(steps):
    time_step_colors = []
    for country in list(country_list.values()):
        country.country_step()
        time_step_colors.append(country.get_color())
    color_list.append(time_step_colors)

fig, ax = plt.subplots()

def animate(step):
    ax.clear()
    for i, country in enumerate(list(country_list.values())):
        country.get_geometry().plot(ax = ax, color = color_list[step][i])

ani = animation.FuncAnimation(fig, animate, frames = range(steps), interval = 10, blit = False)
plt.show()





