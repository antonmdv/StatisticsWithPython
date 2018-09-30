#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:45:49 2017

@author: antonmdv
"""

########################################################################   
#Imports
import numpy as np
import math
import scipy
import matplotlib

########################################################################   
#Test DataSet
#listTest1 = [3, 7, 8, 5, 12, 14, 21, 13]
#listTest2 = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]

#8.1
list81a = [56,47,49,37,38,60,50,43,43,59,50,56,54,58]
list81b = [53,21,32,49,45,38,44,33,32,43,53,46,36,48,39,35,37,36,39,45]

#8.2
list82 = [17.2, 22.1, 18.5, 17.2, 18.6, 14.8, 21.7, 15.8, 16.3, 22.8,
          24.1, 13.3, 16.2, 17.5, 19.0, 23.9, 14.8, 22.2, 21.7, 20.7,
          13.5, 15.8, 13.1, 16.1, 21.9, 23.9, 19.3, 12.0, 19.9, 19.4,
          15.4, 16.7, 19.5, 16.2, 16.9, 17.1, 20.2, 13.4, 19.8, 17.7,
          19.7, 18.7, 17.6, 15.9, 15.2, 17.1, 15.0, 18.8, 21.6, 11.9]
          
#8.5
list85Year = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900,
              1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,]
list85Population = [3.9, 5.3, 7.2, 9.6, 12.9, 17.1, 23.2, 31.4, 38.6, 50.2, 63.0, 76.2,
                    92.2, 106.0, 123.2, 132.2, 151.3, 179.3, 203.3, 226.5, 248.7, 281.4, 308.7]
                    
#8.8
list88One = [ 19, 24, 12, 19, 18, 24, 8, 5, 9, 20, 13, 11, 1, 12, 11, 10, 22, 21, 7, 16, 15, 15, 26, 16, 1,
13, 21, 21, 20, 19]
list88Two = [17, 24, 21, 22, 26, 22, 19, 21, 23, 11, 19, 14, 23, 25, 26, 15, 17, 26, 21, 18, 19, 21, 24,
18, 16, 20, 21, 20, 23, 33]
list88Three = [56, 52, 13, 34, 33, 18, 44, 41, 48, 75, 24, 19, 35, 27, 46, 62, 71, 24, 66, 94, 40, 18, 15,
39, 53, 23, 41, 78, 15, 35]

########################################################################   
#Five-point summary function
def Mean(alist):
    mean  = sum(alist)/len(alist)
    return mean
    
def Minimum(alist):
    minSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] < minSoFar:
            minSoFar = alist[pos]
    return minSoFar
    
def Maximum(alist):
    maxSoFar = alist[0]
    for pos in range(1,len(alist)):
        if alist[pos] > maxSoFar:
            maxSoFar = alist[pos]
    return maxSoFar
    
def Median(alist):
    copylist = alist[:]
    copylist.sort()
    if len(copylist)%2 == 0:
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def Quartile(alist):
    
    copylist = alist[:]
    copylist.sort()
    
    if len(copylist)%2 == 0:
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        lowerHalf = copylist[0:leftmid+1]
        uppedHalf = copylist[rightmid:]

        if len(lowerHalf)%2 == 0:
            rightmid = len(lowerHalf)//2
            leftmid = rightmid - 1
            firstQuart = (lowerHalf[rightmid]+lowerHalf[leftmid])/2
            thirdQuart = (uppedHalf[rightmid]+uppedHalf[leftmid])/2
        else:
            mid = (len(lowerHalf)//2)
            firstQuart = lowerHalf[mid]
            thirdQuart = uppedHalf[mid]
    else:
        mid = len(copylist)//2
        lowerHalf = copylist[0:mid]
        upperHalf = copylist[mid+1:]
        
        if len(lowerHalf)%2 == 0:
            rightmid = len(lowerHalf)//2
            leftmid = rightmid - 1
            firstQuart = (lowerHalf[leftmid]+lowerHalf[rightmid])/2
            thirdQuart = (upperHalf[rightmid]+upperHalf[leftmid])/2
        else:
            mid = (len(lowerHalf)//2)+1
            firstQuart = lowerHalf[mid]
            thirdQuart = upperHalf[mid]
    
    quart = [firstQuart,thirdQuart]
    return quart

def standardDeviation(alist):
    theMean = Mean(alist)
    total = 0
    
    for item in alist:
        difference = item-theMean
        diffsq = difference ** 2
        total = total + diffsq
    if total == 0:
        sdev = 0
    else:
        sdev = math.sqrt(total/len(alist)-1)
    return sdev
    
def FivePointSummary(alist):
    copylist = alist[:]
    minim = Minimum(copylist)
    maxim = Maximum(copylist)
    med = Median(copylist)
    stdDev = standardDeviation(copylist)
    mean = Mean(copylist)
    quart = Quartile(copylist)
    firstQuart = quart[0]
    thirdQuart = quart[1]
    
    print("")
    print("Mean:")
    print(mean)
    print("")
    print("STDev:")
    print(stdDev)
    print("")
    print("Minimum:")
    print(minim)
    print("")
    print("Q1:")
    print(firstQuart)
    print("")
    print("Median:")
    print(med)
    print("")
    print("Q3")
    print(thirdQuart)
    print("")
    print("Max")
    print(maxim)
    print("")
    
    summary = [mean,stdDev,minim,firstQuart,med,thirdQuart,maxim]
    return summary
    
########################################################################   
#Main    
#print("")    
#print("8.1") 
#print("")

#print("5-Point-Summary for 'before' data")  
#fivePointDataBefore = FivePointSummary(list81a)

#print("5-Point-Summary for 'after' data")
#fivePointDataAfter =  FivePointSummary(list81b)

#print("")    
#print("Box Plot for 'before' data")
#matplotlib.pyplot.boxplot(list81a)

#print("")
#print("Box Plot for 'after' data")
#matplotlib.pyplot.boxplot(list81b)
 
########################################################################   
#print("")    
#print("8.2") 
#print("")

#fivePointData = FivePointSummary(list82)
#matplotlib.pyplot.boxplot(list82)

#print("D:")
#IQR = fivePointData[5]-fivePointData[3]
#print("IQR ->")
#print(IQR)

#print("E:")
#matplotlib.pyplot.hist(list82)

########################################################################   
#print("")    
#print("8.5") 
#print("")
#matplotlib.pyplot.errorbar(list85Year,list85Population)

########################################################################   
print("")    
print("8.8") 
print("")

#matplotlib.pyplot.hist(list88One)
#matplotlib.pyplot.hist(list88Two)
#matplotlib.pyplot.hist(list88Three)

meanOne = Mean(list88One)
meanTwo = Mean(list88Two)
meanThree = Mean(list88Three)

medianOne = Median(list88One)
medianTwo = Median(list88Two)
medianThree = Median(list88Three)

print("Mean List One:")
print(meanOne)
print("Mean List Two:")
print(meanTwo)
print("Mean List Three:")
print(meanThree)

print("")
print("Median List One:")
print(medianOne)
print("Median List Two:")
print(medianTwo)
print("Median List Three:")
print(medianThree)
        