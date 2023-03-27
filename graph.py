import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime
from matplotlib import style
from mpl_toolkits.axes_grid1 import Divider,Size

import csv
import time
import subprocess
import PySimpleGUI as sg

fig = plt.figure()

rect = fig.patch
rect.set_facecolor('#0079E7')

def animate(i):
    graph_data = open('example.csv', 'r').read()
    print(graph_data)
    lines = graph_data.split('\n')
    xs = []
    ys = []
    timeC = list()
    for line in lines:
        if len(line) > 1:
            pieces = line.split(',')
            ph = pieces[0]
            
                
                    
            timeB = pieces[1]
            timeA = timeB[:8]
            time_string = datetime.strptime(timeA, "%H:%M:%S")
            
            
            

            xs.append(float(ph))
            timeC.append(time_string)
            
            
            ax1 = fig.add_subplot(1,1,1)
            ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
            ax1.clear()
            ax1.plot(timeC, xs, 'c', linewidth=3.3)
            plt.title('PH Value')
            plt.xlabel('Time')
    
ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
