'''author:Aishwarya
date:19-11-24'''
num=int(input("enter a number"))
print("increasing pattern")
for i in range(1,num):
    for j in range(i):
        print("*",end="")
    print()



print("decreasing pattern")
for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print()



print("hill pattern")
num=int(input("enter a number"))
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for i in range(2*i-1):
       print("*",end=" ")
    print()




for i in range(num,0,-1):
    for j in range(num-i):
        print(" ", end="")
    for i in range(2 * i - 1):
            print("*", end=" ")
    print()



