#!/usr/bin/env/python

import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help='input file // FORMAT --> .pdb')
parser.add_argument("-o", "--output", required=True, help='output file // FORMAT --> .txt')
args = parser.parse_args()

file = open(str(args.input),'r')

list_file = list(file)

remove_list=[]
tingyun=[]

for i in np.arange(0,len(list_file)):
    if list_file[i].startswith('HEADER'):
        remove_list.append(list_file[i])
    if list_file[i].startswith('REMARK'):
        remove_list.append(list_file[i])
    if list_file[i].startswith('TER'):
        remove_list.append(list_file[i])
    if list_file[i].startswith('END'):
        remove_list.append(list_file[i])

        
for j in np.arange(0,len(remove_list)):
    list_file.remove(remove_list[j])
    
for i in np.arange(0,len(list_file)):
    tingyun.append(list_file[i].split()[6:9])
    
tingyun2 = np.transpose(tingyun)

x_values = []
y_values = []
z_values = []

for k in tingyun2[0]:
     x_values.append(float(k))

for k in tingyun2[1]:
     y_values.append(float(k))

for k in tingyun2[2]:
     z_values.append(float(k))

x_max = max(x_values)
y_max = max(y_values)
z_max = max(z_values)

x_min = min(x_values)
y_min = min(y_values)
z_min = min(z_values)

x_coord = (x_max - x_min)
y_coord = (y_max - y_min)
z_coord = (z_max - z_min)

coordinates = [round(x_coord,3),round(y_coord,3),round(z_coord,3)]

print(coordinates)
print(x_max,y_max,z_max,x_min,y_min,z_min)

f = open(str(args.output),"w+")
f.write(str(coordinates))
f.close
