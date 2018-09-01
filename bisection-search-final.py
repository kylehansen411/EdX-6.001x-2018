# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:43:42 2018

@author: kyleh
"""
x = 25
epsilon = 0.001
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 -x) >= epsilon:
    print ('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('NumGuesses = ', numGuesses)
print(ans, 'is close to the square root of', x)


