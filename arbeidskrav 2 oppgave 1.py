# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Hans Petter Helsør, hph@helsor.com, +47 97052966 Github: hphelsor

Beregner alder og andre ting ut fra fødselsår

"""

year_of_birth = int(input("Hvilket år ble du født? "))
age = int(2024 - year_of_birth)
print(f"Da fylte du {age} år i 2024")
if age < 67: #Beregner om man er eller blir pensjonist
    print(f"Du blir pensjonist i {year_of_birth + 67}.")
else:
    print(f"Du ble pensjonist i {year_of_birth + 67}.")
print(f"Det er {age - 18} år siden du ble myndig.")
print(f"I år 2000 var du {2000 - year_of_birth} år gammel.\n")
print(f"Det betyr at du har levd mer enn {age*365} dager.")