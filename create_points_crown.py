#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:21:55 2021

@author: fabio semeraro
"""


##################################################
#                                                #
#                   OPZIONI                      #
#                                                #
##################################################
                                                 #
# Nome del nuovo file da creare                  #
fileName = 'boxcpsBsplines0'                     #
                                                 #
# Coordinate vertice inferiore                   #
min_points = [0, 0, 0]                           #
                                                 #
# Coordinate vertice superiore                   #
max_points = [1, 1, 1]                           #
                                                 #
# Numero di layer nelle 3 direzioni              #
layers = [3, 3, 3]                               #
                                                 #
##################################################

# -------------------------------------------------------------- #
##################################################
#       NON MODIFICARE NULLA DA QUI IN POI       #
##################################################
# ---------------------------------------------------------------#

import numpy as np

my_list = []

with open('boxcpsBsplines0_default','r') as f:
    for item in f:
        my_list.append(item[:-1])

i = 0

while i < len(my_list):
    a = my_list[i].find('( (')
    if a >= 0:
        break
    else:
        i += 1

header = my_list[:i]
footer = my_list[i+1:]    


#DEFINE POINTS

points = np.genfromtxt('punti.csv',delimiter=',')

points_x = points.T[0]
points_y = points.T[1]
points_z = points.T[2] 


npoints = len(points_x)

points_str = ''
points_num = []
          
for i in range(0,len(points_x)):
    points_str = points_str + ' ( ' + str(points_x[i]) + ' ' + str(points_y[i]) + ' ' + str(points_z[i]) + ' )' 
    points_num.append([points_x[i], points_y[i], points_z[i]])


                                                                                            
with open(fileName,'w') as f:
    for i in range(0,len(header)):
        f.write(header[i] + '\n')
    
    f.write('controlPoints  ' + str(npoints) + ' (' )
    f.write(points_str)
    f.write(' );\n')
    
    for i in range(0,len(footer)):
        f.write(footer[i] + '\n')

f.close()


with open(fileName + '.obj','w') as g:
    g.write('# ' + fileName)
    for i in range(0,len(points_num)):
        g.write('\nv ' + str(points_num[i][0]) + ' ' + str(points_num[i][1]) + ' ' + str(points_num[i][2]))
    
