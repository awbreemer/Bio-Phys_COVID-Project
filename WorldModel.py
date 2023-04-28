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
selected_country = 'CHN'


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
country_matrix = []
for i in range(steps):
    time_step_colors = []
    for country in list(country_list.values()):
        country.country_step()
        time_step_colors.append(country.get_color())
        if country.get_iso_a3() == selected_country:
            country_matrix.append(country.get_infection_matrix())
    color_list.append(time_step_colors)

fig, ax = plt.subplots(2)

print(len(country_matrix))

def animate(step):
    ax[0].clear()
    ax[1].clear()
    for i, country in enumerate(list(country_list.values())):
        country.get_geometry().plot(ax = ax[0], color = color_list[step][i])
    print(f"The step of the animation is {step}.")
    ax[1].contourf(country_matrix[step], cmap = 'plasma')


ani = animation.FuncAnimation(fig, animate, frames = range(steps), interval = 5, blit = False)
#plt.show()
ani.save("./InitialAnimation1.gif", writer='imagemagick', fps=5)




