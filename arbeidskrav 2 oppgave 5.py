# -*- coding: utf-8 -*-

"""
Created on Mon Jan  6 19:03:41 2025

@author: Hans Petter Helsør, hph@helsor.com, +47 97052966 Github: hphelsor

Beregner areal og omkrets av en figur som består av en halvsirkel og en rettvinklet trekant

"""

import numpy as np

def tegning(): #Tegner skisse av figuren
    print("\n\n                 ..")
    print("              .      .")
    print("             .        .")
    print("            .     a    .")
    print("           ..............")
    print("           .__|        .")
    print("           .          .")
    print("           .         .")
    print("           .        .")
    print("           .       .")
    print("         b .      .")
    print("           .     .")
    print("           .    .")
    print("           .   .")
    print("           .  .")
    print("           . .")
    print("           . \n")
    
def linje(): #Tegner skillelinje
    print("----------------------------------------------------------------------")

def sjekk_tall(variabel): #Sjekker verdiene som blir lagt inn
    if variabel.isnumeric() == False:
        global variabelfeil
        variabelfeil = True
    return

variabelfeil = False
desimaler = int(input("Hvor mange desimaler ønsker du å regne med? "))

while True:
    tegning() #Tegner skisse   
    variabelfeil = False #Initierer flagg for feil i input data
    diameter = input("Hva er sirkelens diameter? (a) ")
    lengde_b = input("Hva er trekantens side? (b) ")
    sjekk_tall(diameter) 
    sjekk_tall(lengde_b)
    if variabelfeil == False: #Kjører hovedprogrammet hvis variablene er OK
        diameter = float(diameter)
        radius = diameter/2
        lengde_b = float(lengde_b)
        areal_halvsirkel = np.pi * radius**2 / 2
        areal_trekant = radius * lengde_b
        areal = areal_halvsirkel + areal_trekant
        print(f"\nArealet av halvsirkelen er {round(areal_halvsirkel, desimaler)}")
        print(f"Arealet av trekanten er {round(areal_trekant, desimaler)}")
        linje()
        print(f"Samlet areal er {round(areal, desimaler)}\n")
        omkrets_halvsirkel = np.pi*diameter
        lengde_ukjent = np.sqrt(lengde_b**2 + diameter**2)
        omkrets = omkrets_halvsirkel + lengde_b + lengde_ukjent
        print(f"Lengden av halvsirkelen er {round(omkrets_halvsirkel, desimaler)}")
        print(f"Lengden av siden b i trekanten er {round(lengde_b, desimaler)}")
        print(f"Lengden av den ukjente siden (motstående b) i trekanten er {round(lengde_ukjent, desimaler)}")
        linje()
        print(f"Samlet omkrets er {round(omkrets, desimaler)}\n\n")
    else: #Ber om nye verdier dersom de ikke er numeriske
        print("\nVennligst legg inn tallverdier for a og b\n")
    input("Trykk enter for ny beregning. Ctrl+C for å avslutte.")
        
        
        
    
