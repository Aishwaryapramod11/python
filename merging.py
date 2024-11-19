'''
author: Aishwarya
date: 19-11-2024
'''
list1=[]
list2=[]
list1_size=int(input("enter the size of list1"))
print("enter the elements of list1:")
for i in range(list1_size):
    list1.append(int(input()))
list2_size=int(input("enter the size of list2:"))
print("enter the elements of list2:")
for i in range(list2_size):
    list2.append(int(input()))
print(list1,list2)
combinedList=list1+list2
print(combinedList)
evenList=[]
oddList=[]
for i in combinedList:
    if i % 2==0:
        evenList.append(i)
    else:
        oddList.append(i)
print(evenList)
print(oddList)
evenList.sort()
oddList.sort()
print(f"even lisit is {evenList}")
print(f"odd lisit is{oddList}")
merged_list=evenList+oddList
print(f"mergedList:{merged_list}")