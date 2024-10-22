'''
author:Aishwarya
date:22-10-24
Python program convert temperature values back and forth between Celsius and Fahrenheit.
'''
temperature=int(input("enter the temperature"))
unit=input("is this (C)elsius or (F)arenheit?")
if unit=="C":
    f= (9/5*temperature)+32
    print(temperature,"(C)elsius is",f,"(F)arenheit.")
else:
      c = 5/9* (temperature-32)
      print(temperature,"(F)arenheit is",c,"(C)elsius")