#!/usr/bin/env python
"""
**Title: Radiosondenaufstieg**

*Author: Maximilian Meindl*

Description: Short Program to plot a Tephigram which includes a Temperature and humidity line. In second part a geographical map is plotted which shows the ascent point of the radiosonde.
"""

# Import the required packages
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from tephigram_python import Tephigram
from mpl_toolkits.basemap import Basemap

# Initialization of tephigram
tephigram = Tephigram(x_range=(-40,60))

def read_in():
    """
    **Title: Function for reading in the data**
    
    *Description: The file called 'Wien.dat' includes all measurement data which is needed. The following attributes are defined as global and represent the columns of the file.*
    
    :variable P: pressure
    
    :variable T: temperature
    
    :variable T_dp: dew point temperature
    
    :variable RH: relative humidity
    
    :method np.loadtxt: loads the text from the file into the read_in function of the python-program.
    
    :variable sounding: contains the columns of the file loaded before
    """
    sounding = np.loadtxt('Wien.dat', unpack=True)
    global P
    global T
    global T_dp
    global RH
    P = sounding[0]
    T = sounding[2]
    T_dp = sounding[3]
    RH = sounding[4]/100
    
def plot_temp():
    """
    **Title: Function for plotting the temperature line**
    
    *Description: Plotting line of temperature*
    
    :method plot_temp: plots line of temperature depending on pressure and temperature
    """
    tephigram.plot_temp(P=P, T=T)
    
def plot_dewpoint_temp():
    """
    **Title: Function for plotting the humidity line**
    
    *Description: Plotting line of humidity*
    
    :method plot_sounding: plots line of humidity depening on pressure, temperature and dewpoint temperature
    """
    tephigram.plot_sounding(P=P, T=T, T_dp=T_dp)
    
def plot_legend():
    """
    **Title: Function for plotting the legend**
    
    *Description: Plotting legend*
    
    :method plot_legend: plots legend which contoins meteorological parameters
    
    :method savefig: saves the plot as png-File
    """
    tephigram.plot_legend()
    # Saving the Plot as png-File
    tephigram.savefig('tephigram.png')

def plot_card():
    """
    **Title: Function for plotting a geographical map**
    
    *Description: Plotting a geographical map which contains a marker und text*
    
    :variable fig: plots figure with figuresize 12,8
    
    :variable m: creates a Basemap instance
    
    :variable parallels: includes coordinates range and interval
    
    :variable meridians: includes coordinates range and interval
    
    :variable Vienna: include coordinates of city Vienna
    
    :method m.drawparallels: draws paralells
    
    :method m.drawmeridians: draws meridians
    
    :method m.drawcoastlines: draws coastlines
    
    :method m.drawstates: draws states
    
    :method m.drawcountries: draws countries
    
    :method m.drawlsmask: coloring the ocean and the land
    
    :method m.shadedrelief: add relief
    
    :method m.plot: add marker the the card at position of vienna
    
    :method plt.text: add name of city to the marker
    
    :method plt.title: add title above the card plotted before
    
    :method plt.savefig: saving the card as png-file
    
    :method plt.show: shows plot after setting the properties
    """
    fig = plt.figure(figsize=(12,8))
    
    # create a Basemap instance
    m = Basemap(projection='cyl', # try different projection, e.g. 'merc' for mercator
            llcrnrlon = 5.0, llcrnrlat = 45,
            urcrnrlon = 30, urcrnrlat = 62.5,
           resolution='h', area_thresh=10.)

    # set properites...
    parallels = np.arange(-90.,90.,10.0)
    m.drawparallels(parallels,labels=[True,False,False,True],fontsize=10)

    # draw meridians
    meridians = np.arange(-180.0,180.0,10.0)
    m.drawmeridians(meridians,labels=[True,False,False,True],fontsize=10)   
    
    # draw coastlines, states and countries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()
    
    # coloring the oceans and the land
    m.drawlsmask(land_color='lightgreen', ocean_color='aqua', lakes=True)
    # add relief
    m.shadedrelief()

    # draw some data to the map (coordinates)
    Vienna = (16.3720800,  48.2084900)

    # transform coordinates for the projection 
    Vienna=m(Vienna[0], Vienna[1])

    # add marker the the card at position of vienna
    m.plot(Vienna[0], Vienna[1], 'c*', markersize=12, color='black')  # the markers are the same as in the case of normal plot..
   
    # add name of city to the marker
    plt.text(Vienna[0]+0.25, Vienna[1]+0.25, "Vienna",size=18)

    # add title above the card plotted before
    plt.title("09.Juli 2018, 12:00 UTC, Hohe Warte 38 (ZAMG), Vienna")
    
    # saving the card as png-file and show plot
    plt.savefig('basemap.png')
    plt.show()
   
# Execution of the previously defined functions
if __name__ == "__main__":
    read_in()
    plot_temp()
    plot_dewpoint_temp()
    plot_legend()
    plot_card()

