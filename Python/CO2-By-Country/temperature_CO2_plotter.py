#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

class temperature_co2_plottery(object):
    """
    :param filename:
    """
    def __init__(self, filename):
        self.file = filename   

    """
    :param month: which month to plot temperatures from
    :param tmin: start time (year) range to plot
    :param tmax: end time (year) range to plot
    :returns: tempr - data for month and time range specified by user
    """
    def plot_temperature(self, month, tmin, tmax):
        indicators = pd.read_csv("../INF3331-yast/assigment6/input/"+ self.file +".csv")
        if month == 'January':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='January')&(indicators.Year==x)]
        elif month == 'February':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='February')&(indicators.Year==x)]
        elif month == 'March':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='March')&(indicators.Year==x)]
        elif month == 'April':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='April')&(indicators.Year==x)]
        elif month == 'May':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='May')&(indicators.Year==x)]
        elif month == 'June':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='June')&(indicators.Year==x)]
        elif month == 'July': 
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='July')&(indicators.Year==x)]
        elif month == 'August':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='August')&(indicators.Year==x)]
        elif month == 'September':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='September')&(indicators.Year==x)]
        elif month == 'October':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='October')&(indicators.Year==x)]
        elif month == 'November':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='November')&(indicators.Year==x)]
        elif month == 'December':
            for x in range(tmin, tmax): 
                tempr = indicators[(indicators.Month=='December')&(indicators.Year==x)]
        return tempr
        
    """
    :param ymin: minimum CO2 emission
    :param ymax: maximum CO2 emission
    :param tmax: start time range to plot
    :param tmin: end time range to plot
    :returns: co2 - data for time range (with specified y-axis) specified by user
    """
    def plot_CO2(self, ymin, ymax, tmin, tmax):
        indicators = pd.read_csv("../INF3331-yast/assigment6/input/"+ self.file + ".csv")
        
        for x in range(tmin, tmax): 
            for y in range(ymin, ymax):
                co2 = indicators[(indicators.Year==x)&(indicators.Carbon==y)]
        return co2

      
    """
    :param threshold: threshold for emissions
    :param threshmax: if true, show ony data for countrys with emissions lower than threshold
    :return: co2 - data for threshold specified by user
    """
    def co2emission(self, threshold, threshmax = True):
        indicators = pd.read_csv("../INF3331-yast/assigment6/input/"+ self.file + ".csv")
        if threshmax:
            for x in threshold:
                co2 = indicators[(indicators.Carbon==x)]
        else:
            for x in range(threshold, len(indicators)): 
                    co2 = indicators[(indicators.Country)&(indicators.Carbon==x)]
        return co2

def main():
    tc1 = temperature_co2_plottery("temperature")
    tc2 = temperature_co2_plottery("co2")
    tc3 = temperature_co2_plottery("CO2_by_country")
        
    #temperature - plot, save & show figure
    tempr = tc1.plot_temperature('March', '1950', '1960')
    plt.plot(tempr.Year, tempr.Month, 'mo')   
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Temperature', fontsize=14)
    plt.title('Time vs. Temperatur', fontsize=14)
    fig = plt.figure()
    fig.savefig('temperature.jpeg', format='jpeg', dpi=300)
    plt.show()   
        
    #co2 - plot, save & show figure
    co2ut = tc2.plot_CO2(0, 10, '1900', '1950')
    plt.plot(co2ut.Year, co2ut.Carbon, 'ro')   
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Carbon', fontsize=14)
    plt.title('Time vs. CO2', fontsize=14)
    fig = plt.figure()
    fig.savefig('CO2.jpeg', format='jpeg', dpi=300)
    plt.show()
    
    #co2 by country - plot, save & show figure
    co2country = tc3.co2emission(10,False)
    plt.plot(co2country.Country, co2country.Carbon, 'ro')
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Carbon', fontsize=14)
    plt.title('CO2 by Country', fontsize=14) 
    fig = plt.figure()
    fig.savefig('CO2Country.jpeg', format='jpeg', dpi=300)
    plt.show()       

if __name__ == '__main__': 
    main()