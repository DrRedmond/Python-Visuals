# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:29:22 2022

@author: Redmond O'Hanlon'
"""

#import matplot library to create bar chart 
import matplotlib.pyplot as plot

#Renamed Source File to KJV Version of Bible.
#Must be in same directory as Python file
source = 'Bible.txt'

#establish characters to be counted. We are only interested in letters of the alphabet and not any special characters or numbers

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#Create dictionary of letter counts for each character of 'letters'
lcount = dict([(l, 0) for l in letters])

# Read in the text and count the letter occurences
for l in open(source).read():
    try:
        lcount[l.upper()] += 1
    except KeyError:
        
# Ignore characters that are not letters
        pass
     
# The total number of letters
norm = sum(lcount.values())

fig = plot.figure(frameon=True,tight_layout=True,facecolor='#a158cd',figsize=[10, 5.5])

ax = fig.add_subplot(1,1,1)

#Create Bar chart to display how many times each letter was present in the text document

#Set xaxis range to 26 as there is 26 unique characters to be counted
xaxis = range(26)

#Set width, color , and alignment of bar chart
ax.bar(xaxis, [lcount[l] for l in letters], width=0.85,
       color='b', align='center')
ax.set_xticks(xaxis)

#Set X Axis to be the alphabetic characters we defined above as 'letters'
ax.set_xticklabels(letters)

#Set ticks to show below each individual bar
ax.tick_params(axis='x', direction='out')

#Align X Axis to plot
ax.set_xlim(-1, 26)

#Enable Gridlines for Y Axis 
ax.yaxis.grid(True)

#Create Labels for Bar Chart 
ax.set_title('Count Of Letters in Resume')
ax.set_ylabel('Number of Occurances',labelpad=10.0)
ax.set_xlabel('Letters of the Alphabet',labelpad=10.0)
plot.show()
