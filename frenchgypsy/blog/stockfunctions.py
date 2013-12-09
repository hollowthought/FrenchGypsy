import urllib
from math import sqrt
import os



def mean(alist):
    mean = sum(alist) / len(alist)
    return mean
def standardDeviation(alist):
    theMean = mean(alist)
    sum = 0 
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        sum = sum + diffsq
    sdev = sqrt(sum/(len(alist)-1))
    return sdev

def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDeviation(xlist)
    ystd = standardDeviation(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd)
    return corr    

def stockCorrelate( ticker1, ticker2):
	url1 = urllib.urlopen('http://ichart.finance.yahoo.com/table.csv?s=%s' %ticker1)
	url2 = urllib.urlopen('http://ichart.finance.yahoo.com/table.csv?s=%s' %ticker2)
	
	t1Data = url1.readlines()
	t1Data = [line.split(',') for line in t1Data[1:]]
	t2Data = url2.readlines()
	t2Data = [line.split(',') for line in t2Data[1:]]
	t1Close= []
	t2Close= []
    
	for i in range(min(len(t1Data), len(t2Data))):
		if t1Data[i][0] == t2Data[i][0]:
			t1Close.append(float(t1Data[i][4]))
			t2Close.append(float(t2Data[i][4]))
	return correlation(t1Close, t2Close)    


