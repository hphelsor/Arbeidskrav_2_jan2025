# -*- coding: utf-8 -*-

"""
Created on Mon Jan  6 19:03:41 2025

@author: Hans Petter Helsør, hph@helsor.com, +47 97052966 Github: hphelsor

Beregner y=-x^n-a og plotter grafen mellom 2 verdier av x

"""

import matplotlib.pyplot as plt
import numpy as np

print("--------------------------------------------------------------")
print("|||||    Programmet plotter funksjonen y =  -x**n - a    |||||")
print("--------------------------------------------------------------\n")

while True: #Ber om verdier for funksjonen
    power = int(input("Hva er potensverdien n? "))
    constant = int(input("Hva er konstantverdien a? "))
    lower = int(input("Hva er minste verdi for x? "))
    upper = int(input("Hva er største verdi for x? "))
    
    if lower < 0: #Skalering av plotområdet
        points = (upper+abs(lower))*10
    else:
        points = (upper-lower)*10
    x = np.linspace(lower, upper, points)
    y = - x**power - constant #Beregner y for x
    
    #Plotter grafen
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.axhline(0, color='black', linewidth=.5) #Plotter y=0 som referanse
    plt.show()
    input("Trykk enter for ny beregning. Ctrl+C for å avslutte.")