#this is decoder  for my javascript files.
from __future__ import print_function
import os
import os.path
data=[]
os.system("dir>Desktop/downloads/googlemaps_data.txt")
text=open("C:/Users/root/Desktop/downloads/googlemaps_data.txt","w")
text.close()
f=list(open('C:/Users/root/Desktop/downloads/googlemaps.txt'))
ff=f[0].split('@')
fff=ff[1].split(',')
data.append(fff[0])
data.append(' ')
data.append(fff[1])
data.append('\n')
os.remove('C:/Users/root/Desktop/downloads/googlemaps.txt')
k=int(input("please insert the last number of the saved file "))
for i in range(1,k+1):
    string="googlemaps"+" "+"("+str(i)+")"+".txt"
    f=list(open('C:/Users/root/Desktop/downloads/'+string))
    ff=f[0].split('@')
    fff=ff[1].split(',')
    data.append(fff[0])
    data.append(' ')
    data.append(fff[1])
    data.append('\n')
    os.remove('C:/Users/root/Desktop/downloads/'+string)
text=open("C:/Users/root/Desktop/downloads/googlemaps_data.txt","w")
for a in data:
    text.write(a)
text.close()
