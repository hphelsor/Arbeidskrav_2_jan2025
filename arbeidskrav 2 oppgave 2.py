# -*- coding: utf-8 -*-

"""
Created on Mon Jan  6 19:03:41 2025

@author: Hans Petter Helsør, hph@helsor.com, +47 97052966 Github: hphelsor

Beregner behov for pizza og brus for skolearrangement

"""

antall_elever = int(input('Skriv inn antall elever:' ))

#Beregne antall pizzaer, 4 elever pr pizza
antall_pizzaer = int(antall_elever / 4) #Del antall elever på 4 for å finne behov
if antall_elever % 4 != 0: #Hvis antall elever ikke er et multiplum av 4, legg til en pizza
    antall_pizzaer +=1

#Beregne antall 1,5 liter brus, 2,5 dl pr elev    
antall_brus = int(antall_elever / 6) #Del antall elever på 6 for å finne behov
if antall_elever % 6 != 0: #Hvis antall elever ikke er et multiplum av 6, legg til en brus
    antall_brus +=1
    
if antall_pizzaer == 1: #Entall eller flertall?
    print(f"Det må kjøpes {int(antall_pizzaer)} pizza")
else:
    print(f"Det må kjøpes {int(antall_pizzaer)} pizzaer")
    
if antall_brus == 1: #Entall eller flertall?
    print(f"Det må kjøpes {int(antall_brus)} flaske 1,5 liter brus")
else:
    print(f"Det må kjøpes {int(antall_brus)} flasker 1,5 liter brus")