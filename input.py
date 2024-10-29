'''
author:Aishwarya
date:29-10-24
Python program to find no of vowels and consonents
'''
string_input=input("enter a string:")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
        if char in vowels:
         vowels_count+=1
else:
       consonents=0
       consonents+=1
print(f"The no of vowels in the string_input is:{vowels_count}")
print(f"the no of consonents in the string_input is:{consonents}")