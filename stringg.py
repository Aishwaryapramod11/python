'''
author: Aishwarya
date: 08-10-2024
python program : strings
version: 1.0
'''
first_name=input("enter your first_name")
last_name=input("enter your last_name")
full_name= first_name+" "+last_name
print(full_name)
length=len(last_name)
extracted_first_name=full_name[:length+1]
print(extracted_first_name)