# -*- coding: utf-8 -*-

"""
Created on Mon Jan  6 19:03:41 2025

@author: Hans Petter Helsør, hph@helsor.com, +47 97052966 Github: hphelsor

Programmet regner om fra grader til radianer med ønsket presisjon

"""

import numpy as np
v_grad = float(input('Skriv inn gradtallet: ' ))
desimaler = int(input('Hvor mange desimaler ønsker du i svaret? '))
v_rad = round(v_grad*np.pi/180 , desimaler)
print(f"{v_grad} grader tilsvarer {v_rad} radianer")
