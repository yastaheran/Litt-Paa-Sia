#!/usr/bin/python
from flask import Flask
from flask import render_template, request
import temperature_CO2_plottery as tcplt
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
    
@app.route("/plot_CO2", methods=["POST"])
def co2():
    ymin = request.form['ymin']
    ymax = request.form['ymax']
    time1 = request.form['time1']
    time2 = request.form['time2']
    
    #plot,save & show figure
    co2ut = tcplt.plot_CO2(ymin, ymax, time1, time2) 
    plt.plot(co2ut.Year, co2ut.Carbon, 'ro')   
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Carbon', fontsize=14)
    plt.title('Time vs. CO2', fontsize=14)
    fig = plt.figure()
    fig.savefig('CO2.jpeg', format='jpeg', dpi=300)
    plt.show()
    
    return render_template("plot_co2.html")
    
@app.route("/temperature", methods=["POST"])
def temperature():

    button = request.form['month'] #this retrieves which radio button was pressed
    time1 = request.form['time1']
    time2 = request.form['time2']
        
    if button == 'Jan':
        tempr = tcplt.plot_temperature('January', time1, time2)
    elif button == 'Feb':
        tempr = tcplt.plot_temperature('Febraury', time1, time2)
    elif button == 'Mar':
        tempr = tcplt.plot_temperature('March', time1, time2)
    elif button == 'Apr':
        tempr = tcplt.plot_temperature('April', time1, time2)
    elif button == 'May':
        tempr = tcplt.plot_temperature('May', time1, time2)
    elif button == 'Jun':
        tempr = tcplt.plot_temperature('June', time1, time2)
    elif button == 'Jul':
        tempr = tcplt.plot_temperature('July', time1, time2)
    elif button == 'Aug':
        tempr = tcplt.plot_temperature('August', time1, time2)
    elif button == 'Sep':
        tempr = tcplt.plot_temperature('September', time1, time2)
    elif button == 'Oct':
        tempr = tcplt.plot_temperature('October', time1, time2)
    elif button == 'Nov':
        tempr = tcplt.plot_temperature('November', time1, time2)
    elif button == 'Dec':
        tempr = tcplt.plot_temperature('December', time1, time2)
    
    #plot,save & show figure    
    plt.plot(tempr.Year, tempr.Month, 'mo')   
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Temperature', fontsize=14)
    plt.title('Time vs. Temperatur', fontsize=14)
    fig = plt.figure()
    fig.savefig('temperature.jpeg', format='jpeg', dpi=300)
    plt.show() 
        
    return render_template("plot_temperature.html")
    

@app.route("/CO2_by_country", methods=["POST"])
def co2_by_country():
    
    threshold = request.form['threshold']
    choice = request.form['choice']
    if choice == 'true':
        co2country = tcplt.co2emission(threshold, True)
    else:
        co2country = tcplt.co2emission(threshold, False)
    
    #plot, save & show  figure
    plt.plot(co2country.Country, co2country.Carbon, 'ro')
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Carbon', fontsize=14)
    plt.title('CO2 by Country', fontsize=14)
    fig = plt.figure()
    fig.savefig('CO2Country.jpeg', format='jpeg', dpi=300)
    plt.show()
    
    return render_template("plot_co2_by_country.html")

@app.route("/help")
def help():
    return render_template("help.html")
    
if __name__ == "__main__":
    app.run(debug=True)
